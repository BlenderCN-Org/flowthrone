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

// Warps a collection of discrete points with optical flow. This function
// performs the analogue of the above, but for discrete points. Hence, each
// output point i is given by:
//   (x_out, y_out) = (x_in - flow(x_in, y_in, 0), y_in - flow(x_in, y_in, 1))
// NOTE: points *outside* of the flow image boundaries are assigned the nearest
// flow value (this amounts to extending the flow field boundary values
// indefinitely in each direction).
std::vector<std::pair<float, float>> WarpWithFlow(
    const std::vector<std::pair<float, float>>& points, const cv::Mat& flow);

// Resizes the flow field and appropriately scales the flow values.
// Effectively does:
//   cv::resize(input, output, target_size) * target_size / input.size()
cv::Mat ResampleFlow(const cv::Mat& flow, const cv::Size& target_size);

// Computes the warp error I0(x) - I1(warp(x)).
cv::Mat ComputeResidual(const cv::Mat& I0, const cv::Mat& I1,
                        const cv::Mat& flow);

// Returns magnitude of optical flow (i.e. each element is ||w(x)||).
cv::Mat FlowMagnitude(const cv::Mat& flow);

// Like MATLAB's linspace -- returns a vector of values equally spaced
// between min and max (inclusively).
std::vector<float> Linspace(float min, float max, int num);

// Returns a grid of (x, y) values. The grid is laid out row-by-row
// (i.e. x coordinate is changing the fastest).
std::vector<std::pair<float, float>> Meshgrid(const std::vector<float>& x,
                                              const std::vector<float>& y);

// Returns a matrix whose value is 1 at the center, and whose values decrease
// (bilinearly) to zero at the boundaries.
cv::Mat TriangleKernel(cv::Size size);

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
