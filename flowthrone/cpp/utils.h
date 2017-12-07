#pragma once
#include <vector>
#include <opencv2/core/core.hpp>

namespace flowthrone {

// Splits optical flow CV_32FC2 (w_x(p), w_y(p)) into a pair of CV_32FC1,
// whose elements are I_1(p) = p + w_x(p) I_2(p) = p + w_y(p).
// These maps can subsequently be used to call cv::remap directly.
std::vector<cv::Mat> GetFlowMaps(const cv::Mat& flow);

// Warps image with optical flow (flow(p) = w_x(p), w_y(p)).
// NOTE: If you need to apply the same flow to multiple images, it will be
// faster to call GetFlowMaps first, and then call remap multiple times
// (with the same flow).
cv::Mat WarpWithFlow(const cv::Mat& I, const cv::Mat& flow);

// Resizes the flow field and appropriately scales the flow values.
// Effectively does:
//   cv::resize(input, output, target_size) * target_size / input.size()
cv::Mat ResampleFlow(const cv::Mat& flow, const cv::Size& target_size);

// When splitting the image, whether to enforce that the stride size should
// be constant, or whether the patch size should be constant.
// Consider splitting a 20x15 image into 15x15 patches. If stride is kept
// constant, then the output will be:
//   cv::Rect(0, 0, 15, 15), cv::Rect(15, 0, 5, 5)
// Otherwise, if the size is kept constant, then it will be:
//   cv::Rect(0, 0, 15, 15), cv::Rect(5, 0, 15, 15).
enum class SplitImageMode {
  kSizeConstant = 0,
  kStrideConstant = 1,
};
// Given image dimensions, patch dimensions, and stride, returns a collection
// of cv::Rect's that tile the image (possibly with overlap).
std::vector<cv::Rect> SplitImage(
    cv::Size image_sz, cv::Size patch_sz, cv::Size stride,
    SplitImageMode mode = SplitImageMode::kSizeConstant);

}  // namespace flowthrone
