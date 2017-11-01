#include <cmath>
#include <glog/logging.h>
#include "test_utils.h"

namespace flowthrone {

cv::Mat GetRandomFlow(int rows, int cols) {
  cv::Mat uv(rows, cols, CV_32FC2);
  float* data = reinterpret_cast<float*>(uv.data);
  for (int i = 0; i < rows * cols * 2; ++i) {
    data[i] = drand48();
  }
  return uv;
}

}  // namespace flowthrone
