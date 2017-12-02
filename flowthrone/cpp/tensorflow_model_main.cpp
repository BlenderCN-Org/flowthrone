#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

#include "gflags/gflags.h"
#include "glog/logging.h"

#include "tf_utils.h"
#include "visualization.h"
#include "io.h"
#include "optical_flow_tf_model.h"

std::string gBasePath = "/home/vasiliy/";
DEFINE_string(export_dir, "/home/vasiliy/Sandbox/flowthrone/data/",
              "Path to the directory with SavedModel");
DEFINE_string(img1,
              //"/home/vasiliy/data/middlebury/Hydrangea/frame10.png",
              "/home/vasiliy/030000_img1.png", "Filename of image1");
DEFINE_string(img2, "/home/vasiliy/030000_img2.png",
              //"/home/vasiliy/data/middlebury/Hydrangea/frame11.png",
              "Filename of image2");
DEFINE_string(gt, "/home/vasiliy/030000_flow1.flo",
              //"/home/vasiliy/data/middlebury/Hydrangea/flow10.flo",
              "Groundtruth");

namespace tf = tensorflow;

namespace flowthrone {

int main(int argc, char** argv) {
  cv::Mat img1 = cv::imread(FLAGS_img1);
  cv::Mat img2 = cv::imread(FLAGS_img2);
  CHECK(img1.total() && img2.total())
      << "Could not load one or more images. Maybe you did not provide "
         "filenames, or maybe the provided filenames are incorrect? "
      << FLAGS_img1 << " " << FLAGS_img2 << " " << img1.total() << " "
      << img2.total();
  CHECK(!FLAGS_export_dir.empty())
      << "You must provide a tensorflow graph definition to be able to run "
         "binary. ";

  OpticalFlowTensorFlowModel model(FLAGS_export_dir);

  cv::Mat predicted_flow;
  model.Run(img1, img2, predicted_flow);

  cv::Mat gt_flow = ReadFLO(FLAGS_gt);

  cv::resize(predicted_flow, predicted_flow, img1.size());
  cv::imshow("flow", HorizontalConcat(ComputeFlowColor(predicted_flow),
                                      ComputeFlowColor(gt_flow)));
  cv::imshow("images", HorizontalConcat(img1, img2));
  cv::waitKey(0);

  return 0;
}

}  // namespace flowthrone

int main(int argc, char** argv) {
  ::gflags::ParseCommandLineFlags(&argc, &argv, true);
  ::google::InitGoogleLogging(argv[0]);
  ::google::InstallFailureSignalHandler();

  return flowthrone::main(argc, argv);
}
