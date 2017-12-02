#include "optical_flow_tf_model.h"

#include "tf_utils.h"
#include "opencv2/imgproc/imgproc.hpp"
#include "tensorflow/cc/saved_model/loader.h"
#include "tensorflow/core/public/session_options.h"

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

const tf::NodeDef* GetTensorByName(const tf::GraphDef& graph, const std::string& name) {
  for (const auto& node : graph.node()) {
    if (node.name() == name) {
      return &node;
    }
  }
  return nullptr; 
}

tf::TensorShapeProto GetTensorShapeProto(
      const tf::GraphDef& graph_def, const std::string& name) {
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
  return tf::TensorShape({x.dim(1).size(),
                          x.dim(2).size(),
                          x.dim(3).size()}); 
}

tf::TensorShape GetInputTensorShape(const tf::GraphDef& graph_def,
                    const std::string& in1_name,
                    const std::string& in2_name) {
  tf::TensorShapeProto x1_shape = GetTensorShapeProto(graph_def, in1_name);
  tf::TensorShapeProto x2_shape = GetTensorShapeProto(graph_def, in2_name);
  CHECK_EQ(x1_shape.SerializeAsString(), x2_shape.SerializeAsString())
    << "Shapes of the two tensors do not match as expected. Maybe tensor "
    << "names do not correspond to the two input images? Names were: "
    << in1_name << ", " << in2_name << " and shapes were: " 
    << x1_shape.DebugString() << "\n and \n" << x2_shape.DebugString();
  return GetTensorShape(x1_shape);
}

void CheckNumberOfChannels(const cv::Mat& x, int expected_channels) {
  CHECK_EQ(x.channels(), expected_channels) 
      << "Number of channels in the provided image does not match the "
         "expected number of channels.";
}

} // namespace


OpticalFlowTensorFlowModel::OpticalFlowTensorFlowModel(const std::string& export_dir) {
  InitializeFromSavedModel(export_dir, "train");
}

OpticalFlowTensorFlowModel::~OpticalFlowTensorFlowModel() {
  if (session_) {
    session_->Close().IgnoreError();
  }
}

void OpticalFlowTensorFlowModel::InitializeFromSavedModel(
                      const std::string& export_dir, const std::string& tag) {
  CHECK(tf::MaybeSavedModelDirectory(export_dir)) 
      << "Provided directory does not contain SavedModel?";
  
  tf::SavedModelBundle bundle;                                                  
  CHECK_STATUS(tf::LoadSavedModel(                                              
        tf::SessionOptions(), tf::RunOptions(), export_dir, {tag}, &bundle));
  session_ = std::move(bundle.session);  
  
  const tf::GraphDef& graph_def = bundle.meta_graph_def.graph_def();
  input_shape_ = GetInputTensorShape(graph_def, "x1", "x2");
  output_shape_ = GetTensorShape(GetTensorShapeProto(graph_def, "prediction"));

  input_names_ = std::vector<std::string>{"x1", "x2"};
  output_name_ = "prediction";
}

bool OpticalFlowTensorFlowModel::Run(const cv::Mat& I0, const cv::Mat& I1, cv::Mat& flow) {
  CheckNumberOfChannels(I0, input_shape_.dim_size(2));
  CheckNumberOfChannels(I1, input_shape_.dim_size(2));
  cv::Mat I0f = MaybeConvertTo32F(I0);
  cv::Mat I1f = MaybeConvertTo32F(I1);
  cv::Size sz(input_shape_.dim_size(0), input_shape_.dim_size(1));
  cv::resize(I0f, I0f, sz);
  cv::resize(I1f, I1f, sz);

  std::vector<std::pair<std::string, tf::Tensor>> inputs;                       
  inputs.push_back(std::make_pair(input_names_[0], AsTensor(I0f)));                                   
  inputs.push_back(std::make_pair(input_names_[1], AsTensor(I1f)));

  std::vector<tf::Tensor> outputs;                                              
  CHECK_STATUS(session_->Run(inputs, {output_name_}, {}, &outputs));
  CHECK_EQ(1, outputs.size());                                                  
  const tf::Tensor& output = outputs[0];
  flow = AsMat(output);
  return true;
}

} // namespace flowthrone
