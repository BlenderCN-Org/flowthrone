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

std::vector<std::pair<float, float>> WarpWithFlow(
    const std::vector<std::pair<float, float>>& points, const cv::Mat& flow) {
  std::vector<std::pair<float, float>> warped;
  warped.reserve(points.size());
  for (const auto& p : points) {
    float x = p.first;
    float y = p.second;
    // TODO: Currently just does the 'nearest neighbor' flow warping, which is
    // stupid and terrible, but easy.
    int x_rounded = std::max(std::min<int>(round(x), flow.cols - 1), 0);
    int y_rounded = std::max(std::min<int>(round(y), flow.rows - 1), 0);
    const cv::Vec2f& warp = flow.at<cv::Vec2f>(y_rounded, x_rounded);
    warped.emplace_back(x - warp[0], y - warp[1]);
  }
  return warped;
}

cv::Mat FlowMagnitude(const cv::Mat& flow) {
  CHECK_EQ(CV_32FC2, flow.type()) << "Incorrect cv::Mat format for flow";
  std::vector<cv::Mat> flow_maps;
  cv::split(flow, flow_maps);
  cv::Mat magnitude, dxdx, dydy;
  cv::multiply(flow_maps[0], flow_maps[0], dxdx);
  cv::multiply(flow_maps[1], flow_maps[1], dydy);
  cv::sqrt(dxdx + dydy, magnitude);
  return magnitude;
}

cv::Mat WarpWithFlow(const cv::Mat& I, const cv::Mat& flow) {
  CHECK_EQ(CV_32FC2, flow.type()) << "Incorrect cv::Mat format for flow";
  std::vector<cv::Mat> flow_maps = GetFlowMaps(flow);
  cv::Mat I_warped;
  cv::remap(I, I_warped, flow_maps[0], flow_maps[1], cv::INTER_LINEAR);
  return I_warped;
}

cv::Mat ComputeResidual(const cv::Mat& I0, const cv::Mat& I1,
                        const cv::Mat& flow) {
  return I0 - WarpWithFlow(I1, flow);
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

std::vector<float> Linspace(float min, float max, int num) {
  if (num == 0) {
    return {};
  }
  if (num == 1 && (min == max)) {
    return {min};
  }
  CHECK_LT(min, max)
      << "Asked to linspace points where 'smaller' value > 'larger' value.";
  CHECK_LT(1, num) << "If min/max are distinct, then must have at least two "
                      "points as input to "
                      "linspace. ";
  std::vector<float> out(num);
  float dx = (max - min) / (num - 1);
  for (int i = 0; i < num; ++i) {
    out[i] = min + i * dx;
  }
  return out;
}

std::vector<std::pair<float, float>> Meshgrid(const std::vector<float>& x,
                                              const std::vector<float>& y) {
  if (x.empty() || y.empty()) {
    return {};
  }
  std::vector<std::pair<float, float>> out;
  out.reserve(x.size() * y.size());
  for (float yy : y) {
    for (float xx : x) {
      out.emplace_back(xx, yy);
    }
  }
  return out;
}

cv::Mat TriangleKernel(cv::Size size) {
  int xc = size.width / 2;
  int yc = size.height / 2;
  cv::Mat tri(size, CV_32FC1);
  for (int y = 0; y < tri.rows; ++y) {
    float* row = reinterpret_cast<float*>(tri.row(y).data);
    float wy = yc > 0 ? 1.0f - std::abs(y - yc) / float(yc) : 1.0f;
    for (int x = 0; x < tri.cols; ++x) {
      float wx = xc > 0 ? 1.0f - std::abs(x - xc) / float(xc) : 1.0f;
      row[x] = wx * wy;
    }
  }
  return tri;
}

std::vector<cv::Rect> SplitImage(cv::Size image_sz, cv::Size patch_sz,
                                 cv::Size stride, SplitImageMode mode) {
  CHECK(stride.width >= 1 && stride.height >= 1) << "Stride must be positive.";
  CHECK(image_sz.width >= patch_sz.width && image_sz.height >= patch_sz.height)
      << "Currently only support tiling of images that are at least as large "
         "as the patch size.";
  CHECK(patch_sz.width >= stride.width && patch_sz.height >= stride.height)
      << "Patch must be larger than stride. In other words, it is only "
         "possible to densely tile the image.";

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
