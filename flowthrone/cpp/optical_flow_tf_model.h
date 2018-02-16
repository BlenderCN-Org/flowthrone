#pragma once
#include "opencv2/core/core.hpp"
#include "tensorflow/core/public/session.h"
#include "optical_flow_model.h"
#include "flowthrone.pb.h"

namespace flowthrone {

namespace internal {

struct Context {
  std::vector<std::string> input_names;
  std::vector<std::string> output_names;
  // Layout is height, width, number-of-channels.
  tensorflow::TensorShape input_shape;
  tensorflow::TensorShape output_shape;
  // cv::Size analogues of the above.
  cv::Size input_size;
  cv::Size output_size;
  // Will be 'true' if there exists a 'is_training' tensor in the graph.
  // When this is the case, the network was trained with batch normalization,
  // and an additional tensor needs to be added to the tf::Session::Run(..)
  // call.
  bool need_is_training_placeholder = false;

  std::unique_ptr<tensorflow::Session> session;

  static std::unique_ptr<Context> Create(
      std::unique_ptr<tensorflow::Session> session,
      const tensorflow::GraphDef& graph_def,
      const OpticalFlowTensorFlowModelOptions& opts);
  ~Context();

  // Given two images (possibly different resolutions, and not necessarily
  // matching the input resolution of the network), runs inference and fills
  // in the result.
  // Input images must be of type CV_32F, and the output image will similarly
  // be CV_32F.
  void RunInference(const cv::Mat& I0f_in, const cv::Mat& I1f_in,
                    cv::Mat* flow);
};

}  // namespace internal

class OpticalFlowTensorFlowModel : public OpticalFlowModel {
 public:
  OpticalFlowTensorFlowModel(const OpticalFlowTensorFlowModelOptions& opt);
  virtual ~OpticalFlowTensorFlowModel();

  bool Run(const cv::Mat& I0, const cv::Mat& I1, cv::Mat* flow) override;

 private:
  void InitializeFromSavedModel(const std::string& export_dir,
                                const std::string& tag);

  OpticalFlowTensorFlowModelOptions opts_;

  std::unique_ptr<internal::Context> context_;
};

}  // namespace flowthrone
