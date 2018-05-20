#pragma once
#include "flowthrone.pb.h"
#include "opencv2/core/core.hpp"
#include "optical_flow_model.h"
#include "tensorflow/core/public/session.h"

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

  // Whether inputs are of type uint8_t or float.
  bool inputs_are_uint8 = false;

  std::unique_ptr<tensorflow::Session> session;

  static std::unique_ptr<Context> Create(
      std::unique_ptr<tensorflow::Session> session,
      const tensorflow::GraphDef& graph_def,
      const OpticalFlowTensorFlowModelOptions& opts);
  ~Context();

  // Given two images (possibly different resolutions, and not necessarily
  // matching the input resolution of the network), runs inference and fills
  // in the result.
  // Output image will be CV_32FC2.
  void RunInference(const cv::Mat& I0_in, const cv::Mat& I1_in, cv::Mat* flow);
};

}  // namespace internal

class OpticalFlowTensorFlowModel : public OpticalFlowModel {
 public:
  OpticalFlowTensorFlowModel(const OpticalFlowTensorFlowModelOptions& opt);
  virtual ~OpticalFlowTensorFlowModel();

  Result Run(const cv::Mat& I0, const cv::Mat& I1) override;

 private:
  void InitializeFromSavedModel(const std::string& export_dir,
                                const std::string& tag);

  void Postprocess(const cv::Mat& I0, const cv::Mat& I1, cv::Mat* flow);
  OpticalFlowTensorFlowModelOptions opts_;

  std::unique_ptr<internal::Context> context_;
};

}  // namespace flowthrone
