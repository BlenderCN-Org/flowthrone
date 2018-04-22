#include "flow_smoothing.h"
#include <array>
#include "glog/logging.h"
#include "opencv2/imgproc/imgproc.hpp"
#include "utils.h"

namespace flowthrone {

cv::Mat DenoiseColorWeightedFilterInternal(const cv::Mat& flow_in,
                                           const cv::Mat& image,
                                           const DenoisingOptions& options) {
  CHECK_EQ(flow_in.rows, image.rows);
  CHECK_EQ(flow_in.cols, image.cols);
  CHECK_EQ(CV_32FC2, flow_in.type());
  CHECK_EQ(CV_32FC1, image.type());

  // Cache the exponential.
  constexpr int kNumPoints = 250;
  constexpr float kMaxValue = 5.0f;
  std::vector<float> exp_cache = GetExponentialVector(kMaxValue, kNumPoints);
  auto exp_index = [kMaxValue, kNumPoints](float val) {
    return std::min(kNumPoints - 1,
                    static_cast<int>(val * (kNumPoints / kMaxValue)));
  };

  constexpr float kEps = 1e-6;
  int window_size = options.window_size;
  cv::Mat flow_out(flow_in.rows, flow_in.cols, CV_32FC2);
  float inv_sigma_intensity_sq = std::numeric_limits<float>::max();
  float inv_sigma_distance_sq = std::numeric_limits<float>::max();
  if (options.sigma_intensity > 0) {
    inv_sigma_intensity_sq =
        1.0f / options.sigma_intensity / options.sigma_intensity;
  }
  if (options.sigma_distance > 0) {
    inv_sigma_distance_sq =
        1.0f / options.sigma_distance / options.sigma_distance;
  }
  for (int y = 0; y < image.rows; ++y) {
    int y_lo = std::max(0, y - window_size);
    int y_hi = std::min(image.rows - 1, y + window_size);
    const float* image_values_at_y = image.ptr<float>(y);
    cv::Vec2f* output_flow_at_y = flow_out.ptr<cv::Vec2f>(y);
    for (int x = 0; x < image.cols; ++x) {
      int x_lo = std::max(0, x - window_size);
      int x_hi = std::min(image.cols - 1, x + window_size);

      float image_value = image_values_at_y[x];
      cv::Vec2f output_flow{0, 0};
      float Z = 0.0f;
      for (int yy = y_lo; yy <= y_hi; ++yy) {
        int dy_sq = (yy - y) * (yy - y);
        const float* image_values_at_yy = image.ptr<float>(yy);
        const cv::Vec2f* flow_at_yy = flow_in.ptr<cv::Vec2f>(yy);
        for (int xx = x_lo; xx <= x_hi; ++xx) {
          int dx_sq = (xx - x) * (xx - x);
          const float distance_weight = (dy_sq + dx_sq) * inv_sigma_distance_sq;
          const float I = image_values_at_yy[xx];
          const float intensity_weight =
              (image_value - I) * (image_value - I) * inv_sigma_intensity_sq;

          const float exp_arg = intensity_weight + distance_weight;
          const float weight = exp_cache[exp_index(exp_arg)] + kEps;
          Z += weight;
          output_flow += weight * flow_at_yy[xx];
        }
      }
      output_flow_at_y[x] = output_flow / Z;
    }
  }
  return flow_out;
}

cv::Mat DenoiseColorWeightedFilter(const cv::Mat& flow_in, const cv::Mat& image,
                                   const DenoisingOptions& options) {
  cv::Mat image_gray;
  if (image.type() == CV_8UC3) {
    cv::cvtColor(image, image_gray, CV_BGR2GRAY);
    image_gray.convertTo(image_gray, CV_32FC1);
    return DenoiseColorWeightedFilter(flow_in, image_gray, options);
  } else if (image.type() == CV_32FC3) {
    cv::cvtColor(image, image_gray, CV_BGR2GRAY);
  } else if (image.type() == CV_32FC1) {
    image_gray = image;
  } else {
    LOG(FATAL) << "Couldn't interpret image type. Currently can only support "
                  "CV_8UC3, CV_32FCP{1,3}. Maybe your image is different?";
  }
  return DenoiseColorWeightedFilterInternal(flow_in, image_gray, options);
}

}  // namespace flowthrone
