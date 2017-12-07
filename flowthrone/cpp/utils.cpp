#include "utils.h"
#include <glog/logging.h>
#include <opencv2/imgproc/imgproc.hpp>

namespace flowthrone {

std::vector<cv::Mat> GetFlowMaps(const cv::Mat& flow) {
  std::vector<cv::Mat> flow_maps;
  cv::split(flow, flow_maps);
  // Compute x' = x + w(x,y), y' = y + w(x,y)
  for (int r = 0; r < flow.rows; ++r) {
    flow_maps[1].row(r) += r;
    float* data = flow_maps[0].ptr<float>(r);
    for (int c = 0; c < flow.cols; ++c) {
      data[c] += c;
    }
  }
  return flow_maps;
}

cv::Mat WarpWithFlow(const cv::Mat& I, const cv::Mat& flow) {
  CHECK_EQ(CV_32FC2, flow.type()) << "Incorrect cv::Mat format for flow";
  std::vector<cv::Mat> flow_maps = GetFlowMaps(flow);
  cv::Mat I_warped;
  cv::remap(I, I_warped, flow_maps[0], flow_maps[1], cv::INTER_LINEAR);
  return I_warped;
}

cv::Mat ResampleFlow(const cv::Mat& flow, const cv::Size& target_size) {
  CHECK_EQ(2, flow.channels());
  cv::Mat flow_out;
  cv::resize(flow, flow_out, target_size);
  std::vector<cv::Mat> flow_fields;
  cv::split(flow_out, flow_fields);
  CHECK_EQ(2, flow_fields.size());
  flow_fields[0] *= static_cast<float>(flow.cols) / target_size.width;
  flow_fields[1] *= static_cast<float>(flow.rows) / target_size.height;
  cv::merge(flow_fields, flow_out);
  return flow_out;
}

std::vector<cv::Rect> SplitImage(cv::Size image_sz, cv::Size patch_sz,
                                 cv::Size stride, SplitImageMode mode) {
  CHECK(stride.width >= 1 && stride.height >= 1) << "Stride must be positive.";
  CHECK(image_sz.width >= patch_sz.width && image_sz.height >= patch_sz.height)
      << "Currently only support tiling of images that are at least as large "
         "as "
         "the patch size.";
  CHECK(patch_sz.width >= stride.width && patch_sz.height >= stride.height)
      << "Patch must be larger than stride. In other words, it is only "
         "possible "
         "to densely tile the image.";

  std::vector<std::pair<int, int>> y_offset_and_sz{{0, patch_sz.height}};
  std::vector<std::pair<int, int>> x_offset_and_sz{{0, patch_sz.width}};

  if (mode == SplitImageMode::kSizeConstant) {
    int last_y_offset = image_sz.height - patch_sz.height;
    while (y_offset_and_sz.back().first < last_y_offset) {
      int y =
          std::min(y_offset_and_sz.back().first + stride.height, last_y_offset);
      y_offset_and_sz.push_back(std::make_pair(y, patch_sz.height));
    }
    int last_x_offset = image_sz.width - patch_sz.width;
    while (x_offset_and_sz.back().first < last_x_offset) {
      int x =
          std::min(x_offset_and_sz.back().first + stride.width, last_x_offset);
      x_offset_and_sz.push_back(std::make_pair(x, patch_sz.width));
    }
  } else {  // mode == SplitImageMode::kStrideConstant
    int last_y_offset = image_sz.height - stride.height;
    while (y_offset_and_sz.back().first < last_y_offset) {
      int y_left = y_offset_and_sz.back().first + stride.height;
      int y_right = std::min(image_sz.height, y_left + patch_sz.height);
      y_offset_and_sz.push_back(std::make_pair(y_left, y_right - y_left));
    }
    int last_x_offset = image_sz.width - stride.width;
    while (x_offset_and_sz.back().first < last_x_offset) {
      int x_left = x_offset_and_sz.back().first + stride.width;
      int x_right = std::min(image_sz.width, x_left + patch_sz.width);
      x_offset_and_sz.push_back(std::make_pair(x_left, x_right - x_left));
    }
  }
  std::vector<cv::Rect> output;
  output.reserve(x_offset_and_sz.size() * y_offset_and_sz.size());
  for (const auto& pair_y : y_offset_and_sz) {
    for (const auto& pair_x : x_offset_and_sz) {
      cv::Rect rect(pair_x.first, pair_y.first, pair_x.second, pair_y.second);
      output.push_back(rect);
    }
  }
  return output;
};

}  // namespace flowthrone
