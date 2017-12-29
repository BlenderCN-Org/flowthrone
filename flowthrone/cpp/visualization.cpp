#include "visualization.h"
#include "glog/logging.h"

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

}  // namespace internal

cv::Mat ComputeFlowColor(const cv::Mat& flow) {
  CHECK_EQ(CV_32FC2, flow.type()) << "Input should be CV_32FC2.";
  std::vector<cv::Vec3b> colorwheel = internal::MakeColorWheel();
  int num_colors = colorwheel.size();
  cv::Mat image(flow.rows, flow.cols, CV_8UC3);

  // Find largest flow magnitude.
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
  for (int r = 0; r < flow.rows; ++r) {
    for (int c = 0; c < flow.cols; ++c) {
      cv::Vec2f uv = flow.at<cv::Vec2f>(r, c);
      if (std::isnan(uv[0]) || std::isnan(uv[1])) {
        image.at<cv::Vec3b>(r, c) = cv::Vec3b(0, 0, 0);
        continue;
      }
      uv[0] /= (uv_max_mag + 1e-9f);
      uv[1] /= (uv_max_mag + 1e-9f);
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
            1.0 -
            uv_mag * (1.0 - (color0[q] * (1 - f) + color1[q] * f) / 255.0f);
      }
      image.at<cv::Vec3b>(r, c) = cv::Vec3b(std::min<int>(255, color[0] * 255),
                                            std::min<int>(255, color[1] * 255),
                                            std::min<int>(255, color[2] * 255));
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

}  // namespace flowthrone
