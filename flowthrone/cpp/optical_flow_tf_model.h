#pragma once
#include "opencv2/core/core.hpp"
#include "tensorflow/core/public/session.h"

namespace flowthrone {

class OpticalFlowTensorFlowModel {
 public:
  // TODO(vasiliy): fix
  OpticalFlowTensorFlowModel(const std::string& export_dir);
  ~OpticalFlowTensorFlowModel();

  bool Run(const cv::Mat& I0, const cv::Mat& I1, cv::Mat& flow);

 private:
  // TODO: error handling.
  void InitializeFromSavedModel(const std::string& export_dir,
                                const std::string& tag);

  std::unique_ptr<tensorflow::Session> session_;

  std::vector<std::string> input_names_;
  std::string output_name_;

  tensorflow::TensorShape input_shape_;
  tensorflow::TensorShape output_shape_;
};

}  // namespace flowthrone
