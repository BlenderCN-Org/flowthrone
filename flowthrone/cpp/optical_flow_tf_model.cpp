#include "optical_flow_tf_model.h"

#include "tf_utils.h"
#include "utils.h"
#include "opencv2/imgproc/imgproc.hpp"
#include "tensorflow/cc/saved_model/loader.h"
#include "tensorflow/core/public/session_options.h"

#include "opencv2/highgui/highgui.hpp"

namespace tf = tensorflow;

namespace flowthrone {

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

tf::TensorShapeProto GetTensorShapeProto(const tf::GraphDef& graph_def,
                                         const std::string& name) {
  const std::string kShapeKey = "_output_shapes";
  const tf::NodeDef* node = CHECK_NOTNULL(GetTensorByName(graph_def, name));
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

// Returns a matrix whose value is 1 at the center, and decreases to zero
// at the boundaries.
cv::Mat TriangleKernel(cv::Size size) {
  int xc = size.width / 2;
  int yc = size.height / 2;
  cv::Mat tri(size, CV_32FC1);
  for (int y = 0; y < tri.rows; ++y) {
    float* row = reinterpret_cast<float*>(tri.row(y).data);
    float wy = 1.0 - std::abs(y - yc) / float(yc);
    for (int x = 0; x < tri.cols; ++x) {
      float wx = 1.0 - std::abs(x - xc) / float(xc);
      row[x] = wx * wy;
    }
  }
  return tri;
}

}  // namespace
using Options = OpticalFlowTensorFlowModel::Options;

OpticalFlowTensorFlowModel::OpticalFlowTensorFlowModel(const Options& opts)
    : opts_(opts) {
  const std::string kModelTag = "train";
  InitializeFromSavedModel(opts.export_dir, kModelTag);
}

OpticalFlowTensorFlowModel::~OpticalFlowTensorFlowModel() {
  if (session_) {
    session_->Close().IgnoreError();
  }
}

void OpticalFlowTensorFlowModel::InitializeFromSavedModel(
    const std::string& export_dir, const std::string& tag) {
  CHECK(tf::MaybeSavedModelDirectory(export_dir))
      << "Provided directory does not contain SavedModel? "
      << "Provided directory was: '" << export_dir << "'";

  tf::SavedModelBundle bundle;
  CHECK_STATUS(tf::LoadSavedModel(tf::SessionOptions(), tf::RunOptions(),
                                  export_dir, {tag}, &bundle));
  session_ = std::move(bundle.session);

  // These must match names that are specified at training time.
  input_names_ = std::vector<std::string>{"x1", "x2"};
  output_name_ = "prediction";

  const tf::GraphDef& graph_def = bundle.meta_graph_def.graph_def();
  input_shape_ =
      GetInputTensorShape(graph_def, input_names_[0], input_names_[1]);
  output_shape_ = GetTensorShape(GetTensorShapeProto(graph_def, output_name_));
}

bool OpticalFlowTensorFlowModel::Run(const cv::Mat& I0, const cv::Mat& I1,
                                     cv::Mat& flow) {
  CheckNumberOfChannels(I0, input_shape_.dim_size(2));
  CheckNumberOfChannels(I1, input_shape_.dim_size(2));
  cv::Mat I0f = MaybeConvertTo32F(I0);
  cv::Mat I1f = MaybeConvertTo32F(I1);

  std::vector<std::pair<std::string, tf::Tensor>> inputs;
  inputs.push_back(std::make_pair(input_names_[0], tf::Tensor()));
  inputs.push_back(std::make_pair(input_names_[1], tf::Tensor()));
  std::vector<tf::Tensor> outputs;

  if (!opts_.sliding_window) {
    cv::Size sz(input_shape_.dim_size(0), input_shape_.dim_size(1));
    cv::resize(I0f, I0f, sz);
    cv::resize(I1f, I1f, sz);
    AsTensor(I0f, &inputs[0].second);
    AsTensor(I1f, &inputs[1].second);

    CHECK_STATUS(session_->Run(inputs, {output_name_}, {}, &outputs));
    CHECK_EQ(1, outputs.size());
    const tf::Tensor& output = outputs[0];
    AsMat(output, &flow);
    cv::resize(flow, flow, I0.size());
  } else {
    cv::Size patch_sz(input_shape_.dim_size(0), input_shape_.dim_size(1));
    int stride_x = patch_sz.width * opts_.stride_fraction;
    int stride_y = patch_sz.height * opts_.stride_fraction;
    std::vector<cv::Rect> patch_locations =
        SplitImage(I0.size(), patch_sz, cv::Size(stride_x, stride_y),
                   SplitImageMode::kStrideConstant);
    flow = cv::Mat(I0.size(), CV_32FC2, cv::Scalar(0.0f));
    cv::Mat counts = cv::Mat(I0.size(), CV_32FC1, cv::Scalar(0));

    cv::Mat kernel = TriangleKernel(cv::Size(64, 64));
    for (const auto& rect : patch_locations) {
      cv::Mat I0f_patch = I0f(rect);
      cv::Mat I1f_patch = I1f(rect);
      cv::resize(I0f_patch, I0f_patch, cv::Size(64, 64));
      cv::resize(I1f_patch, I1f_patch, cv::Size(64, 64));

      AsTensor(I0f_patch, &inputs[0].second);
      AsTensor(I1f_patch, &inputs[1].second);

      CHECK_STATUS(session_->Run(inputs, {output_name_}, {}, &outputs));
      CHECK_EQ(1, outputs.size());
      const tf::Tensor& output = outputs[0];
      cv::Mat flow_patch;
      AsMat(output, &flow_patch);
      cv::resize(flow_patch, flow_patch, rect.size());
      cv::Mat this_kernel;
      cv::resize(kernel, this_kernel, rect.size());
      cv::Mat kernel_32fc2;
      cv::merge(std::vector<cv::Mat>{this_kernel, this_kernel}, kernel_32fc2);
      cv::multiply(flow_patch, kernel_32fc2, flow_patch);
      cv::add(flow(rect), flow_patch, flow(rect));
      cv::add(counts(rect), this_kernel, counts(rect));
    }
    cv::Mat counts_32fc2;
    // counts.convertTo(counts, CV_32F);
    cv::merge(std::vector<cv::Mat>{counts, counts}, counts_32fc2);
    flow = flow / counts_32fc2;
  }
  return true;
}

}  // namespace flowthrone
