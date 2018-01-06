// Tool for running and visualizing optical flow. You can either provide a pair
// of images (--img1, --img2), or a video (--video).
// When --visualize flag is added, each output will be shown to the user;
// otherwise, you may provide --output_image or --output_video flags.
// Example:
//   ./optical_flow_main --video /tmp/input.mp4 --output_video /tmp/flow.avi
//
#include <memory>
#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "gflags/gflags.h"
#include "glog/logging.h"
#include "visualization.h"
#include "io.h"
#include "optical_flow_model.h"

static const std::string gUsageMessage = R"(
Tool for running and visualizing optical flow.
You can either provide a pair of images (using '--img1', '--img2' flags), or a
video (using '--video' flag).
When '--visualize' flag is added, each frame's output will be shown to the
user; otherwise, you may provide '--output_image' or '--output_video' flags to
write images or video, respectively.
Example:
  ./optical_flow_tool --video /tmp/input.mp4 --output_video /tmp/flow.avi
)";

DEFINE_string(video, "", "Path to a video file.");
DEFINE_string(img1, "", "Filename of image1");
DEFINE_string(img2, "", "Filename of image2");
DEFINE_string(output, "", "Output image or video filename");
DEFINE_bool(visualize, false,
            "Whether the results should be visualized or not.");
DEFINE_bool(more, false,
            "Whether to visualize even more artifacts. This is inactive "
            "unless '--visualize' is on");
DEFINE_string(options, "",
              "Filename containing OpticalFlowOptions options (configuration "
              "for optical flow)");

namespace flowthrone {

// Abstraction over a pair of images, or a video sequence.
class Feeder {
 public:
  virtual bool next(cv::Mat* output) = 0;
  static std::unique_ptr<Feeder> Create();
};

int main(int argc, char** argv) {
  std::unique_ptr<OpticalFlowModel> model =
      OpticalFlowModel::Create(FLAGS_options);

  std::unique_ptr<Feeder> data_feeder = Feeder::Create();
  std::vector<cv::Mat> images(2);
  CHECK(data_feeder->next(&images[1])) << "Could not read first image.";

  std::unique_ptr<cv::VideoWriter> video_writer;
  if (!FLAGS_output.empty() && dynamic_cast<VideoFeeder>(data_feeder)) {
    int fourcc = CV_FOURCC('M', 'P', '4', '2');
    int fps = 30;
    cv::Size sz(images[1].cols * 2, images[1].rows);
    video_writer.reset(
        new cv::VideoWriter(FLAGS_output, fourcc, fps, sz));
    CHECK(video_writer->isOpened())
        << "Could not successfully open video for writing "
        << FLAGS_output;
  }

  while (true) {
    // Push the old image to the 'back' of the queue, and fill in latest image.
    std::swap(images[0], images[1]);
    images[1] = cv::Mat();

    if (!data_feeder->next(&images[1]) || (images[1].total() == 0)) {
      LOG(INFO) << "No more images left!";
      break;
    } else {
      LOG(INFO) << "Computing flow.";
    }
    cv::Mat predicted_flow;
    model->Run(images[0], images[1], &predicted_flow);

    // Visualizations/output.
    cv::Mat vis = VisualizeTuple(images[0], images[1], predicted_flow);
    if (FLAGS_visualize) {
      if (FLAGS_more) {
        // Show warped points in the two images.
        cv::Mat I0_vis, I1_vis;
        std::tie(I0_vis, I1_vis) =
            OverlayWarpedPoints(images[0], images[1], predicted_flow);
        cv::imshow("warped_points", HorizontalConcat(I0_vis, I1_vis));
      }
      cv::imshow("image", vis);
      cv::waitKey(0);
    }
    if (!FLAGS_output.empty()) {
      if (video_writer) {
        video_writer->write(vis);
        LOG(INFO) << "Added a frame to output video.";
      } else {
        cv::imwrite(FLAGS_output_image, vis);
        LOG(INFO) << "Wrote " << FLAGS_output;
      }
    }
  }
  return 0;
}

class VideoFeeder : public Feeder {
 public:
  VideoFeeder() {
    video_.open(FLAGS_video);
    CHECK(video_.isOpened()) << "Could not open " << FLAGS_video;
  }
  bool next(cv::Mat* output) override {
    cv::Mat img;
    video_.grab();
    bool success = video_.retrieve(img);
    cv::resize(img, img, cv::Size(), 0.5, 0.5);
    *output = img;
    return success;
  }

 private:
  cv::VideoCapture video_;
};

class ImageFeeder : public Feeder {
 public:
  ImageFeeder() {
    for (const std::string& fn : {FLAGS_img1, FLAGS_img2}) {
      images_.push_back(cv::imread(fn));
      CHECK(images_.back().total())
          << "Failed reading image '" << fn
          << "' maybe the file does not exist, or is not an image?";
    }
  }
  bool next(cv::Mat* output) override {
    if (index_ >= 2) {
      return false;
    }
    *output = images_[index_].clone();
    index_++;
    return true;
  }

 private:
  std::vector<cv::Mat> images_;
  int index_ = 0;
};

std::unique_ptr<Feeder> Feeder::Create() {
  bool have_video_fn =
      !FLAGS_video.empty() && (FLAGS_img1.empty() && FLAGS_img2.empty());
  bool have_image_fns =
      FLAGS_video.empty() && (!FLAGS_img1.empty() && !FLAGS_img2.empty());
  if (have_video_fn) {
    return std::unique_ptr<Feeder>(new VideoFeeder);
  } else if (have_image_fns) {
    return std::unique_ptr<Feeder>(new ImageFeeder);
  } else {
    LOG(FATAL)
        << "You must either specify the video filename (--video) or a pair of "
           "images (--img1, --img2) that should be processed. "
           "It is not acceptable to specify both --video and --img1/--img2 or "
           "neither.\n"
           "For help, consider running './optical_flow_main --helpshort ";
    return nullptr;
  }
}

}  // namespace flowthrone

int main(int argc, char** argv) {
  ::gflags::SetUsageMessage(gUsageMessage);
  ::gflags::ParseCommandLineFlags(&argc, &argv, true);
  ::google::InitGoogleLogging(argv[0]);
  ::google::InstallFailureSignalHandler();
  FLAGS_alsologtostderr = 1;
  return flowthrone::main(argc, argv);
}
