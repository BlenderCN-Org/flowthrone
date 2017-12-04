#include <gtest/gtest.h>
#include <glog/logging.h>
#include "tf_utils.h"
#include "test_utils.h"

namespace flowthrone {
namespace tf = tensorflow;

TEST(ConvertToAndFromTensor, Correct) {
  // Ensure that we can take a random cv::Mat, convert it to a tensor,
  // convert it back to cv::Mat and get the same result.
  int rows = 1 + rand() % 100;
  int cols = 1 + rand() % 100;
  const cv::Mat x = GetRandomFlow(rows, cols);
  tf::Tensor tensor;
  AsTensor(x, &tensor);
  cv::Mat x_converted;
  AsMat(tensor, &x_converted);
  ASSERT_EQ(x.size(), x_converted.size());
  EXPECT_FLOAT_EQ(0.0f, cv::norm(x - x_converted));
}

TEST(ConvertToAndFromTensorVectorVersion, Correct) {
  int rows = 200;
  int cols = 200;
  cv::Mat big_matrix = GetRandomFlow(rows, cols);
  // Subsets of the large matrix selected like so will not be deep-copied, and
  // therefore will be not be laid out contiguously in memory.
  std::vector<cv::Mat> mats{big_matrix(cv::Rect(0, 0, 50, 50)),
                            big_matrix(cv::Rect(20, 20, 50, 50)),
                            big_matrix(cv::Rect(100, 100, 50, 50))};
  tf::Tensor tensor;
  AsTensor(mats, &tensor);
  std::vector<cv::Mat> mats_converted;
  AsMat(tensor, &mats_converted);
  ASSERT_EQ(mats.size(), mats_converted.size());
  for (size_t i = 0; i < mats.size(); ++i) {
    EXPECT_FLOAT_EQ(0.0f, cv::norm(mats[i] - mats_converted[i]));
  }
}

}  // namespace flowthrone
