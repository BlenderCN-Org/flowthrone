#pragma once
#include "opencv2/core/core.hpp"
#include "tensorflow/core/public/session.h"
#include "optical_flow_model.h"
#include "flowthrone.pb.h"

namespace flowthrone {

class OpticalFlowTensorFlowModel : public OpticalFlowModel {
 public:
  OpticalFlowTensorFlowModel(const OpticalFlowTensorFlowModelOptions& opt);
  virtual ~OpticalFlowTensorFlowModel();

  bool Run(const cv::Mat& I0, const cv::Mat& I1, cv::Mat* flow) override;

 private:
  void InitializeFromSavedModel(const std::string& export_dir,
                                const std::string& tag);

  // Helper for running inference that resizes input/output images before/after
  // running inference.
  // Note: this function will perform some unnecessary allocation when running
  // the network multiple times.
  // input_size -- size that images should be resized to prior to sending to
  //               the network.
  // target_size -- size that output image should be resized to after being
  //                received from the network.
  // Both images must have type CV_32F, but of arbitrary size.
  // Output image will be CV_32FC2, and will be resized to target_size.
  void RunInference(const cv::Size& input_size, const cv::Size& target_size,
                    const cv::Mat& I0f, const cv::Mat& I1f, cv::Mat* output);

  OpticalFlowTensorFlowModelOptions opts_;

  std::unique_ptr<tensorflow::Session> session_;

  std::vector<std::string> input_names_;
  std::string output_name_;

  // Layout is height, width, number-of-channels.
  tensorflow::TensorShape input_shape_;
  tensorflow::TensorShape output_shape_;
};

}  // namespace flowthrone
