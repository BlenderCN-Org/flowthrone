#include "visualization.h"
#include <gtest/gtest.h>
#include "gflags/gflags.h"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

DEFINE_bool(visualize, false, "When true, will display the image");

namespace flowthrone {

TEST(MakeColorWheel, CheckColorMap) {
  // This is a very weak test: only checks that the center point is colored
  // white.
  cv::Mat flow_x(10, 10, CV_32FC1, 0.0f);
  cv::Mat flow_y(10, 10, CV_32FC1, 0.0f);
  const float center_x = flow_x.cols / 2;
  const float center_y = flow_x.rows / 2;
  for (int r = 0; r < flow_x.rows; ++r) {
    for (int c = 0; c < flow_x.cols; ++c) {
      float dx = c - center_x;
      float dy = r - center_y;
      flow_x.at<float>(r, c) = dx;
      flow_y.at<float>(r, c) = dy;
    }
  }

  cv::Mat flow;
  cv::merge(std::vector<cv::Mat>{flow_x, flow_y}, flow);
  cv::Mat image = ComputeFlowColor(flow);
  EXPECT_EQ(cv::Vec3b(255, 255, 255),
            image.at<cv::Vec3b>(image.rows / 2, image.cols / 2))
      << "Point with zero displacement should have been white";

  if (FLAGS_visualize) {
    cv::resize(image, image, cv::Size(), 10.0, 10.0, cv::INTER_LINEAR);
    cv::imshow("image", image);
    cv::waitKey(0);
  }
}

}  // namespace flowthrone

int main(int argc, char** argv) {
  ::gflags::ParseCommandLineFlags(&argc, &argv, true);
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
