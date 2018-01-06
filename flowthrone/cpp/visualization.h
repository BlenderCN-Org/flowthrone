// Utilities for visualization.
#pragma once
#include <opencv2/core/core.hpp>

namespace flowthrone {

// Given a flow (CV_32FC2), colors it according to the standard visualization
// scheme and returns a CV_8UC3 image.
cv::Mat ComputeFlowColor(const cv::Mat& flow);

// Horizontally concatenates two images. Makes a deep copy of the image data.
// This is equivalent to cv::hconcat(std::vector<cv::Mat>{x, y}, output);
cv::Mat HorizontalConcat(const cv::Mat& x, const cv::Mat& y);
cv::Mat HorizontalConcat(const cv::Mat& i0, const cv::Mat& i1,
                         const cv::Mat& i2);
// Vertically concatentates two images. Makes a deep copy of the image data.
// This is a shorthand for cv::vconcat(std::vector<cv::Mat>{x, y}, output);
cv::Mat VerticalConcat(const cv::Mat& x, const cv::Mat& y);

// Returns an horizontally concatenated image used for visualization:
// blended pair of images on the left and the colorized optical flow field on
// the right.
cv::Mat VisualizeTuple(const cv::Mat& I0, const cv::Mat& I1,
                       const cv::Mat& flow);
cv::Mat VisualizeTuple(const cv::Mat& I0, const cv::Mat& I1,
                       const cv::Mat& flow, const cv::Mat& flow_gt);

}  // namespace flowthrone
