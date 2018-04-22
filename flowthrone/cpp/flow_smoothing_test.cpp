#include "flow_smoothing.h"
#include <gflags/gflags.h>
#include <glog/logging.h>
#include <gtest/gtest.h>
#include <opencv2/highgui/highgui.hpp>
#include "utils.h"
#include "visualization.h"

DEFINE_bool(visualize, false, "Visualize results");

namespace flowthrone {

TEST(DenoiseColorWeightedFilter, DoesTheRightThing) {
  cv::Rect center(25, 25, 50, 50);
  cv::Mat image(100, 100, CV_32FC1, cv::Scalar(0.0f));
  cv::Mat flow_x(100, 100, CV_32FC1);
  cv::Mat flow_y(100, 100, CV_32FC1);

  for (auto& mat : {flow_x, flow_y}) {
    float* image_data = reinterpret_cast<float*>(mat.data);
    for (size_t i = 0; i < mat.total(); ++i) {
      image_data[i] = 0.5 * static_cast<float>(drand48());
    }
    cv::Mat subimage = mat(center);
    subimage = subimage + cv::Mat(subimage.rows, subimage.cols, CV_32FC1,
                                  cv::Scalar(0.5f));
  }
  image(center) = 1;

  cv::Mat flow;
  cv::merge(std::vector<cv::Mat>{flow_x, flow_y}, flow);
  DenoisingOptions options;
  options.sigma_distance = 100;
  options.window_size = 21;
  options.sigma_intensity = 0.01;

  cv::Mat denoised_flow = DenoiseColorWeightedFilter(flow, image, options);

  cv::Mat flow_image =
      HorizontalConcat(ComputeFlowColor(flow), ComputeFlowColor(denoised_flow));

  LOG(INFO) << "Showing the original image, original (noisy) optical flow "
            << "and the resulting (denoised) optical flow.";
  cv::imshow("original_image", image);
  cv::imshow("image2", flow_image);
  cv::waitKey(0);
}

int main(int argc, char** argv) {
  google::ParseCommandLineFlags(&argc, &argv, true);
  google::InitGoogleLogging(argv[0]);
  ::testing::InitGoogleTest(&argc, argv);
  FLAGS_alsologtostderr = 1;
  return RUN_ALL_TESTS();
}

}  // namespace flowthrone
