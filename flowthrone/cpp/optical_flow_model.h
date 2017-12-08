#pragma once
#include "opencv2/core/core.hpp"

namespace flowthrone {

// Interface that the optical flow algorithm should implement.
class OpticalFlowModel {
 public:
  virtual bool Run(const cv::Mat& I0, const cv::Mat& I1, cv::Mat* flow) = 0;
};

}  // namespace flowthrone
