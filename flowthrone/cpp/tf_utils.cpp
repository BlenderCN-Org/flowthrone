#include "tf_utils.h"

namespace flowthrone {
namespace tf = tensorflow;

tf::Tensor AsTensor(const cv::Mat& x) {
  CHECK_EQ(x.depth(), CV_32F) << "Input matrix must be CV_32F";
  tf::Tensor y(tf::DT_FLOAT,
               tf::TensorShape({1, x.rows, x.cols, x.channels()}));
  auto y_mapped = y.tensor<float, 4>();
  int rows = x.rows;
  int cols = x.cols;
  int channels = x.channels();
  int row_size = channels * cols * sizeof(float);

  for (int r = 0; r < rows; ++r) {
    const float* row = reinterpret_cast<const float*>(x.data + r * row_size);
    for (int c = 0; c < cols; ++c) {
      for (int k = 0; k < channels; ++k) {
        float value = row[k + channels * c];
        y_mapped(0, r, c, k) = value;
      }
    }
  }
  return y;
}

cv::Mat AsMat(const tf::Tensor& x) {
  CHECK_EQ(tf::DT_FLOAT, x.dtype()) << "Input tensor must be DT_FLOAT";
  CHECK_EQ(x.dims(), 4) << "Input tensor must have 4 dimensions.";
  CHECK_EQ(1, x.dim_size(0)) << "Batch size of the input tensor must be 1";
  int rows = x.dim_size(1);
  int cols = x.dim_size(2);
  int channels = x.dim_size(3);
  int row_size = channels * cols * sizeof(float);

  cv::Mat y(rows, cols, CV_32FC(channels));
  auto x_mapped = x.tensor<float, 4>();
  for (int r = 0; r < rows; ++r) {
    float* row = reinterpret_cast<float*>(y.data + r * row_size);
    for (int c = 0; c < cols; ++c) {
      for (int k = 0; k < channels; ++k) {
        row[k + c * channels] = x_mapped(0, r, c, k);
      }
    }
  }
  return y;
}

void CHECK_STATUS(const tf::Status& x) { CHECK(x.ok()) << x.ToString(); }

}  // namespace flowthrone
