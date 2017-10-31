#include <gtest/gtest.h>
#include <glog/logging.h>
#include "io.h"
#include "test_utils.h"

namespace flowthrone {

TEST(ReadWriteFLO, Correct) {
  // Ensure that we can write a file, read it back, and get the same flow
  // that we started with.
  const cv::Mat uv = GetRandomFlow(20, 40);
  const std::string test_fn = "io_test.flo";
  WriteFLO(test_fn, uv);
  const cv::Mat uv_from_file = ReadFLO(test_fn);
  EXPECT_FLOAT_EQ(0.0f, cv::norm(uv - uv_from_file));
  CHECK_EQ(0, std::remove(test_fn.c_str()));
}

int main(int argc, char** argv) {
  google::InitGoogleLogging(argv[0]);
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

}  // namespace flowthrone
