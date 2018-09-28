#include "optical_flow_tf_internal.h"

#include "opencv2/imgproc/imgproc.hpp"
#include "tensorflow/cc/saved_model/loader.h"
#include "tensorflow/core/public/session_options.h"
#include "tf_utils.h"
#include "utils.h"

namespace tf = tensorflow;

namespace flowthrone {
namespace internal {

namespace {

tf::TensorShape GetTensorShape(const tf::TensorShapeProto& x) {
  CHECK_EQ(4, x.dim_size());
  CHECK_EQ(-1, x.dim(0).size())
      << "Expected the first dimension to be unspecified (number of examples).";
  return tf::TensorShape({x.dim(1).size(), x.dim(2).size(), x.dim(3).size()});
}

tf::TensorShape GetInputTensorShape(const tf::GraphDef& graph_def,
                                    const std::string& in1_name,
                                    const std::string& in2_name) {
  tf::TensorShapeProto x1_shape = GetTensorShapeProto(graph_def, in1_name);
  tf::TensorShapeProto x2_shape = GetTensorShapeProto(graph_def, in2_name);

  CHECK_EQ(x1_shape.SerializeAsString(), x2_shape.SerializeAsString())
      << "Shapes of the two tensors do not match as expected. Maybe tensor "
      << "names do not correspond to the two input images? Names were: "
      << in1_name << ", " << in2_name
      << " and shapes were: " << x1_shape.DebugString() << "\n and \n"
      << x2_shape.DebugString();
  return GetTensorShape(x1_shape);
}

std::pair<std::string, tf::Tensor> CreateIsTrainingPlaceholderPair() {
  tf::Tensor is_training(tf::DT_BOOL, tf::TensorShape({}));
  is_training.flat<bool>()(0) = false;
  return std::make_pair("is_training", std::move(is_training));
}

}  // namespace

std::unique_ptr<Context> Context::Create(
    std::unique_ptr<tensorflow::Session> session, const tf::GraphDef& graph_def,
    const OpticalFlowTensorFlowModelOptions& opts) {
  std::unique_ptr<Context> context(new Context);
  CHECK_EQ(2, opts.input_tensor_name_size())
      << "You must specify exactly two input tensors in your options. Probably "
         "these should be the names of the two input images to the network. ";
  context->input_names = std::vector<std::string>(
      opts.input_tensor_name().begin(), opts.input_tensor_name().end());
  CHECK_EQ(1, opts.output_tensor_name_size())
      << "You must specify exactly one output tensor in your options. Probably "
         "this should be the output flow prediction tensor.";
  context->output_names = std::vector<std::string>(
      opts.output_tensor_name().begin(), opts.output_tensor_name().end());

  context->input_shape = GetInputTensorShape(graph_def, context->input_names[0],
                                             context->input_names[1]);
  context->output_shape =
      GetTensorShape(GetTensorShapeProto(graph_def, context->output_names[0]));
  // TODO: cv::Size(width, height). Is input_shape.dim_size() the same?
  context->input_size = cv::Size(context->input_shape.dim_size(0),
                                 context->input_shape.dim_size(1));
  context->output_size = cv::Size(context->output_shape.dim_size(0),
                                  context->output_shape.dim_size(1));
  context->need_is_training_placeholder =
      static_cast<bool>(GetTensorByName(graph_def, "is_training"));

  {  // Verify that both inputs are of the same type and set expected type.
    auto x1_type = GetTensorDataType(graph_def, context->input_names[0]);
    auto x2_type = GetTensorDataType(graph_def, context->input_names[1]);
    CHECK_EQ(x1_type, x2_type) << "Inputs do not have the same data type?";
    context->inputs_are_uint8 = (x1_type == tf::DT_UINT8);
  }

  context->session = std::move(session);
  return std::move(context);
}

void Context::RunInference(const cv::Mat& I0_in, const cv::Mat& I1_in,
                           std::vector<cv::Mat>* outputs) {
  // Size of the input fed into this function.
  // This will be used to resize the output.
  cv::Size original_input_output_size = I0_in.size();

  std::vector<std::pair<std::string, tf::Tensor>> inputs_tf;
  inputs_tf.push_back(std::make_pair(input_names[0], tf::Tensor()));
  inputs_tf.push_back(std::make_pair(input_names[1], tf::Tensor()));
  if (need_is_training_placeholder) {
    inputs_tf.push_back(CreateIsTrainingPlaceholderPair());
  }

  std::vector<tf::Tensor> outputs_tf;

  cv::Mat I0, I1;
  cv::resize(I0_in, I0, input_size);
  cv::resize(I1_in, I1, input_size);
  AsTensor(I0, &inputs_tf[0].second);
  AsTensor(I1, &inputs_tf[1].second);
  CHECK_STATUS(session->Run(inputs_tf, output_names, {}, &outputs_tf));
  CHECK_EQ(output_names.size(), outputs_tf.size());

  outputs->resize(output_names.size());
  for (size_t i = 0; i < output_names.size(); ++i) {
    const tf::Tensor& output_tf = outputs_tf[i];
    cv::Mat& output_mat = outputs->at(i);
    AsMat(output_tf, &output_mat);
    output_mat = ResampleFlow(output_mat, original_input_output_size);
  }
}

Context::~Context() {
  if (session) {
    session->Close().IgnoreError();
  }
}

tf::SessionOptions CreateSessionOptions() {
  tf::SessionOptions session_opts;
  tf::GPUOptions* gpu_opts = session_opts.config.mutable_gpu_options();
  gpu_opts->set_allow_growth(true);
  return session_opts;
}

std::unique_ptr<Context> Context::CreateFromSavedModel(
    const OpticalFlowTensorFlowModelOptions& opts,
    const std::string& export_dir, const std::string& tag) {
  CHECK(tf::MaybeSavedModelDirectory(export_dir))
      << "Provided directory does not contain SavedModel? "
      << "Provided directory was: '" << opts.export_dir() << "'";

  tf::SavedModelBundle bundle;
  tf::SessionOptions session_opts = CreateSessionOptions();
  CHECK_STATUS(tf::LoadSavedModel(session_opts, tf::RunOptions(), export_dir,
                                  {tag}, &bundle));

  return Context::Create(std::move(bundle.session),
                         bundle.meta_graph_def.graph_def(), opts);
}

std::unique_ptr<Context> Context::CreateFromFrozenGraph(
    const OpticalFlowTensorFlowModelOptions& opts,
    const std::string& frozen_graph_filename) {
  tf::SessionOptions session_opts = CreateSessionOptions();
  std::unique_ptr<tf::Session> session(tf::NewSession(session_opts));
  CHECK(static_cast<bool>(session));

  tf::GraphDef graph_def;
  CHECK_STATUS(tf::ReadBinaryProto(tf::Env::Default(), frozen_graph_filename,
                                   &graph_def));
  CHECK_STATUS(session->Create(graph_def));
  return Context::Create(std::move(session), graph_def, opts);
}

}  // namespace internal

}  // namespace flowthrone
