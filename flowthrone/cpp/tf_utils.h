#pragma once
#include "opencv2/core/core.hpp"
#include "tensorflow/core/framework/tensor.h"

namespace flowthrone {

// TODO(vasiliy): more documentation.
//
// Converts a cv::Mat to a tensor. 
// cv::Mat must have depth 32F. TODO(vasiliy): fix.
tensorflow::Tensor AsTensor(const cv::Mat& x);
// Converts a tensor to a cv::Mat.
// The provided tensor must have 4 dimensions.
// The first dimension (batch size) must be 1. Number of channels is limited
// by opencv.
cv::Mat AsMat(const tensorflow::Tensor& x);

void CHECK_STATUS(const tensorflow::Status& s);

} // namespace flowthrone
