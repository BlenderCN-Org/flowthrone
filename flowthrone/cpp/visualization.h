// Utilities for visualization.
#pragma once
#include <opencv2/core/core.hpp>

namespace flowthrone {

// Given a flow (CV_32FC2), colors it according to the standard visualization
// scheme and returns a CV_8UC3 image.
// As is common, visualizationn uses largest flow magnitude to decide on color
// 'intensities'. This is reassonable for frame-by-frame visuals, but in other
// cases (e.g. we are processing a video, and one pair of frames has very
// little motion) this results in bad looking results.
// The optional argument adjusts the normalization as
//   uv_max_magnitude = max( max(flow), least_max_flow_mag);
cv::Mat ComputeFlowColor(const cv::Mat& flow, float least_max_flow_mag = 0.0f);

// Horizontally concatenates two images. Makes a deep copy of the image data.
// This is equivalent to cv::hconcat(std::vector<cv::Mat>{x, y}, output);
cv::Mat HorizontalConcat(const cv::Mat& x, const cv::Mat& y);
cv::Mat HorizontalConcat(const cv::Mat& i0, const cv::Mat& i1,
                         const cv::Mat& i2);
// Vertically concatentates two images. Makes a deep copy of the image data.
// This is a shorthand for cv::vconcat(std::vector<cv::Mat>{x, y}, output);
cv::Mat VerticalConcat(const cv::Mat& x, const cv::Mat& y);

// Options for visualizing a 'tuple' of images.
struct VisTupleOptions {
  // Describes how images should be displayed.
  enum ImageVisualizationPlan {
    // Only show first image.
    SHOW_IMAGE0 = 0,
    // Only show second image.
    SHOW_IMAGE1 = 1,
    // Show blended images.
    SHOW_BLENDED = 2,
  };
  float least_max_flow_mag = 0.0f;
  ImageVisualizationPlan image_vis = SHOW_BLENDED;
};

// Returns an horizontally concatenated image used for visualization:
// blended pair of images on the left and the colorized optical flow field on
// the right.
cv::Mat VisualizeTuple(const cv::Mat& I0, const cv::Mat& I1,
                       const cv::Mat& flow,
                       const VisTupleOptions& opts = VisTupleOptions{});
cv::Mat VisualizeTuple(const cv::Mat& I0, const cv::Mat& I1,
                       const cv::Mat& flow, const cv::Mat& flow_gt,
                       const VisTupleOptions& opts = VisTupleOptions{});

// Given a pair of images and flow, overlays a grid of points on each image
// that displays the correspondence.
// A regular grid is overlaid on I1, and the grid on I0 is warped by the flow.
std::pair<cv::Mat, cv::Mat> OverlayWarpedPoints(
    const cv::Mat& I0, const cv::Mat& I1, const cv::Mat& flow,
    int point_spacing = 10, int point_radius = 2, int point_thickness = 2);

}  // namespace flowthrone
