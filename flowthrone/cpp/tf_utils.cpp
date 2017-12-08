#include "tf_utils.h"

namespace flowthrone {
namespace tf = tensorflow;

namespace {

void CheckInputIsConsistent(const std::vector<cv::Mat>& mats) {
  if (mats.empty()) {
    return;
  }
  const cv::Mat& front = mats.front();
  CHECK(std::all_of(
      mats.begin(), mats.end(),
      [&front](const cv::Mat& mat) { return front.size() == mat.size(); }))
      << "Cannot convert to a tensor: passed cv::Mat's have inconsistent "
         "dimensions.";
  CHECK(std::all_of(
      mats.begin(), mats.end(),
      [&front](const cv::Mat& mat) { return front.depth() == mat.depth(); }))
      << "Cannot convert to a tensor: passed cv::Mat's have inconsistent "
         "bit depth.";
  CHECK(std::all_of(mats.begin(), mats.end(),
                    [&front](const cv::Mat& mat) {
                      return front.channels() == mat.channels();
                    }))
      << "Cannot convert to a tensor: passed cv::Mat's have inconsistent "
         "number "
         "of channels.";
}

void FillPreallocatedTensor(const cv::Mat& mat, int idx, tf::Tensor* tensor) {
  CHECK_EQ(mat.depth(), CV_32F) << "Input matrix must be CV_32F";
  auto tensor_mapped = tensor->tensor<float, 4>();
  int rows = mat.rows;
  int cols = mat.cols;
  int channels = mat.channels();
  // int row_size = channels * cols * sizeof(float);

  for (int r = 0; r < rows; ++r) {
    const float* row = reinterpret_cast<const float*>(mat.row(r).data);
    for (int c = 0; c < cols; ++c) {
      for (int k = 0; k < channels; ++k) {
        tensor_mapped(idx, r, c, k) = row[k + channels * c];
      }
    }
  }
}

void FillMat(const tf::Tensor& tensor, int idx, cv::Mat* mat) {
  CHECK_EQ(tensor.dims(), 4) << "Input tensor must have 4 dimensions.";
  CHECK_LT(idx, tensor.dim_size(0));
  int rows = tensor.dim_size(1);
  int cols = tensor.dim_size(2);
  int channels = tensor.dim_size(3);
  int row_size = channels * cols * sizeof(float);

  *mat = cv::Mat(rows, cols, CV_32FC(channels));
  auto tensor_mapped = tensor.tensor<float, 4>();
  for (int r = 0; r < rows; ++r) {
    float* row = reinterpret_cast<float*>(mat->data + r * row_size);
    for (int c = 0; c < cols; ++c) {
      for (int k = 0; k < channels; ++k) {
        row[k + c * channels] = tensor_mapped(idx, r, c, k);
      }
    }
  }
}

}  // namespace

void AsTensor(const std::vector<cv::Mat>& mats, tf::Tensor* tensor) {
  if (mats.empty()) {
    *tensor = tf::Tensor();
    return;
  }
  CheckInputIsConsistent(mats);
  int n = mats.size();
  int rows = mats[0].rows;
  int cols = mats[0].cols;
  int channels = mats[0].channels();

  *tensor =
      tf::Tensor(tf::DT_FLOAT, tf::TensorShape({n, rows, cols, channels}));
  for (int i = 0; i < n; ++i) {
    FillPreallocatedTensor(mats[i], i, tensor);
  }
}

void AsTensor(const cv::Mat& mat, tf::Tensor* tensor) {
  int rows = mat.rows;
  int cols = mat.cols;
  int channels = mat.channels();

  *tensor =
      tf::Tensor(tf::DT_FLOAT, tf::TensorShape({1, rows, cols, channels}));
  FillPreallocatedTensor(mat, 0, tensor);
}

void AsMat(const tf::Tensor& tensor, std::vector<cv::Mat>* mats) {
  CHECK_EQ(4, tensor.dims()) << "Currently we assume that the tensor has "
                                "four dimensions even though there is not a "
                                "fundamental reason to do so.";
  CHECK_EQ(tf::DT_FLOAT, tensor.dtype()) << "Input tensor must be DT_FLOAT";
  *mats = std::vector<cv::Mat>{};
  int n = tensor.dim_size(0);
  for (int i = 0; i < n; ++i) {
    mats->push_back(cv::Mat());
    FillMat(tensor, i, &mats->back());
  }
}

void AsMat(const tf::Tensor& tensor, cv::Mat* mat) {
  CHECK_EQ(4, tensor.dims()) << "Currently we assume that the tensor has "
                                "four dimensions even though there is not a "
                                "fundamental reason to do so.";
  CHECK_EQ(tf::DT_FLOAT, tensor.dtype()) << "Input tensor must be DT_FLOAT";
  *mat = cv::Mat();
  FillMat(tensor, 0, mat);
}

// Deprecated.
tf::Tensor AsTensor(const cv::Mat& x) {
  CHECK_EQ(x.depth(), CV_32F) << "Input matrix must be CV_32F";
  tf::Tensor y(tf::DT_FLOAT,
               tf::TensorShape({1, x.rows, x.cols, x.channels()}));
  FillPreallocatedTensor(x, 0, &y);
  return y;
}

cv::Mat AsMat(const tf::Tensor& x) {
  CHECK_EQ(tf::DT_FLOAT, x.dtype()) << "Input tensor must be DT_FLOAT";
  CHECK_EQ(x.dims(), 4) << "Input tensor must have 4 dimensions.";
  CHECK_EQ(1, x.dim_size(0)) << "Batch size of the input tensor must be 1";
  cv::Mat output;
  FillMat(x, 0, &output);
  return output;
}

void CHECK_STATUS(const tf::Status& x) { CHECK(x.ok()) << x.ToString(); }

}  // namespace flowthrone