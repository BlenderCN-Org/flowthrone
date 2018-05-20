#include "optical_flow_tf_model.h"

#include "flow_smoothing.h"
#include "opencv2/imgproc/imgproc.hpp"
#include "tensorflow/cc/saved_model/loader.h"
#include "tensorflow/core/public/session_options.h"
#include "tf_utils.h"
#include "utils.h"

namespace tf = tensorflow;

namespace flowthrone {
using internal::Context;
using Result = OpticalFlowModel::Result;

namespace {

// Converts a cv::Mat to float or returns its shallow copy.
cv::Mat MaybeConvertTo32F(const cv::Mat& x) {
  if (x.depth() == CV_32F) {
    return x;
  } else {
    cv::Mat y;
    x.convertTo(y, CV_32F);
    return y;
  }
}

const tf::NodeDef* GetTensorByName(const tf::GraphDef& graph,
                                   const std::string& name) {
  for (const auto& node : graph.node()) {
    if (node.name() == name) {
      return &node;
    }
  }
  return nullptr;
}

tf::DataType GetTensorDataType(const tf::GraphDef& graph_def,
                               const std::string& name) {
  const tf::NodeDef* node = GetTensorByName(graph_def, name);
  CHECK(node) << "Could not find tensor called '" << name << "'";
  CHECK(node->attr().count("dtype"));
  return node->attr().at("dtype").type();
}

tf::TensorShapeProto GetTensorShapeProto(const tf::GraphDef& graph_def,
                                         const std::string& name) {
  const std::string kShapeKey = "_output_shapes";
  const tf::NodeDef* node = GetTensorByName(graph_def, name);
  CHECK(node) << "Could not find tensor called '" << name << "'";
  CHECK(node->attr().count(kShapeKey));
  CHECK_GE(node->attr().at(kShapeKey).list().shape_size(), 1);
  return node->attr().at(kShapeKey).list().shape(0);
}

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

void CheckNumberOfChannels(const cv::Mat& x, int expected_channels) {
  CHECK_EQ(x.channels(), expected_channels)
      << "Number of channels in the provided image does not match the "
         "expected number of channels.";
}

std::pair<std::string, tf::Tensor> CreateIsTrainingPlaceholderPair() {
  tf::Tensor is_training(tf::DT_BOOL, tf::TensorShape({}));
  is_training.flat<bool>()(0) = false;
  return std::make_pair("is_training", std::move(is_training));
}

}  // namespace

OpticalFlowTensorFlowModel::OpticalFlowTensorFlowModel(
    const OpticalFlowTensorFlowModelOptions& opts)
    : opts_(opts) {
  const std::string kModelTag = "train";
  InitializeFromSavedModel(opts_.export_dir(), kModelTag);
}

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

Context::~Context() {
  if (session) {
    session->Close().IgnoreError();
  }
}

void Context::RunInference(const cv::Mat& I0_in, const cv::Mat& I1_in,
                           cv::Mat* flow) {
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
  CHECK_STATUS(session->Run(inputs_tf, {output_names[0]}, {}, &outputs_tf));
  CHECK_EQ(1, outputs_tf.size());
  const tf::Tensor& output_tf = outputs_tf[0];
  AsMat(output_tf, flow);
  *flow = ResampleFlow(*flow, original_input_output_size);
}

void OpticalFlowTensorFlowModel::InitializeFromSavedModel(
    const std::string& export_dir, const std::string& tag) {
  CHECK(tf::MaybeSavedModelDirectory(export_dir))
      << "Provided directory does not contain SavedModel? "
      << "Provided directory was: '" << export_dir << "'";

  tf::SavedModelBundle bundle;
  CHECK_STATUS(tf::LoadSavedModel(tf::SessionOptions(), tf::RunOptions(),
                                  export_dir, {tag}, &bundle));

  context_ = Context::Create(std::move(bundle.session),
                             bundle.meta_graph_def.graph_def(), opts_);
}

OpticalFlowTensorFlowModel::~OpticalFlowTensorFlowModel() {}

Result OpticalFlowTensorFlowModel::Run(const cv::Mat& I0_in,
                                       const cv::Mat& I1_in) {
  CheckNumberOfChannels(I0_in, context_->input_shape.dim_size(2));
  CheckNumberOfChannels(I1_in, context_->input_shape.dim_size(2));
  cv::Mat I0, I1;
  // Convert inputs to float if necessary. Newer models shall take in uint8
  // as inputs, but for backward compatibility float inputs are supported too.
  if (context_->inputs_are_uint8) {
    I0 = I0_in;
    I1 = I1_in;
  } else {
    I0 = MaybeConvertTo32F(I0_in);
    I1 = MaybeConvertTo32F(I1_in);
  }

  cv::Mat output_flow = cv::Mat(I0.size(), CV_32FC2, cv::Scalar(0.0f));
  if (!opts_.sliding_window()) {
    context_->RunInference(I0, I1, &output_flow);
  } else {
    // Doesn't __really__ need to be the case.
    cv::Size patch_sz = context_->input_size;

    int stride_x = patch_sz.width * opts_.window_stride();
    int stride_y = patch_sz.height * opts_.window_stride();
    std::vector<cv::Rect> patch_locations =
        SplitImage(I0.size(), patch_sz, cv::Size(stride_x, stride_y),
                   SplitImageMode::kSizeConstant);

    cv::Mat counts = cv::Mat(I0.size(), CV_32FC1, cv::Scalar(0));
    cv::Mat kernel = SquaredExponentialKernel(patch_sz);

    for (const auto& rect : patch_locations) {
      // At the boundaries, rect.size() != patch_sz, so the patch (and the
      // kernel) may need to be resized even if patch_sz == network input size.
      cv::Mat I0_patch = I0(rect);
      cv::Mat I1_patch = I1(rect);
      cv::Mat flow_patch;
      context_->RunInference(I0_patch, I1_patch, &flow_patch);

      cv::Mat this_kernel;
      cv::resize(kernel, this_kernel, rect.size());
      cv::Mat kernel_32fc2;
      cv::merge(std::vector<cv::Mat>{this_kernel, this_kernel}, kernel_32fc2);
      cv::multiply(flow_patch, kernel_32fc2, flow_patch);
      cv::add(output_flow(rect), flow_patch, output_flow(rect));
      cv::add(counts(rect), this_kernel, counts(rect));
    }
    cv::Mat counts_32fc2;
    cv::merge(std::vector<cv::Mat>{counts, counts}, counts_32fc2);
    output_flow = output_flow / counts_32fc2;
  }

  Postprocess(I0_in, I1_in, &output_flow);
  Result result;
  result.flow = std::move(output_flow);
  return result;
}

void OpticalFlowTensorFlowModel::Postprocess(const cv::Mat& I0_in,
                                             const cv::Mat& I1_in,
                                             cv::Mat* flow) {
  if (opts_.has_denoising_options()) {
    DenoisingOptions dn_opts;
    dn_opts.sigma_intensity = opts_.denoising_options().sigma_intensity();
    dn_opts.sigma_distance = opts_.denoising_options().sigma_distance();
    dn_opts.window_size = opts_.denoising_options().window_size();
    *flow = DenoiseColorWeightedFilter(*flow, I0_in, dn_opts);
  }
}

}  // namespace flowthrone
