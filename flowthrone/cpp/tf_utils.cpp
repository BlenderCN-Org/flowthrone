#include "tf_utils.h"

namespace tf = tensorflow;
namespace flowthrone {

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

template <typename T>
void FillPreallocatedTensor(const cv::Mat& mat, int idx, tf::Tensor* tensor) {
  auto tensor_mapped = tensor->tensor<T, 4>();
  int rows = mat.rows;
  int cols = mat.cols;
  int channels = mat.channels();

  for (int r = 0; r < rows; ++r) {
    const T* row = reinterpret_cast<const T*>(mat.row(r).data);
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

  if (mats[0].depth() == CV_32F) {
    *tensor =
        tf::Tensor(tf::DT_FLOAT, tf::TensorShape({n, rows, cols, channels}));
    for (int i = 0; i < n; ++i) {
      FillPreallocatedTensor<float>(mats[i], i, tensor);
    }
  } else if (mats[0].depth() == CV_8U) {
    *tensor =
        tf::Tensor(tf::DT_UINT8, tf::TensorShape({n, rows, cols, channels}));
    for (int i = 0; i < n; ++i) {
      FillPreallocatedTensor<uint8_t>(mats[i], i, tensor);
    }
  } else {
    LOG(FATAL) << "Not implemented.";
  }
}

void AsTensor(const cv::Mat& mat, tf::Tensor* tensor) {
  int rows = mat.rows;
  int cols = mat.cols;
  int channels = mat.channels();

  if (mat.depth() == CV_32F) {
    *tensor =
        tf::Tensor(tf::DT_FLOAT, tf::TensorShape({1, rows, cols, channels}));
    FillPreallocatedTensor<float>(mat, 0, tensor);
  } else if (mat.depth() == CV_8U) {
    *tensor =
        tf::Tensor(tf::DT_UINT8, tf::TensorShape({1, rows, cols, channels}));
    FillPreallocatedTensor<uint8_t>(mat, 0, tensor);
  } else {
    LOG(FATAL) << "Not implemented: you passed a cv::Mat of type "
               << mat.type();
  }
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

const tf::NodeDef* GetTensorByName(const tf::GraphDef& graph,
                                   const std::string& name) {
  for (const auto& node : graph.node()) {
    if (node.name() == name) {
      return &node;
    }
  }
  return nullptr;
}

tf::DataType GetTensorDataType(const tf::GraphDef& graph_def,
                               const std::string& name) {
  const tf::NodeDef* node = GetTensorByName(graph_def, name);
  CHECK(node) << "Could not find tensor called '" << name << "'";
  CHECK(node->attr().count("dtype"));
  return node->attr().at("dtype").type();
}

tf::TensorShapeProto GetTensorShapeProto(const tf::GraphDef& graph_def,
                                         const std::string& name) {
  const std::string kShapeKey = "_output_shapes";
  const tf::NodeDef* node = GetTensorByName(graph_def, name);
  CHECK(node) << "Could not find tensor called '" << name << "'";
  CHECK(node->attr().count(kShapeKey)) << "Could not find key: " << kShapeKey
                                       << " DebugString\n"
                                       << node->DebugString();
  CHECK_GE(node->attr().at(kShapeKey).list().shape_size(), 1);
  return node->attr().at(kShapeKey).list().shape(0);
}

}  // namespace flowthrone
