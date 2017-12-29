#include "evaluation.h"
#include "glog/logging.h"

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
      const float numerator = 1.0f + uv_gt[0] * uv[0] + uv_gt[1] * uv[1];
      const float denominator =
          sqrt(1 + uv_gt[0] * uv_gt[0] + uv_gt[1] * uv_gt[1]) *
          sqrt(1 + uv[0] * uv[0] + uv[1] * uv[1]);
      float ratio = numerator / denominator;
      ratio = std::min(std::max(ratio, -1.0f), +1.0f);
      const float e = acos(ratio);
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

EvaluationOutput::Result ComputeAverageSummary(
    const google::protobuf::RepeatedPtrField<EvaluationOutput::Result>&
        results) {
  double ee = 0;
  double ae = 0;
  double elapsed = 0;
  for (const auto& result : results) {
    ee += result.average_endpoint_error() / results.size();
    ae += result.average_angular_error() / results.size();
    elapsed += result.elapsed() / results.size();
  }
  EvaluationOutput::Result summary;
  summary.set_average_angular_error(ae);
  summary.set_average_endpoint_error(ee);
  summary.set_elapsed(elapsed);
  return summary;
}

}  // namespace flowthrone
