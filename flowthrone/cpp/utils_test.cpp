#include "utils.h"
#include <gtest/gtest.h>
#include <glog/logging.h>

namespace flowthrone {

namespace {

cv::Mat Identity(int n) {
  cv::Mat m(n, n, CV_8UC1, cv::Scalar(0));
  for (int i = 0; i < n; ++i) {
    m.at<uchar>(i, i) = 255;
  }
  return m;
}

}  // namespace

TEST(WarpWithFlow, ZeroFlowTest) {
  cv::Mat I = Identity(4);
  cv::Mat flow(4, 4, CV_32FC2, 0.0f);
  cv::Mat I_warped = WarpWithFlow(I, flow);
  EXPECT_GE(1e-9, cv::norm(I - I_warped))
      << "Flow is zero, so the warped image is identical to the warped one";
}

TEST(WarpWithFlow, Displacement) {
  cv::Mat I = Identity(4);
  cv::Mat flow(4, 4, CV_32FC2, cv::Scalar(1, 0));
  cv::Mat I_warped = WarpWithFlow(I, flow);
  // The warped image should look like:
  //  1 0 0 0        0 0 0 0
  //  0 1 0 0  --->  1 0 0 0
  //  0 0 1 0  --->  0 1 0 0
  //  0 0 0 1        0 0 1 0
  // Note how regions without corresponces are zero-filled.
  for (int r = 1; r < I.rows; ++r) {
    EXPECT_EQ(I.at<uchar>(r, r), I_warped.at<uchar>(r, r - 1));
  }
}

TEST(ResampleFlow, Correct) {
  cv::Mat uv;
  cv::merge(std::vector<cv::Mat>{cv::Mat(10, 10, CV_32FC1, cv::Scalar(10)),
                                 cv::Mat(10, 10, CV_32FC1, cv::Scalar(20))},
            uv);
  cv::Mat uv_resampled = ResampleFlow(uv, cv::Size(100, 50));
  // Flow field is constant, so examine a single value.
  const cv::Vec2f& uv_value = uv_resampled.at<cv::Vec2f>(10, 10);
  EXPECT_FLOAT_EQ(1.0f, uv_value[0]);
  EXPECT_FLOAT_EQ(4.0f, uv_value[1]);
  EXPECT_EQ(cv::Size(100, 50), uv_resampled.size());
}

}  // namespace flowthrone
