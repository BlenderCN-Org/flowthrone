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

}  // namespace flowthrone
