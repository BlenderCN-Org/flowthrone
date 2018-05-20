#include "visualization.h"
#include "glog/logging.h"
#include "utils.h"

namespace flowthrone {

namespace internal {

std::vector<cv::Vec3b> MakeColorWheel() {
  int ry = 15;
  int yg = 6;
  int gc = 4;
  int cb = 11;
  int bm = 13;
  int mr = 6;
  std::vector<cv::Vec3b> colors;
  colors.reserve(ry + yg + gc + cb + bm + mr);
  for (int i = 0; i < ry; ++i) {
    colors.push_back(cv::Vec3b(0, floor(255.0 * i / ry), 255));
  }
  for (int i = 0; i < yg; ++i) {
    colors.push_back(cv::Vec3b(0, 255, 255 - floor(255.0 * i / yg)));
  }
  for (int i = 0; i < gc; ++i) {
    colors.push_back(cv::Vec3b(floor(255.0 * i / gc), 255, 0));
  }
  for (int i = 0; i < cb; ++i) {
    colors.push_back(cv::Vec3b(255, 255 - floor(255.0 * i / cb), 0));
  }
  for (int i = 0; i < bm; ++i) {
    colors.push_back(cv::Vec3b(255, 0, floor(255.0 * i / bm)));
  }
  for (int i = 0; i < mr; ++i) {
    colors.push_back(cv::Vec3b(255 - floor(255.0 * i / mr), 0, 255));
  }
  return colors;
}

cv::Vec3b BlendedColor(const std::vector<cv::Vec3b>& colorwheel, float x) {
  CHECK(0 <= x && x <= 1.0f);
  size_t n = colorwheel.size();
  x *= n;
  int hi = std::min<int>(n - 1, int(ceil(x)));
  int lo = std::min<int>(n - 1, int(x));
  float w = 1.0 - (x - lo);
  const auto& c0 = colorwheel[lo];
  const auto& c1 = colorwheel[hi];
  cv::Vec3b out;
  for (int i = 0; i < 3; ++i) {
    out[i] = std::min(255.0f, std::max(0.0f, w * c0[i] + (1 - w) * c1[i]));
  }
  return out;
}

float MaximumFlowMagnitude(const cv::Mat& flow) {
  CHECK_EQ(CV_32FC2, flow.type()) << "Input should be CV_32FC2.";
  float* flow_data = reinterpret_cast<float*>(flow.data);
  float uv_max_mag = std::numeric_limits<float>::lowest();
  for (size_t i = 0; i < flow.total(); ++i) {
    float uv = sqrt(flow_data[2 * i] * flow_data[2 * i] +
                    flow_data[2 * i + 1] * flow_data[2 * i + 1]);
    if (std::isnan(uv)) {
      continue;
    }
    uv_max_mag = std::max(uv, uv_max_mag);
  }
  return uv_max_mag;
}

cv::Vec3b GetPixelColor(const cv::Vec2f& _uv,
                        const std::vector<cv::Vec3b>& colorwheel,
                        float uv_max_mag) {
  if (std::isnan(_uv[0]) || std::isnan(_uv[1])) {
    return cv::Vec3b(0, 0, 0);
  }
  CHECK(!colorwheel.empty());
  float actual_mag_sq = _uv[0] * _uv[0] + _uv[1] * _uv[1];
  CHECK_LE(actual_mag_sq, uv_max_mag * uv_max_mag + 1e-2 * (actual_mag_sq))
      << "Provided upper bound on flow magnitude is not actually an upper "
         "bound! This will produce a poor visualization.";
  cv::Vec2f uv = _uv;
  uv[0] /= (uv_max_mag + 1e-9f);
  uv[1] /= (uv_max_mag + 1e-9f);
  size_t num_colors = colorwheel.size();
  float uv_mag = sqrt(uv[0] * uv[0] + uv[1] * uv[1]);  // in [0, \infty)
  float uv_angle = atan2(-uv[1], -uv[0]) / M_PI;       // in [-1, 1]
  float fk = (uv_angle + 1.0f) / 2.0f * (num_colors - 1);
  int k0 = static_cast<int>(fk) % num_colors;
  int k1 = (k0 + 1) % num_colors;
  float f = fk - k0;
  const cv::Vec3b& color0 = colorwheel[k0];
  const cv::Vec3b& color1 = colorwheel[k1];
  cv::Vec3f color;
  for (int q = 0; q < 3; ++q) {
    color[q] =
        1.0 - uv_mag * (1.0 - (color0[q] * (1 - f) + color1[q] * f) / 255.0f);
  }
  return cv::Vec3b(std::min<int>(255, color[0] * 255),
                   std::min<int>(255, color[1] * 255),
                   std::min<int>(255, color[2] * 255));
}

}  // namespace internal

cv::Mat ComputeFlowColor(const cv::Mat& flow, float least_max_flow_mag) {
  CHECK_EQ(CV_32FC2, flow.type()) << "Input should be CV_32FC2.";
  std::vector<cv::Vec3b> colorwheel = internal::MakeColorWheel();
  cv::Mat image(flow.rows, flow.cols, CV_8UC3);

  float uv_max_mag =
      std::max(least_max_flow_mag, internal::MaximumFlowMagnitude(flow));

  for (int r = 0; r < flow.rows; ++r) {
    for (int c = 0; c < flow.cols; ++c) {
      const cv::Vec2f& uv = flow.at<cv::Vec2f>(r, c);
      image.at<cv::Vec3b>(r, c) =
          internal::GetPixelColor(uv, colorwheel, uv_max_mag);
    }
  }
  return image;
}

cv::Mat HorizontalConcat(const cv::Mat& x, const cv::Mat& y) {
  CHECK_EQ(x.rows, y.rows);
  CHECK_EQ(x.type(), y.type());
  cv::Mat out;
  cv::hconcat(std::vector<cv::Mat>{x, y}, out);
  return out;
}

cv::Mat HorizontalConcat(const cv::Mat& i0, const cv::Mat& i1,
                         const cv::Mat& i2) {
  CHECK(i0.rows == i1.rows && i1.rows == i2.rows);
  CHECK(i0.type() == i1.type() && i1.type() == i2.type());
  cv::Mat out;
  cv::hconcat(std::vector<cv::Mat>{i0, i1, i2}, out);
  return out;
}

cv::Mat VerticalConcat(const cv::Mat& x, const cv::Mat& y) {
  CHECK_EQ(x.cols, y.cols);
  CHECK_EQ(x.type(), y.type());
  cv::Mat out;
  cv::vconcat(std::vector<cv::Mat>{x, y}, out);
  return out;
}

cv::Mat VisualizeTuple(const cv::Mat& I0, const cv::Mat& I1,
                       const cv::Mat& flow, const VisTupleOptions& opts) {
  cv::Mat flow_vis = ComputeFlowColor(flow, opts.least_max_flow_mag);
  return HorizontalConcat(0.5 * I0 + 0.5 * I1, flow_vis);
}

cv::Mat VisualizeTuple(const cv::Mat& I0, const cv::Mat& I1,
                       const cv::Mat& flow, const cv::Mat& flow_gt,
                       const VisTupleOptions& opts) {
  cv::Mat flow_vis = ComputeFlowColor(flow, opts.least_max_flow_mag);
  cv::Mat flow_vis_gt = ComputeFlowColor(flow_gt, opts.least_max_flow_mag);
  return HorizontalConcat(0.5 * I0 + 0.5 * I1, flow_vis, flow_vis_gt);
}

std::pair<cv::Mat, cv::Mat> OverlayWarpedPoints(const cv::Mat& I0,
                                                const cv::Mat& I1,
                                                const cv::Mat& flow,
                                                int point_spacing, int radius,
                                                int thickness) {
  std::vector<cv::Vec3b> colormap = internal::MakeColorWheel();
  int cols = I0.cols;
  int rows = I1.rows;
  int nx = cols / point_spacing;
  int ny = rows / point_spacing;
  CHECK(nx > 0 && ny > 0);
  auto points_img1 = Meshgrid(
      Linspace(0.0f + point_spacing / 2.0, cols - point_spacing / 2.0, nx),
      Linspace(0.0f + point_spacing / 2.0, cols - point_spacing / 2.0, ny));
  auto points_img0 = WarpWithFlow(points_img1, flow);
  cv::Mat img0_vis = I0.clone();
  cv::Mat img1_vis = I1.clone();
  CHECK_EQ(points_img1.size(), points_img0.size());
  for (size_t i = 0; i < points_img1.size(); ++i) {
    float x0, y0, x1, y1;
    std::tie(x1, y1) = points_img1[i];
    std::tie(x0, y0) = points_img0[i];
    float frac = i / static_cast<float>(points_img1.size());
    const cv::Vec3b& color_vec3b = internal::BlendedColor(colormap, frac);
    const cv::Scalar color(color_vec3b[0], color_vec3b[1], color_vec3b[2]);
    cv::circle(img1_vis, cv::Point(x1, y1), 1, color, 2);
    cv::circle(img0_vis, cv::Point(x0, y0), 1, color, 2);
  }
  return std::make_pair(img0_vis, img1_vis);
}

}  // namespace flowthrone
