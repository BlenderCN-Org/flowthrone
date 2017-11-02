#include "evaluation.h"
#include "test_utils.h"
#include <gtest/gtest.h>
#include <glog/logging.h>
#include <numeric>

namespace flowthrone {

TEST(FlowEndpointError, ZeroErrorWhenArgumentsAreSame) {
  cv::Mat uv = GetRandomFlow(20, 40);
  cv::Mat uv_error;
  EXPECT_FLOAT_EQ(0.0f, FlowEndpointError(uv, uv, &uv_error));
  EXPECT_EQ(0.0f, cv::norm(uv_error));
}

TEST(FlowAngularError, ZeroErrorWhenArgumentsAreSame) {
  cv::Mat uv = GetRandomFlow(20, 40);
  cv::Mat uv_error;
  EXPECT_FLOAT_EQ(0.0f, FlowAngularError(uv, uv, &uv_error));
  EXPECT_EQ(0.0f, cv::norm(uv_error));
}

TEST(FlowEndpointError, Correct) {
  // Loop verifies that error does not depend on image size (due to averaging).
  for (int sz : {10, 20, 30}) {
    cv::Mat uv(sz, 2 * sz, CV_32FC2, cv::Scalar(1, 1));
    cv::Mat uv_gt(sz, 2 * sz, CV_32FC2, cv::Scalar(0, 0));
    ASSERT_NEAR(std::sqrt(2.0f), FlowEndpointError(uv, uv_gt), 1e-4);
  }
}

TEST(FlowAngularError, Correct) {
  // Loop verifies that error does not depend on image size (due to averaging).
  for (int sz : {10, 20, 30}) {
    cv::Mat uv(sz, 2 * sz, CV_32FC2, cv::Scalar(1, 0));
    cv::Mat uv_gt(sz, 2 * sz, CV_32FC2, cv::Scalar(0, 1));
    ASSERT_NEAR(std::acos(0.5f), FlowAngularError(uv, uv_gt), 1e-4);
    ASSERT_NEAR(std::acos(0.5f), FlowAngularError(-uv, uv_gt), 1e-4);
    ASSERT_NEAR(std::acos(0.0), FlowAngularError(-uv_gt, uv_gt), 1e-4);
    // Both displacement vectors point in the same direction.
    uv.setTo(cv::Scalar(0, 2));
    ASSERT_NEAR(std::acos(3 / (std::sqrt(2) * std::sqrt(5))),
                FlowAngularError(uv, uv_gt), 1e-4);
  }
}

TEST(NansAreIgnored, Works) {
  // Left size of the prediction matches groundtruth, while the right side is
  // random. Right side of groundtruth is set to NaN, so the error should be
  // zero for all metrics.
  cv::Mat uv_gt(10, 20, CV_32FC2, cv::Scalar(0, 0));
  cv::Mat uv(10, 20, CV_32FC2, cv::Scalar(0, 0));
  cv::Rect kRightHalf(10, 0, 10, 10);
  uv_gt(kRightHalf).setTo(std::numeric_limits<float>::quiet_NaN());
  uv(kRightHalf) = GetRandomFlow(10, 10);

  ASSERT_NEAR(0.0f, FlowEndpointError(uv, uv_gt), 1e-4);
  ASSERT_NEAR(0.0f, FlowAngularError(uv, uv_gt), 1e-4);
}

}  // namespace flowthrone
