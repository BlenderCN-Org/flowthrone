#pragma once
#include "opencv2/core/core.hpp"
#include "tensorflow/core/framework/tensor.h"
// Note: this include probably has more than we need here.
#include "tensorflow/cc/saved_model/loader.h"

namespace flowthrone {

// Converts a collection of cv::Mat's to a tensor. All images must have the
// same size and the same number of channels.
// Moreover, all images must be of types {CV_8U, CV_32F} and the returned tensor
// will have type {DT_UINT8, DT_FLOAT}.
void AsTensor(const std::vector<cv::Mat>& x, tensorflow::Tensor* tensor);
void AsTensor(const cv::Mat& x, tensorflow::Tensor* tensor);

// Converts a tensor to a collection of cv::Mat's.
// Tensor must have 4 dimensions (even if there is a single instance, and even
// if the number of channels is 1).
void AsMat(const tensorflow::Tensor& tensor, std::vector<cv::Mat>* x);
// Converts a tensor to a single cv::Mat. The first dimension of the tensor
// must be 1.
void AsMat(const tensorflow::Tensor& tensor, cv::Mat* x);

// Returns a tensor from the graph. If the tensor is not found, returns a
// nullptr.
const tensorflow::NodeDef* GetTensorByName(const tensorflow::GraphDef& graph,
                                           const std::string& name);

// Returns a DataType for a given tensor. Will CHECK-fail if tensor is not
// present in the graph.
tensorflow::DataType GetTensorDataType(const tensorflow::GraphDef& graph_def,
                                       const std::string& name);

// Returns a TensorShapeProto for a given tensor. Will CHECK-fail if tensor is
// not present in the graph.
tensorflow::TensorShapeProto GetTensorShapeProto(
    const tensorflow::GraphDef& graph_def, const std::string& name);

}  // namespace flowthrone
