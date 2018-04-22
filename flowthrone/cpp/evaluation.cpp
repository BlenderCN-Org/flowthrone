#include "evaluation.h"
#include "glog/logging.h"

using google::protobuf::Map;
using google::protobuf::RepeatedPtrField;
using google::protobuf::RepeatedField;

namespace flowthrone {

namespace {

void CheckForSanityErrors(const cv::Mat& flow, const cv::Mat& flow_gt) {
  CHECK_EQ(CV_32FC2, flow.type()) << "Must be CV_32FC2";
  CHECK_EQ(CV_32FC2, flow_gt.type()) << "Must be CV_32FC2";
  CHECK_EQ(flow.rows, flow_gt.rows);
  CHECK_EQ(flow.cols, flow_gt.cols);
}

// NaN's are 'sentinel' values in groundtruth where flow is unavailable.
bool IsInvalidWarp(const cv::Vec2f& uv) {
  return std::isnan(uv[0]) || std::isnan(uv[1]);
}

}  // namespace

float FlowEndpointError(const cv::Mat& flow, const cv::Mat& flow_gt,
                        cv::Mat* flow_error) {
  CheckForSanityErrors(flow, flow_gt);

  cv::Mat error(flow.rows, flow.cols, CV_32FC1, cv::Scalar(0.0f));
  float sum_of_errors = 0.0f;
  for (int r = 0; r < flow.rows; ++r) {
    for (int c = 0; c < flow.cols; ++c) {
      const cv::Vec2f& uv_gt = flow_gt.at<cv::Vec2f>(r, c);
      const cv::Vec2f& uv = flow.at<cv::Vec2f>(r, c);
      if (IsInvalidWarp(uv_gt)) {
        continue;
      }
      const float err_sq = (uv[0] - uv_gt[0]) * (uv[0] - uv_gt[0]) +
                           (uv[1] - uv_gt[1]) * (uv[1] - uv_gt[1]);
      error.at<float>(r, c) = sqrt(err_sq);
      sum_of_errors += sqrt(err_sq);
    }
  }
  if (flow_error) {
    *flow_error = error;
  }
  return sum_of_errors / (flow.rows * flow.cols);
}

float FlowAngularError(const cv::Mat& flow, const cv::Mat& flow_gt,
                       cv::Mat* flow_error) {
  CheckForSanityErrors(flow, flow_gt);

  cv::Mat error(flow.rows, flow.cols, CV_32FC1, cv::Scalar(0.0f));
  float sum_of_errors = 0.0f;
  for (int r = 0; r < flow.rows; ++r) {
    for (int c = 0; c < flow.cols; ++c) {
      const cv::Vec2f& uv_gt = flow_gt.at<cv::Vec2f>(r, c);
      const cv::Vec2f& uv = flow.at<cv::Vec2f>(r, c);
      if (IsInvalidWarp(uv_gt)) {
        continue;
      }
      // Promote to double, for numerical reasons.
      const double numerator = 1.0 + uv_gt[0] * uv[0] + uv_gt[1] * uv[1];
      const double denominator =
          std::sqrt(1.0 + uv_gt[0] * uv_gt[0] + uv_gt[1] * uv_gt[1]) *
          std::sqrt(1.0 + uv[0] * uv[0] + uv[1] * uv[1]);
      double ratio = numerator / denominator;
      ratio = std::min(std::max(ratio, -1.0), +1.0);
      const double e = std::acos(ratio);
      CHECK(0 <= e && e <= M_PI);
      error.at<float>(r, c) = e;
      sum_of_errors += e;
    }
  }
  if (flow_error) {
    *flow_error = error;
  }
  return sum_of_errors / (flow.rows * flow.cols);
}

namespace {

void CheckIntervalsAreSane(const RepeatedPtrField<Interval>& intervals) {
  for (const auto& interval : intervals) {
    CHECK_LT(interval.lo(), interval.hi())
        << "The interval [a, b) must have a < b (strictly!)";
  }
}

bool InInterval(const Interval& interval, float value) {
  return interval.lo() <= value && value < interval.hi();
}

IntervalValue CreateIntervalValue(const Interval interval, float value) {
  IntervalValue pair;
  *pair.mutable_interval() = interval;
  pair.set_value(value);
  return pair;
}

Interval CreateInterval(const std::pair<float, float>& pair) {
  Interval interval;
  interval.set_lo(pair.first);
  interval.set_hi(pair.second);
  return interval;
}

RepeatedPtrField<IntervalValue> Zip(const RepeatedPtrField<Interval>& intervals,
                                    const std::vector<float>& values) {
  CHECK_EQ(intervals.size(), values.size());
  RepeatedPtrField<IntervalValue> out;
  for (int i = 0; i < intervals.size(); ++i) {
    *out.Add() = CreateIntervalValue(intervals[i], values[i]);
  }
  return out;
}

std::pair<RepeatedPtrField<Interval>, std::vector<float>> Unzip(
    const RepeatedPtrField<IntervalValue>& zipped) {
  std::vector<float> values;
  RepeatedPtrField<Interval> intervals;
  for (int i = 0; i < zipped.size(); ++i) {
    *intervals.Add() = zipped[i].interval();
    values.push_back(zipped[i].value());
  }
  return std::make_pair(std::move(intervals), std::move(values));
}

}  // namespace

std::vector<float> AverageErrorByInterval(
    const cv::Mat& flow_gt, const cv::Mat& error,
    const RepeatedPtrField<Interval>& intervals) {
  CHECK_EQ(error.type(), CV_32FC1) << "Error input must have type CV_32FC1";
  CHECK_EQ(flow_gt.type(), CV_32FC2) << "Flow input must have type CV_32FC2";
  CHECK_EQ(error.total(), flow_gt.total()) << "Input sizes must match!";
  CheckIntervalsAreSane(intervals);
  if (intervals.empty()) {
    return std::vector<float>{};
  }
  std::vector<float> out(intervals.size(), 0.0f);
  std::vector<int> counts(intervals.size(), 0);

  const float* error_data = reinterpret_cast<const float*>(error.data);
  const cv::Vec2f* flow_gt_data =
      reinterpret_cast<const cv::Vec2f*>(flow_gt.data);
  for (size_t i = 0; i < error.total(); ++i) {
    const cv::Vec2f& uv = flow_gt_data[i];
    if (IsInvalidWarp(uv)) {
      continue;
    }
    float uv_mag = std::sqrt(uv[0] * uv[0] + uv[1] * uv[1]);
    for (int idx = 0; idx < intervals.size(); ++idx) {
      if (InInterval(intervals[idx], uv_mag)) {
        counts[idx]++;
        out[idx] += error_data[i];
      }
    }
  }
  for (int idx = 0; idx < intervals.size(); ++idx) {
    if (counts[idx]) {
      out[idx] /= counts[idx];
    } else {
      out[idx] = std::numeric_limits<float>::quiet_NaN();
    }
  }
  return out;
}

EvaluationOutput::Result ComputeAverageSummary(
    const RepeatedPtrField<EvaluationOutput::Result>& results) {
  double ee = 0;
  double ae = 0;
  double elapsed = 0;

  RepeatedPtrField<Interval> ee_intervals;
  RepeatedPtrField<Interval> ae_intervals;
  if (results.size()) {
    ee_intervals = Unzip(results[0].endpoint_error_in_interval()).first;
    ae_intervals = Unzip(results[0].angular_error_in_interval()).first;
  }
  std::vector<float> ee_in_interval_values(ee_intervals.size(), 0.0f);
  std::vector<float> ae_in_interval_values(ae_intervals.size(), 0.0f);

  for (const auto& result : results) {
    ee += result.average_endpoint_error() / results.size();
    ae += result.average_angular_error() / results.size();
    elapsed += result.elapsed() / results.size();

    {  // Aggregate per-interval endpoint error values.
      CHECK_EQ(result.endpoint_error_in_interval_size(), ee_intervals.size());
      auto values = Unzip(result.endpoint_error_in_interval()).second;
      for (size_t i = 0; i < values.size(); ++i) {
        if (std::isnan(values[i])) {
          continue;
        }
        ee_in_interval_values[i] += values[i] / results.size();
      }
    }
    {  // Aggregate per-interval angular error values.
      CHECK_EQ(result.angular_error_in_interval_size(), ae_intervals.size());
      auto values = Unzip(result.angular_error_in_interval()).second;
      for (size_t i = 0; i < values.size(); ++i) {
        if (std::isnan(values[i])) {
          continue;
        }
        ae_in_interval_values[i] += values[i] / results.size();
      }
    }
  }

  EvaluationOutput::Result summary;
  summary.set_average_angular_error(ae);
  summary.set_average_endpoint_error(ee);
  summary.set_elapsed(elapsed);
  *summary.mutable_endpoint_error_in_interval() =
      Zip(ee_intervals, ee_in_interval_values);
  *summary.mutable_angular_error_in_interval() =
      Zip(ae_intervals, ae_in_interval_values);
  return summary;
}

namespace {

// Returns a vector that satisfies:
//  y[i][j] = x[j][i]
// and consequently:
//  y.size() == x[0].size() and y[0].size() == x.size()
std::vector<std::vector<float>> Reshape(
    const std::vector<std::vector<float>>& x) {
  if (x.empty()) {
    return std::vector<std::vector<float>>{};
  }
  // Verify that all inner dimensions are the same.
  for (const auto& x_vec : x) {
    CHECK_EQ(x_vec.size(), x[0].size());
  }

  std::vector<std::vector<float>> y(x[0].size(), std::vector<float>(x.size()));
  for (size_t i = 0; i < x.size(); ++i) {
    for (size_t j = 0; j < x[i].size(); ++j) {
      y[j][i] = x[i][j];
    }
  }
  return y;
}

// Note: extraction of singular fields could really be done with reflection,
// but it doesn't help readability any, and since we don't really care about
// genericity much, doesn't seem worth it...
std::vector<float> ExtractAndSort(
    const RepeatedPtrField<EvaluationOutput::Result>& results,
    std::function<float(const EvaluationOutput::Result&)> extractor) {
  std::vector<float> out;
  out.reserve(results.size());
  for (const auto& result : results) {
    out.push_back(extractor(result));
  }
  std::sort(out.begin(), out.end());
  return out;
}

std::vector<std::vector<float>> ExtractAndSortInInterval(
    const RepeatedPtrField<EvaluationOutput::Result>& results,
    std::function<
        RepeatedPtrField<IntervalValue>(const EvaluationOutput::Result&)>
        extractor) {
  std::vector<std::vector<float>> out;
  out.reserve(results.size());
  for (const auto& result : results) {
    out.push_back(Unzip(extractor(result)).second);
  }
  // Rearrange inner and outer dimensions of the vectors. After doing that,
  // out[i] corresponds to all results for a given interval, and out.size()
  // has the same number as the number of intervals.
  out = Reshape(out);
  for (auto& out_vec : out) {
    std::sort(out_vec.begin(), out_vec.end());
    // Remove NaNs -- they affect percentiles in ways that are useless to us.
    out_vec.erase(std::remove_if(out_vec.begin(), out_vec.end(),
                                 [](float x) { return std::isnan(x); }),
                  out_vec.end());
  }
  return out;
}

std::vector<float> SortedEndpointErrorValues(
    const RepeatedPtrField<EvaluationOutput::Result>& results) {
  return ExtractAndSort(results, [](const EvaluationOutput::Result& x) {
    return x.average_endpoint_error();
  });
}

std::vector<float> SortedAngularErrorValues(
    const RepeatedPtrField<EvaluationOutput::Result>& results) {
  return ExtractAndSort(results, [](const EvaluationOutput::Result& x) {
    return x.average_angular_error();
  });
}

std::vector<float> SortedElapsedValues(
    const RepeatedPtrField<EvaluationOutput::Result>& results) {
  return ExtractAndSort(
      results, [](const EvaluationOutput::Result& x) { return x.elapsed(); });
}

std::vector<std::vector<float>> SortedEndpointErrorInInterval(
    const RepeatedPtrField<EvaluationOutput::Result>& results) {
  return ExtractAndSortInInterval(results,
                                  [](const EvaluationOutput::Result& x) {
                                    return x.endpoint_error_in_interval();
                                  });
}

std::vector<std::vector<float>> SortedAngularErrorInInterval(
    const RepeatedPtrField<EvaluationOutput::Result>& results) {
  return ExtractAndSortInInterval(results,
                                  [](const EvaluationOutput::Result& x) {
                                    return x.angular_error_in_interval();
                                  });
}

Map<int, EvaluationOutput::Result> InitializePercentileMap(
    const RepeatedField<int>& percentiles) {
  Map<int, EvaluationOutput::Result> map;
  for (int percentile : percentiles) {
    CHECK(0 <= percentile && percentile <= 100)
        << "Percentile must be specified as an integer in {0, .., 100} range.";
    map[percentile] = EvaluationOutput::Result{};
  }
  return map;
}

void FillPercentileMapWithAverageEndpointErrors(
    const RepeatedPtrField<EvaluationOutput::Result>& results,
    const RepeatedField<int>& percentiles,
    Map<int, EvaluationOutput::Result>& map) {
  auto values = SortedEndpointErrorValues(results);
  for (int percentile : percentiles) {
    int idx = (percentile / 100.0f) * (values.size() - 1);
    EvaluationOutput::Result& summary = map[percentile];
    summary.set_average_endpoint_error(values[idx]);
  }
}

void FillPercentileMapWithAverageAngularErrors(
    const RepeatedPtrField<EvaluationOutput::Result>& results,
    const RepeatedField<int>& percentiles,
    Map<int, EvaluationOutput::Result>& map) {
  auto values = SortedAngularErrorValues(results);
  for (int percentile : percentiles) {
    int idx = (percentile / 100.0f) * (values.size() - 1);
    EvaluationOutput::Result& summary = map[percentile];
    summary.set_average_angular_error(values[idx]);
  }
}

void FillPercentileMapWithElapsed(
    const RepeatedPtrField<EvaluationOutput::Result>& results,
    const RepeatedField<int>& percentiles,
    Map<int, EvaluationOutput::Result>& map) {
  auto values = SortedElapsedValues(results);
  for (int percentile : percentiles) {
    int idx = (percentile / 100.0f) * (values.size() - 1);
    EvaluationOutput::Result& summary = map[percentile];
    summary.set_elapsed(values[idx]);
  }
}

std::vector<float> ValuesForPercentile(
    const std::vector<std::vector<float>>& values, int percentile) {
  std::vector<float> percentile_values;
  for (const auto& v : values) {
    if (v.empty()) {
      percentile_values.push_back(std::numeric_limits<float>::quiet_NaN());
    } else {
      int idx = (percentile / 100.0f) * (v.size() - 1);
      percentile_values.push_back(v[idx]);
    }
  }
  return percentile_values;
}

void FillPercentileMapWithEndpointErrorInInterval(
    const RepeatedPtrField<EvaluationOutput::Result>& results,
    const RepeatedField<int>& percentiles,
    Map<int, EvaluationOutput::Result>& map) {
  auto values = SortedEndpointErrorInInterval(results);
  auto intervals = Unzip(results[0].endpoint_error_in_interval()).first;
  for (int percentile : percentiles) {
    EvaluationOutput::Result& summary = map[percentile];
    std::vector<float> percentile_values =
        ValuesForPercentile(values, percentile);
    *summary.mutable_endpoint_error_in_interval() =
        Zip(intervals, percentile_values);
  }
}

void FillPercentileMapWithAngularErrorInInterval(
    const RepeatedPtrField<EvaluationOutput::Result>& results,
    const RepeatedField<int>& percentiles,
    Map<int, EvaluationOutput::Result>& map) {
  auto values = SortedAngularErrorInInterval(results);
  auto intervals = Unzip(results[0].angular_error_in_interval()).first;
  for (int percentile : percentiles) {
    EvaluationOutput::Result& summary = map[percentile];
    std::vector<float> percentile_values =
        ValuesForPercentile(values, percentile);
    *summary.mutable_angular_error_in_interval() =
        Zip(intervals, percentile_values);
  }
}

}  // namespace

Map<int, EvaluationOutput::Result> ComputePercentileSummary(
    const RepeatedPtrField<EvaluationOutput::Result>& results,
    const RepeatedField<int>& percentiles) {
  CHECK_LE(1, results.size())
      << "You must provide a nonzero vector to this function.";
  Map<int, EvaluationOutput::Result> map = InitializePercentileMap(percentiles);

  FillPercentileMapWithAverageAngularErrors(results, percentiles, map);
  FillPercentileMapWithAverageEndpointErrors(results, percentiles, map);
  FillPercentileMapWithElapsed(results, percentiles, map);

  FillPercentileMapWithAngularErrorInInterval(results, percentiles, map);
  FillPercentileMapWithEndpointErrorInInterval(results, percentiles, map);
  return map;
}

EvaluationOutput::Result Evaluate(const cv::Mat& prediction,
                                  const cv::Mat& groundtruth,
                                  const EvaluationInput::Options& options) {
  cv::Mat ee, ae;
  float average_ae = FlowAngularError(prediction, groundtruth, &ae);
  float average_ee = FlowEndpointError(prediction, groundtruth, &ee);

  EvaluationOutput::Result result;
  result.set_average_angular_error(average_ae);
  result.set_average_endpoint_error(average_ee);

  const auto& intervals = options.displacement_interval();
  *result.mutable_endpoint_error_in_interval() =
      Zip(intervals, AverageErrorByInterval(groundtruth, ee, intervals));
  *result.mutable_angular_error_in_interval() =
      Zip(intervals, AverageErrorByInterval(groundtruth, ae, intervals));
  return result;
}

EvaluationInput::Options GetDefaultEvaluationOptions() {
  EvaluationInput::Options options;
  for (int p : std::vector<int>{10, 25, 50, 75, 90}) {
    options.add_summary_percentile(p);
  }
  // Evaluate over the same set of displacement intervals that is used in
  // Sintel benchmark.
  for (const auto& pair :
       std::vector<std::pair<float, float>>{{0, 10}, {10, 40}, {40, 1e9}}) {
    *options.add_displacement_interval() = CreateInterval(pair);
  }
  return options;
}

}  // namespace flowthrone
