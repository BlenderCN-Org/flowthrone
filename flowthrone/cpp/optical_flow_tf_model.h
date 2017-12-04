#pragma once
#include "opencv2/core/core.hpp"
#include "tensorflow/core/public/session.h"

namespace flowthrone {

class OpticalFlowTensorFlowModel {
 public:
  struct Options {
    std::string export_dir;
    bool sliding_window = true;
    double stride_fraction = 0.5;
  };

  OpticalFlowTensorFlowModel(const Options& opt);
  ~OpticalFlowTensorFlowModel();

  bool Run(const cv::Mat& I0, const cv::Mat& I1, cv::Mat& flow);

 private:
  void InitializeFromSavedModel(const std::string& export_dir,
                                const std::string& tag);

  Options opts_;

  std::unique_ptr<tensorflow::Session> session_;

  std::vector<std::string> input_names_;
  std::string output_name_;

  // Layout is height, width, number-of-channels.
  tensorflow::TensorShape input_shape_;
  tensorflow::TensorShape output_shape_;
};

}  // namespace flowthrone
