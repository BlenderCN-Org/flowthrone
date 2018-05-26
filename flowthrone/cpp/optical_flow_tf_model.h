#pragma once
#include "flowthrone.pb.h"
#include "opencv2/core/core.hpp"
#include "optical_flow_model.h"
#include "tensorflow/core/public/session.h"

namespace flowthrone {

namespace internal {
struct Context;
}  // namespace internal

class OpticalFlowTensorFlowModel : public OpticalFlowModel {
 public:
  OpticalFlowTensorFlowModel(const OpticalFlowTensorFlowModelOptions& opt);
  virtual ~OpticalFlowTensorFlowModel();

  Result Run(const cv::Mat& I0, const cv::Mat& I1) override;

 private:
  void Postprocess(const cv::Mat& I0, const cv::Mat& I1, cv::Mat* flow);
  OpticalFlowTensorFlowModelOptions opts_;

  std::unique_ptr<internal::Context> context_;
};

}  // namespace flowthrone
