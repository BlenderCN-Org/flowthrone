#include <gtest/gtest.h>
#include <glog/logging.h>
#include "tf_utils.h"
#include "test_utils.h"

namespace flowthrone {

TEST(ConvertToAndFromTensor, Correct) {
  // Ensure that we can take a random cv::Mat, convert it to a tensor,
  // convert it back to cv::Mat and get the same result.
  int rows = 1 + rand() % 100;
  int cols = 1 + rand() % 100;
  const cv::Mat x = GetRandomFlow(rows, cols);
  const cv::Mat x_converted = AsMat(AsTensor(x));
  ASSERT_EQ(x.size(), x_converted.size());
  EXPECT_FLOAT_EQ(0.0f, cv::norm(x - x_converted));
}

}  // namespace flowthrone
