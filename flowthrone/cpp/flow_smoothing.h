#pragma once
#include "opencv2/core/core.hpp"

namespace flowthrone {

struct DenoisingOptions {
  float sigma_intensity = 1.0;
  float sigma_distance = 1.0;
  int window_size = 5;
};

// Filters optical flow using cross-bilateral filter -- flow values are
// averaged over a neighborhood, but the weights are computed using image
// intensity differences.
cv::Mat DenoiseColorWeightedFilter(const cv::Mat& flow_in, const cv::Mat& I0,
                                   const DenoisingOptions& options);

}  // namespace flowthrone
