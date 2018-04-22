#include "evaluation.h"
#include <glog/logging.h>
#include <gtest/gtest.h>
#include <numeric>
#include "test_utils.h"

namespace flowthrone {

TEST(FlowEndpointError, ZeroErrorWhenArgumentsAreSame) {
  cv::Mat uv = GetRandomFlow(20, 40);
  cv::Mat uv_error;
  EXPECT_NEAR(0.0f, FlowEndpointError(uv, uv, &uv_error), 1e-5);
  EXPECT_NEAR(0.0f, cv::norm(uv_error), 1e-5);
}

TEST(FlowAngularError, ZeroErrorWhenArgumentsAreSame) {
  cv::Mat uv = GetRandomFlow(20, 40);
  cv::Mat uv_error;
  EXPECT_NEAR(0.0f, FlowAngularError(uv, uv, &uv_error), 1e-5);
  EXPECT_NEAR(0.0f, cv::norm(uv_error), 1e-5);
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

namespace {

Interval CreateInterval(float a, float b) {
  Interval interval;
  interval.set_lo(a);
  interval.set_hi(b);
  return interval;
}

}  // namespace

TEST(AverageErrorByInterval, Works) {
  //  [ 5 5 5 5 5 ]   <-- optical flow norm
  //  [ 0 0 0 0 0 ]
  //
  //  [ 2 2 2 2 2 ]   <-- error image
  //  [ 1 1 1 1 1 ]
  using google::protobuf::RepeatedPtrField;
  using google::protobuf::RepeatedField;

  cv::Rect top_rows(0, 0, 20, 5);
  cv::Mat uv(10, 20, CV_32FC2, cv::Scalar(0));
  uv(top_rows).setTo(cv::Vec2f(3.0, 4.0f));
  cv::Mat error(10, 20, CV_32FC1, cv::Scalar(1.0f));
  error(top_rows).setTo(cv::Scalar(2.0f));

  // Verify that when interval is [0, infty), then the average is returned.
  RepeatedPtrField<Interval> intervals;
  *intervals.Add() = CreateInterval(0, 1e9);
  *intervals.Add() = CreateInterval(0, 1);
  *intervals.Add() = CreateInterval(0, 5);  // <-- should be same as above,
                                            //     (the interval is half open).
  *intervals.Add() = CreateInterval(5, 6);
  *intervals.Add() = CreateInterval(10, 11);

  auto errors = AverageErrorByInterval(uv, error, intervals);
  ASSERT_EQ(intervals.size(), errors.size());

  float average_error = cv::sum(error)[0] / error.total();
  EXPECT_EQ(average_error, errors[0])
      << "Should have computed average over the entire 'error' image.";
  EXPECT_EQ(1.0f, errors[1]) << "Incorrect average, on interval [0, 1)";
  EXPECT_EQ(1.0f, errors[2]) << "Incorrect average, on interval [0, 5)";
  EXPECT_EQ(2.0f, errors[3]) << "Incorrect average, on interval [5, 6)";

  EXPECT_TRUE(std::isnan(errors[4]))
      << "Nothing fell into the interval [10, 11), and the convention is to "
         "return 'NaN' in this situation.";
}

}  // namespace flowthrone
