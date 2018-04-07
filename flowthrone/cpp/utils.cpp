#include "utils.h"
#include <glog/logging.h>
#include <opencv2/imgproc/imgproc.hpp>

namespace flowthrone {

std::vector<cv::Mat> GetFlowMaps(const cv::Mat& flow) {
  std::vector<cv::Mat> flow_maps;
  cv::split(flow, flow_maps);
  // Compute x' = x + w(x,y), y' = y + w(x,y)
  for (int r = 0; r < flow.rows; ++r) {
    flow_maps[1].row(r) += r;
    float* data = flow_maps[0].ptr<float>(r);
    for (int c = 0; c < flow.cols; ++c) {
      data[c] += c;
    }
  }
  return flow_maps;
}

std::vector<std::pair<float, float>> WarpWithFlow(
    const std::vector<std::pair<float, float>>& points, const cv::Mat& flow) {
  std::vector<std::pair<float, float>> warped;
  warped.reserve(points.size());
  for (const auto& p : points) {
    float x = p.first;
    float y = p.second;
    // TODO: Currently just does the 'nearest neighbor' flow warping, which is
    // stupid and terrible, but easy.
    int x_rounded = std::max(std::min<int>(round(x), flow.cols - 1), 0);
    int y_rounded = std::max(std::min<int>(round(y), flow.rows - 1), 0);
    const cv::Vec2f& warp = flow.at<cv::Vec2f>(y_rounded, x_rounded);
    warped.emplace_back(x - warp[0], y - warp[1]);
  }
  return warped;
}

cv::Mat FlowMagnitude(const cv::Mat& flow) {
  CHECK_EQ(CV_32FC2, flow.type()) << "Incorrect cv::Mat format for flow";
  std::vector<cv::Mat> flow_maps;
  cv::split(flow, flow_maps);
  cv::Mat magnitude, dxdx, dydy;
  cv::multiply(flow_maps[0], flow_maps[0], dxdx);
  cv::multiply(flow_maps[1], flow_maps[1], dydy);
  cv::sqrt(dxdx + dydy, magnitude);
  return magnitude;
}

cv::Mat WarpWithFlow(const cv::Mat& I, const cv::Mat& flow) {
  CHECK_EQ(CV_32FC2, flow.type()) << "Incorrect cv::Mat format for flow";
  std::vector<cv::Mat> flow_maps = GetFlowMaps(flow);
  cv::Mat I_warped;
  cv::remap(I, I_warped, flow_maps[0], flow_maps[1], cv::INTER_LINEAR);
  return I_warped;
}

cv::Mat ComputeResidual(const cv::Mat& I0, const cv::Mat& I1,
                        const cv::Mat& flow) {
  return I0 - WarpWithFlow(I1, flow);
}

cv::Mat ResampleFlow(const cv::Mat& flow, const cv::Size& target_size) {
  CHECK_EQ(2, flow.channels());
  cv::Mat flow_out;
  cv::resize(flow, flow_out, target_size);
  std::vector<cv::Mat> flow_fields;
  cv::split(flow_out, flow_fields);
  CHECK_EQ(2, flow_fields.size());
  flow_fields[0] *= static_cast<float>(flow.cols) / target_size.width;
  flow_fields[1] *= static_cast<float>(flow.rows) / target_size.height;
  cv::merge(flow_fields, flow_out);
  return flow_out;
}

std::vector<float> Linspace(float min, float max, int num) {
  if (num == 0) {
    return {};
  }
  if (num == 1 && (min == max)) {
    return {min};
  }
  CHECK_LT(min, max)
      << "Asked to linspace points where 'smaller' value > 'larger' value.";
  CHECK_LT(1, num) << "If min/max are distinct, then must have at least two "
                      "points as input to "
                      "linspace. ";
  std::vector<float> out(num);
  float dx = (max - min) / (num - 1);
  for (int i = 0; i < num; ++i) {
    out[i] = min + i * dx;
  }
  return out;
}

std::vector<std::pair<float, float>> Meshgrid(const std::vector<float>& x,
                                              const std::vector<float>& y) {
  if (x.empty() || y.empty()) {
    return {};
  }
  std::vector<std::pair<float, float>> out;
  out.reserve(x.size() * y.size());
  for (float yy : y) {
    for (float xx : x) {
      out.emplace_back(xx, yy);
    }
  }
  return out;
}

cv::Mat TriangleKernel(cv::Size size) {
  int xc = size.width / 2;
  int yc = size.height / 2;
  cv::Mat kernel(size, CV_32FC1);
  for (int y = 0; y < kernel.rows; ++y) {
    float* row = reinterpret_cast<float*>(kernel.row(y).data);
    float wy = yc > 0 ? 1.0f - std::abs(y - yc) / float(yc) : 1.0f;
    for (int x = 0; x < kernel.cols; ++x) {
      float wx = xc > 0 ? 1.0f - std::abs(x - xc) / float(xc) : 1.0f;
      row[x] = wx * wy;
    }
  }
  return kernel;
}

cv::Mat ExponentialKernel(cv::Size size, float sigma) {
  float xc = size.width / 2.0f;
  float yc = size.height / 2.0f;
  cv::Mat kernel(size, CV_32FC1);
  for (int y = 0; y < kernel.rows; ++y) {
    float* row = reinterpret_cast<float*>(kernel.row(y).data);
    float dy = (y - yc) / yc;
    for (int x = 0; x < kernel.cols; ++x) {
      float dx = (x - xc) / xc;
      float dist = std::sqrt(dx * dx + dy * dy);
      row[x] = exp(-dist / sigma);
    }
  }
  return kernel;
}

cv::Mat SquaredExponentialKernel(cv::Size size, float sigma) {
  float xc = size.width / 2.0f;
  float yc = size.height / 2.0f;
  cv::Mat kernel(size, CV_32FC1);
  float half_inv_sigma_sq = 0.5f / (sigma * sigma);
  for (int y = 0; y < kernel.rows; ++y) {
    float* row = reinterpret_cast<float*>(kernel.row(y).data);
    float dy = (y - yc) / yc;
    float dy_sq = dy * dy;
    for (int x = 0; x < kernel.cols; ++x) {
      float dx = (x - xc) / xc;
      float dx_sq = dx * dx;
      row[x] = exp(-half_inv_sigma_sq * (dx_sq + dy_sq));
    }
  }
  return kernel;
}

std::vector<cv::Rect> SplitImage(cv::Size image_sz, cv::Size patch_sz,
                                 cv::Size stride, SplitImageMode mode) {
  CHECK(stride.width >= 1 && stride.height >= 1) << "Stride must be positive.";
  CHECK(image_sz.width >= patch_sz.width && image_sz.height >= patch_sz.height)
      << "Currently only support tiling of images that are at least as large "
         "as the patch size.";
  CHECK(patch_sz.width >= stride.width && patch_sz.height >= stride.height)
      << "Patch must be larger than stride. In other words, it is only "
         "possible to densely tile the image.";

  std::vector<std::pair<int, int>> y_offset_and_sz{{0, patch_sz.height}};
  std::vector<std::pair<int, int>> x_offset_and_sz{{0, patch_sz.width}};

  if (mode == SplitImageMode::kSizeConstant) {
    int last_y_offset = image_sz.height - patch_sz.height;
    while (y_offset_and_sz.back().first < last_y_offset) {
      int y =
          std::min(y_offset_and_sz.back().first + stride.height, last_y_offset);
      y_offset_and_sz.push_back(std::make_pair(y, patch_sz.height));
    }
    int last_x_offset = image_sz.width - patch_sz.width;
    while (x_offset_and_sz.back().first < last_x_offset) {
      int x =
          std::min(x_offset_and_sz.back().first + stride.width, last_x_offset);
      x_offset_and_sz.push_back(std::make_pair(x, patch_sz.width));
    }
  } else {  // mode == SplitImageMode::kStrideConstant
    int last_y_offset = image_sz.height - stride.height;
    while (y_offset_and_sz.back().first < last_y_offset) {
      int y_left = y_offset_and_sz.back().first + stride.height;
      int y_right = std::min(image_sz.height, y_left + patch_sz.height);
      y_offset_and_sz.push_back(std::make_pair(y_left, y_right - y_left));
    }
    int last_x_offset = image_sz.width - stride.width;
    while (x_offset_and_sz.back().first < last_x_offset) {
      int x_left = x_offset_and_sz.back().first + stride.width;
      int x_right = std::min(image_sz.width, x_left + patch_sz.width);
      x_offset_and_sz.push_back(std::make_pair(x_left, x_right - x_left));
    }
  }
  std::vector<cv::Rect> output;
  output.reserve(x_offset_and_sz.size() * y_offset_and_sz.size());
  for (const auto& pair_y : y_offset_and_sz) {
    for (const auto& pair_x : x_offset_and_sz) {
      cv::Rect rect(pair_x.first, pair_y.first, pair_x.second, pair_y.second);
      output.push_back(rect);
    }
  }
  return output;
};

cv::Mat ComputeFlowDivergence(const cv::Mat& flow) {
  CHECK_EQ(CV_32FC2, flow.type());

  std::vector<cv::Mat> flow_split;
  cv::split(flow, flow_split);

  cv::Mat w_x_dx, w_y_dy;
  cv::Mat kx = (cv::Mat_<float>(1, 3) << -0.5, 0, 0.5);
  cv::Mat ky = (cv::Mat_<float>(3, 1) << -0.5, 0, 0.5);
  cv::filter2D(flow_split[0], w_x_dx, -1, kx);
  cv::filter2D(flow_split[1], w_y_dy, -1, ky);
  CHECK_EQ(CV_32FC1, w_x_dx.type());
  return w_x_dx + w_y_dy;
}

cv::Mat ProbabilityOfOcclusion(const cv::Mat& I0, const cv::Mat& I1,
                               const cv::Mat& flow, float sigma_d,
                               float sigma_i) {
  cv::Mat flow_div = ComputeFlowDivergence(flow);
  cv::min(flow_div, cv::Scalar(0.0f), flow_div);

  // Compute brightness constancy violation.
  cv::Mat I_dt = WarpWithFlow(I1, flow) - I0;  // I1_warped - I0
  CHECK_EQ(I_dt.type(), CV_32FC1) << "Passed images must be of type CV_32FC1";

  constexpr int kNumExpPoints = 250;
  constexpr float kExpMaxValue = 10.0;
  std::vector<float> exp_cache =
      GetExponentialVector(kExpMaxValue, kNumExpPoints);
  auto exp_index = [kExpMaxValue, kNumExpPoints](float val) {
    return std::min(kNumExpPoints - 1,
                    static_cast<int>(std::min<float>(kExpMaxValue, val) *
                                     (kNumExpPoints / kExpMaxValue)));
  };
  cv::Mat p_occ(I0.rows, I0.cols, CV_32FC1);
  const float* I_dt_data = reinterpret_cast<const float*>(I_dt.data);
  const float* flow_div_data = reinterpret_cast<const float*>(flow_div.data);
  float* p_occ_data = reinterpret_cast<float*>(p_occ.data);

  const float sigma_i_inv = 1.0f / sigma_i;
  const float sigma_d_inv = 1.0f / sigma_d;
  for (size_t i = 0; i < p_occ.total(); ++i) {
    float argexp1 = 0.5 * I_dt_data[i] * sigma_i_inv;
    float argexp2 = 0.5 * flow_div_data[i] * sigma_d_inv;
    float argexp_total = argexp1 * argexp1 + argexp2 * argexp2;
    p_occ_data[i] = 1.0f - exp_cache[exp_index(argexp_total)];
  }
  return p_occ;
}

std::vector<float> GetExponentialVector(float max_value, int num_points) {
  CHECK(max_value > 0);
  std::vector<float> exps(num_points);
  for (int i = 0; i < num_points; ++i) {
    exps[i] = exp(-i * max_value / num_points);
  }
  return exps;
}

}  // namespace flowthrone
