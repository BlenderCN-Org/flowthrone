#include "utils.h"
#include <glog/logging.h>
#include <gtest/gtest.h>

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

TEST(WarpWithFlow, DiscreteDisplacement) {
  using std::pair;
  using std::make_pair;
  cv::Mat flow(4, 4, CV_32FC2, cv::Scalar(1, 0));
  std::vector<pair<float, float>> input_points;
  constexpr int kNumPoints = 100;
  for (int i = 0; i < kNumPoints; ++i) {
    input_points.emplace_back(drand48() * 10.0f - 5.0f,
                              drand48() * 10.0f - 5.0f);
  }
  auto output_points = WarpWithFlow(input_points, flow);
  ASSERT_EQ(output_points.size(), input_points.size());
  for (int i = 0; i < kNumPoints; ++i) {
    EXPECT_EQ(output_points[i].first, input_points[i].first - 1.0f);
    EXPECT_EQ(output_points[i].second, input_points[i].second);
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

TEST(SplitImageTest, SimpleCorrect) {
  int n = 20;
  int k = 5;
  cv::Size image_size(k * n, n);
  cv::Size patch_size(n, n);
  std::vector<cv::Rect> tiles = SplitImage(image_size, patch_size, patch_size);
  ASSERT_EQ(k, tiles.size());
  for (int i = 0; i < k; ++i) {
    ASSERT_EQ(cv::Rect(n * i, 0, n, n), tiles[i]);
  }
}

TEST(SplitImageTest, NonIntegralSplit) {
  cv::Size image_size(110, 50);
  cv::Size patch_size(50, 50);
  cv::Size stride_size(25, 25);

  std::vector<cv::Rect> tiles = SplitImage(image_size, patch_size, stride_size,
                                           SplitImageMode::kSizeConstant);
  ASSERT_EQ(4, tiles.size());
  ASSERT_EQ(cv::Rect(0, 0, 50, 50), tiles[0]);
  ASSERT_EQ(cv::Rect(25, 0, 50, 50), tiles[1]);
  ASSERT_EQ(cv::Rect(50, 0, 50, 50), tiles[2]);
  ASSERT_EQ(cv::Rect(60, 0, 50, 50), tiles[3]);
  // Note that the stride is not respected near the right edge of the image.
}

TEST(SplitImageTest, NonIntegralSplit2) {
  cv::Size image_size(110, 50);
  cv::Size patch_size(50, 50);
  cv::Size stride_size(25, 25);

  std::vector<cv::Rect> tiles = SplitImage(image_size, patch_size, stride_size,
                                           SplitImageMode::kStrideConstant);
  ASSERT_EQ(10, tiles.size());

  ASSERT_EQ(cv::Rect(0, 0, 50, 50), tiles[0]);
  ASSERT_EQ(cv::Rect(25, 0, 50, 50), tiles[1]);
  ASSERT_EQ(cv::Rect(50, 0, 50, 50), tiles[2]);
  ASSERT_EQ(cv::Rect(75, 0, 35, 50), tiles[3]);
  ASSERT_EQ(cv::Rect(100, 0, 10, 50), tiles[4]);

  ASSERT_EQ(cv::Rect(0, 25, 50, 25), tiles[5]);
  ASSERT_EQ(cv::Rect(25, 25, 50, 25), tiles[6]);
  ASSERT_EQ(cv::Rect(50, 25, 50, 25), tiles[7]);
  ASSERT_EQ(cv::Rect(75, 25, 35, 25), tiles[8]);
  ASSERT_EQ(cv::Rect(100, 25, 10, 25), tiles[9]);
}

TEST(Linspace, Works) {
  ASSERT_EQ(std::vector<float>({1, 2, 3}), Linspace(1, 3, 3));
  ASSERT_EQ(std::vector<float>({10}), Linspace(10, 10, 1));
  ASSERT_EQ(std::vector<float>(), Linspace(10, 10, 0));
  ASSERT_EQ(std::vector<float>({1, 3, 5, 7, 9}), Linspace(1, 9, 5));
}

TEST(Meshgrid, Works) {
  using std::pair;
  using std::vector;
  vector<pair<float, float>> expected;

  expected = vector<pair<float, float>>();
  ASSERT_EQ(expected, Meshgrid(vector<float>(), vector<float>()));

  expected = vector<pair<float, float>>{{1, 0}, {2, 0}};
  ASSERT_EQ(expected, Meshgrid(vector<float>({1, 2}), vector<float>({0})));

  expected = vector<pair<float, float>>{{1, 3}, {2, 3}, {1, 4}, {2, 4}};
  ASSERT_EQ(expected, Meshgrid(vector<float>({1, 2}), vector<float>({3, 4})));
}

TEST(TriangleKernel, Works) {
  cv::Mat kernel, expected_kernel;

  // 4x1 kernel
  kernel = TriangleKernel(cv::Size(4, 1));
  std::vector<float> values{0.0f, 0.5f, 1.0f, 0.5f};
  expected_kernel = cv::Mat(1, 4, CV_32FC1);
  for (size_t i = 0; i < values.size(); ++i) {
    expected_kernel.at<float>(0, i) = values[i];
  }
  ASSERT_EQ(cv::Size(4, 1), kernel.size());
  ASSERT_EQ(0.0, cv::norm(kernel - expected_kernel));

  // 3x3 kernel
  kernel = TriangleKernel(cv::Size(3, 3));
  expected_kernel = cv::Mat::zeros(3, 3, CV_32FC1);
  expected_kernel.at<float>(1, 1) = 1.0f;
  ASSERT_EQ(cv::Size(3, 3), kernel.size());
  ASSERT_EQ(CV_32F, kernel.type());
  ASSERT_EQ(0.0, cv::norm(kernel - expected_kernel));

  // Identity kernel.
  kernel = TriangleKernel(cv::Size(1, 1));
  ASSERT_EQ(cv::Size(1, 1), kernel.size());
  ASSERT_EQ(1.0f, kernel.at<float>(0, 0));
}

TEST(ComputeFlowDivergence, DISABLED_TODO) {}

TEST(ProbabilityOfOcclusion, CorrectMovingSquare) {
  // A 6x6 square is moving from (2,2) to (4,2) (two pixels to the right).
  // The occluded region should be a cv::Rect(8, 2, 2, 6) (i.e. two pixels to
  // the right of the original rectangle's location).
  constexpr int kHeight = 6;
  constexpr int kWidth = 6;
  constexpr int kX = 2;
  constexpr int kY = 2;
  cv::Mat I0(10, 10, CV_32FC1, cv::Scalar(0));
  cv::Mat I1(10, 10, CV_32FC1, cv::Scalar(0));
  I0(cv::Rect(kX, kY, kWidth, kHeight)).setTo(1.0f);
  I1(cv::Rect(kX + 2, kY, kWidth, kHeight)).setTo(1.0f);
  cv::Mat wx(10, 10, CV_32FC1, cv::Scalar(0.0f));
  cv::Mat wy(10, 10, CV_32FC1, cv::Scalar(0.0f));
  wx(cv::Rect(kX, kY, kWidth, kHeight)).setTo(2.0f);

  cv::Mat expected_occ(10, 10, CV_32FC1, cv::Scalar(0));
  expected_occ(cv::Rect(kX + kWidth, kY, 2, kHeight)).setTo(1.0f);

  cv::Mat flow;
  cv::merge(std::vector<cv::Mat>{wx, wy}, flow);

  constexpr float kSigmaD = 1e5;
  constexpr float kSigmaI = 1e-5;
  cv::Mat occ = ProbabilityOfOcclusion(I0, I1, flow, kSigmaD, kSigmaI);
  EXPECT_NEAR(0.0f, cv::norm(occ - expected_occ), 1e-3)
      << "Predicted incorrect occlusion? Predicted: \n"
      << occ << "\nExpected:\n"
      << expected_occ;
}

}  // namespace flowthrone
