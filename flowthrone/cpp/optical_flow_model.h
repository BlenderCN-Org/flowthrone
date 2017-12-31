#pragma once
#include "opencv2/core/core.hpp"
#include "google/protobuf/message.h"

namespace flowthrone {

// Interface that the optical flow algorithm should implement.
class OpticalFlowModel {
 public:
  virtual bool Run(const cv::Mat& I0, const cv::Mat& I1, cv::Mat* flow) = 0;

  // Instantiates the derived class from the configuration proto.
  static std::unique_ptr<OpticalFlowModel> Create(
      const google::protobuf::Message& opts);
  // Instantiates the derived class from filename that contains the
  // configuration proto.
  static std::unique_ptr<OpticalFlowModel> Create(const std::string& filename);
};

}  // namespace flowthrone
