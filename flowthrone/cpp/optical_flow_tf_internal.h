#pragma once
#include "flowthrone.pb.h"
#include "opencv2/core/core.hpp"
#include "tensorflow/core/public/session.h"

namespace flowthrone {
namespace internal {

// Object used to run network inference.
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

  // Factory method for creating the context object.
  static std::unique_ptr<Context> Create(
      std::unique_ptr<tensorflow::Session> session,
      const tensorflow::GraphDef& graph_def,
      const OpticalFlowTensorFlowModelOptions& opts);

  // Creates and returns a Context object from a directory containing a
  // SavedModel.
  static std::unique_ptr<Context> CreateFromSavedModel(
      const OpticalFlowTensorFlowModelOptions& opts,
      const std::string& export_dir, const std::string& tag);

  ~Context();

  // Given two images (possibly different resolutions, and not necessarily
  // matching the input resolution of the network), runs inference and fills
  // in the result.
  // Inputs may be CV_8UC3 or CV_32FC3. Output image(s) will be CV_32FC2.
  void RunInference(const cv::Mat& I0_in, const cv::Mat& I1_in,
                    std::vector<cv::Mat>* outputs);
};

}  // namespace internal
}  // namespace flowthrone
