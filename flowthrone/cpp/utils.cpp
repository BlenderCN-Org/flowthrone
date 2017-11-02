#include "utils.h"
#include <glog/logging.h>
#include <opencv2/imgproc/imgproc.hpp>

namespace flowthrone {

std::vector<cv::Mat> GetFlowMaps(const cv::Mat& flow) {
  std::vector<cv::Mat> flow_maps;
  cv::split(flow, flow_maps);
  // Compute x' = x + w(x,y), y' = y + w(x,y)
  for (int r = 0; r < flow.rows; ++r) {
    flow_maps[1].row(r) += r;
    float* data = flow_maps[0].ptr<float>(r);
    for (int c = 0; c < flow.cols; ++c) {
      data[c] += c;
    }
  }
  return flow_maps;
}

cv::Mat WarpWithFlow(const cv::Mat& I, const cv::Mat& flow) {
  CHECK_EQ(CV_32FC2, flow.type()) << "Incorrect cv::Mat format for flow";
  std::vector<cv::Mat> flow_maps = GetFlowMaps(flow);
  cv::Mat I_warped;
  cv::remap(I, I_warped, flow_maps[0], flow_maps[1], cv::INTER_LINEAR);
  return I_warped;
}

cv::Mat ResampleFlow(const cv::Mat& flow, const cv::Size& target_size) {
  CHECK_EQ(2, flow.channels());
  cv::Mat flow_out;
  cv::resize(flow, flow_out, target_size);
  std::vector<cv::Mat> flow_fields;
  cv::split(flow_out, flow_fields);
  CHECK_EQ(2, flow_fields.size());
  flow_fields[0] *= static_cast<float>(flow.cols) / target_size.width;
  flow_fields[1] *= static_cast<float>(flow.rows) / target_size.height;
  cv::merge(flow_fields, flow_out);
  return flow_out;
}

}  // namespace flowthrone
