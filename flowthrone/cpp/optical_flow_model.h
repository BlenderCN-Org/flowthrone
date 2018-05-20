#pragma once
#include "google/protobuf/message.h"
#include "opencv2/core/core.hpp"

namespace flowthrone {

// Interface that the optical flow algorithm should implement.
class OpticalFlowModel {
 public:
  // Structure containing result of a single call to OpticaFlowModel::Run.
  struct Result {
    cv::Mat flow;
    bool success;
  };

  virtual Result Run(const cv::Mat& I0, const cv::Mat& I1) = 0;

  // Instantiates the derived class from the configuration proto.
  static std::unique_ptr<OpticalFlowModel> Create(
      const google::protobuf::Message& opts);
  // Instantiates the derived class from filename that contains the
  // configuration proto.
  static std::unique_ptr<OpticalFlowModel> Create(const std::string& filename);
};

}  // namespace flowthrone
