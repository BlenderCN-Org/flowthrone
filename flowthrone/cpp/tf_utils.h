#pragma once
#include "opencv2/core/core.hpp"
#include "tensorflow/core/framework/tensor.h"

namespace flowthrone {

// Converts a collection of cv::Mat's to a tensor. All images must have the
// same size and the same number of channels.
// Moreover, all images must be of type CV_32F and the returned tensor will
// have type DT_FLOAT.
void AsTensor(const std::vector<cv::Mat>& x, tensorflow::Tensor* tensor);
void AsTensor(const cv::Mat& x, tensorflow::Tensor* tensor);

// Converts a tensor to a collection of cv::Mat's.
// Tensor must have 4 dimensions (even if there is a single instance, and even
// if the number of channels is 1).
void AsMat(const tensorflow::Tensor& tensor, std::vector<cv::Mat>* x);
// Converts a tensor to a single cv::Mat. The first dimension of the tensor
// must be 1.
void AsMat(const tensorflow::Tensor& tensor, cv::Mat* x);

// CHECK the status and print an error if it is invalid.
void CHECK_STATUS(const tensorflow::Status& s);

}  // namespace flowthrone
