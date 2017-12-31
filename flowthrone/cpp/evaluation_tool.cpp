// Binary can be used to evaluate optical flow on a collection of images.
#include <cstdlib>
#include <chrono>
#include <boost/filesystem.hpp>
#include <gflags/gflags.h>
#include <glog/logging.h>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "evaluation.h"
#include "io.h"
#include "flowthrone.pb.h"
#include "optical_flow_model.h"
#include "visualization.h"

static const std::string gUsageMessage = R"(
Tool for evaluating optical flow on a collection of images.

Example:
./evaluation_tool --eval_input /path/to/evaluation_input.pbtxt
                  --eval_output /path/to/evaluation_results.pbtxt
                  --options /path/to/solver/options.pbtxt
                  --write_images
)";

DEFINE_string(eval_input, "", "EvaluationInput proto filename");
DEFINE_string(eval_output, "output.pbtxt", "EvaluationOutput proto filename");
DEFINE_string(options, "",
              "Filename containing OpticalFlowOptions options (configuration "
              "for optical flow)");
DEFINE_bool(write_images, false,
            "Write intermediate images with results? If set to true, images "
            "will be written to the same directory that --eval_output points "
            "to, with filenames matching the 'identifier's in "
            "EvaluationInput proto.");

using namespace std::chrono;
using boost::filesystem::path;

namespace flowthrone {

namespace {

void LoadTriplet(const EvaluationInput::Datum& datum, cv::Mat* I0, cv::Mat* I1,
                 cv::Mat* flow_gt) {
  constexpr bool kLoadColorImage = true;
  CHECK(datum.has_image0_filename() && datum.has_image1_filename() &&
        datum.has_gt_filename())
      << "You did not specify paths to both images, and to groundtruth. ";

  *I0 = cv::imread(datum.image0_filename(), kLoadColorImage);
  *I1 = cv::imread(datum.image1_filename(), kLoadColorImage);
  *flow_gt = ReadFLO(datum.gt_filename());

  CHECK(I0->total()) << "Could not read from " << datum.image0_filename();
  CHECK(I1->total()) << "Could not read from " << datum.image1_filename();
  CHECK(flow_gt->total()) << "Could not read from " << datum.gt_filename();
}

}  // namespace

int main(int argc, char** argv) {
  CHECK(!FLAGS_eval_input.empty())
      << "You must provide a valid path to the file with evaluation options "
         "(--eval_input argument)";

  EvaluationInput evaluation_config;
  ParseProtoFromFile(FLAGS_eval_input, &evaluation_config);

  std::unique_ptr<OpticalFlowModel> solver =
      OpticalFlowModel::Create(FLAGS_options);

  EvaluationOutput output;
  output.mutable_result()->Reserve(evaluation_config.datum_size());
  for (const auto& datum : evaluation_config.datum()) {
    LOG(INFO) << "Running on: " << datum.identifier();

    cv::Mat I0, I1, flow_gt, predicted_flow;
    LoadTriplet(datum, &I0, &I1, &flow_gt);
    auto t1 = high_resolution_clock::now();
    solver->Run(I0, I1, &predicted_flow);
    auto t2 = high_resolution_clock::now();
    float elapsed = float(duration_cast<nanoseconds>(t2 - t1).count()) / 1e9;

    if (FLAGS_write_images) {
      auto base_output_dir = path(FLAGS_eval_output).remove_filename();
      // Visualization block. Image pair is blended together, while predicted
      // and groundtruth optical flow are visualized in conventional ways.
      // Images are saved in the same directory as the output proto.
      cv::Mat image_blended = 0.5 * I0 + 0.5 * I1;
      cv::Mat flow_vis = ComputeFlowColor(predicted_flow);
      cv::Mat flow_gt_vis = ComputeFlowColor(flow_gt);
      cv::Mat vis = HorizontalConcat(image_blended, flow_vis, flow_gt_vis);
      std::string image_filename =
          (base_output_dir / path(datum.identifier() + ".png")).string();
      LOG(INFO) << "Writing " << image_filename;
      cv::imwrite(image_filename, vis);
    }

    // Perform evaluation.
    EvaluationOutput::Result result;
    result.set_identifier(datum.identifier());
    result.set_average_angular_error(FlowAngularError(predicted_flow, flow_gt));
    result.set_average_endpoint_error(
        FlowEndpointError(predicted_flow, flow_gt));
    result.set_elapsed(elapsed);
    *output.add_result() = result;

    // Calculate average statistics and write results to file.
    // Some flow evaluations may take a REALLY LONG TIME, so it's nicer to
    // write this small proto regularly, rather than waiting until the end.
    *output.mutable_average_summary() = ComputeAverageSummary(output.result());
    WriteProtoToFile(FLAGS_eval_output, output);
    VLOG(1) << "Processed " << output.result_size() << " results. Updated "
            << FLAGS_eval_output;
  }
  LOG(INFO) << "Finished evaluation and wrote: " << FLAGS_eval_output;
  return 0;
}

}  // namespace flowthrone

int main(int argc, char** argv) {
  google::SetUsageMessage(gUsageMessage);
  google::ParseCommandLineFlags(&argc, &argv, true);
  google::InitGoogleLogging(argv[0]);
  google::InstallFailureSignalHandler();
  FLAGS_alsologtostderr = 1;

  return flowthrone::main(argc, argv);
}
