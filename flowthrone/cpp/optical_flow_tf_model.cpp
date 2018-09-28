#include "optical_flow_tf_model.h"

#include "glog/logging.h"
#include "opencv2/imgproc/imgproc.hpp"

#include "flow_smoothing.h"
#include "optical_flow_tf_internal.h"
#include "tf_utils.h"
#include "utils.h"

#include "opencv2/highgui/highgui.hpp"
#include "visualization.h"

namespace tf = tensorflow;

namespace flowthrone {
using internal::Context;
using Result = OpticalFlowModel::Result;

namespace {

// Converts a cv::Mat to float or returns its shallow copy.
cv::Mat MaybeConvertTo32F(const cv::Mat& x) {
  if (x.depth() == CV_32F) {
    return x;
  } else {
    cv::Mat y;
    x.convertTo(y, CV_32F);
    return y;
  }
}

void CheckNumberOfChannels(const cv::Mat& x, int expected_channels) {
  CHECK_EQ(x.channels(), expected_channels)
      << "Number of channels in the provided image does not match the "
         "expected number of channels.";
}

void CheckOutputSizeIsConsistent(const cv::Mat& I, const cv::Mat& flow) {
  LOG_IF(FATAL, I.rows != flow.rows || I.cols != flow.cols)
      << "Dimensions of the output flow field and input image do not match. "
         "Image dimensions are "
      << I.size() << " but output flow is: " << flow.size();
}

}  // namespace

OpticalFlowTensorFlowModel::OpticalFlowTensorFlowModel(
    const OpticalFlowTensorFlowModelOptions& opts)
    : opts_(opts) {
  LOG_IF(FATAL, !(opts_.has_export_dir() ^ opts_.has_frozen_graph_filename()))
      << "Neither 'export_dir' not 'frozen_graph_filename' has been specified "
         "in options, so the network can't be created. Specify one and exactly "
         "one of the two fields.";
  if (opts_.has_export_dir()) {
    const std::string kModelTag = "train";
    context_ = internal::Context::CreateFromSavedModel(opts, opts_.export_dir(),
                                                       kModelTag);
  } else if (opts_.has_frozen_graph_filename()) {
    context_ = internal::Context::CreateFromFrozenGraph(
        opts, opts_.frozen_graph_filename());
  }
  CHECK(context_);
}

OpticalFlowTensorFlowModel::~OpticalFlowTensorFlowModel() {}

Result OpticalFlowTensorFlowModel::Run(const cv::Mat& I0_in,
                                       const cv::Mat& I1_in) {
  CheckNumberOfChannels(I0_in, context_->input_shape.dim_size(2));
  CheckNumberOfChannels(I1_in, context_->input_shape.dim_size(2));
  cv::Mat I0, I1;
  // Convert inputs to float if necessary. Newer models shall take in uint8
  // as inputs, but for backward compatibility float inputs are supported too.
  if (context_->inputs_are_uint8) {
    I0 = I0_in;
    I1 = I1_in;
  } else {
    I0 = MaybeConvertTo32F(I0_in);
    I1 = MaybeConvertTo32F(I1_in);
  }

  if (opts_.image_resize_factor() != 1.0) {
    const float scale = opts_.image_resize_factor();
    cv::resize(I0_in, I0, cv::Size(), scale, scale);
    cv::resize(I1_in, I1, cv::Size(), scale, scale);
  }

  cv::Mat output_flow = cv::Mat(I0.size(), CV_32FC2, cv::Scalar(0.0f));
  if (!NeedSlidingWindow(I0.size())) {
    std::vector<cv::Mat> net_outputs;
    context_->RunInference(I0, I1, &net_outputs);
    CHECK_LE(1, net_outputs.size());
    output_flow = net_outputs[0];
  } else {
    // Doesn't __really__ need to be the case.
    cv::Size patch_sz = context_->input_size;

    int stride_x = patch_sz.width * opts_.window_stride();
    int stride_y = patch_sz.height * opts_.window_stride();
    std::vector<cv::Rect> patch_locations =
        SplitImage(I0.size(), patch_sz, cv::Size(stride_x, stride_y),
                   SplitImageMode::kSizeConstant);

    cv::Mat counts = cv::Mat(I0.size(), CV_32FC1, cv::Scalar(0));
    cv::Mat kernel = SquaredExponentialKernel(patch_sz);

    for (const auto& rect : patch_locations) {
      // At the boundaries, rect.size() != patch_sz, so the patch (and the
      // kernel) may need to be resized even if patch_sz == network input size.
      cv::Mat I0_patch = I0(rect);
      cv::Mat I1_patch = I1(rect);
      std::vector<cv::Mat> net_outputs;
      context_->RunInference(I0_patch, I1_patch, &net_outputs);
      CHECK_EQ(1, net_outputs.size());
      cv::Mat flow_patch = net_outputs[0];

      cv::Mat this_kernel;
      cv::resize(kernel, this_kernel, rect.size());
      cv::Mat kernel_32fc2;
      cv::merge(std::vector<cv::Mat>{this_kernel, this_kernel}, kernel_32fc2);
      cv::multiply(flow_patch, kernel_32fc2, flow_patch);
      cv::add(output_flow(rect), flow_patch, output_flow(rect));
      cv::add(counts(rect), this_kernel, counts(rect));
    }
    cv::Mat counts_32fc2;
    cv::merge(std::vector<cv::Mat>{counts, counts}, counts_32fc2);
    output_flow = output_flow / counts_32fc2;
  }

  Postprocess(I0, I1, &output_flow);

  if (opts_.image_resize_factor() != 1.0) {
    // Apply the inverse of the transformation applied previously.
    const cv::Size target_size(output_flow.cols / opts_.image_resize_factor(),
                               output_flow.rows / opts_.image_resize_factor());
    output_flow = ResampleFlow(output_flow, target_size);
  }

  CheckOutputSizeIsConsistent(I0_in, output_flow);
  CheckOutputSizeIsConsistent(I1_in, output_flow);

  Result result;
  result.flow = std::move(output_flow);
  return result;
}

void OpticalFlowTensorFlowModel::Postprocess(const cv::Mat& I0_in,
                                             const cv::Mat& I1_in,
                                             cv::Mat* flow) {
  if (opts_.has_denoising_options()) {
    DenoisingOptions dn_opts;
    dn_opts.sigma_intensity = opts_.denoising_options().sigma_intensity();
    dn_opts.sigma_distance = opts_.denoising_options().sigma_distance();
    dn_opts.window_size = opts_.denoising_options().window_size();
    if (opts_.denoising_options().use_probability_of_occlusion()) {
      cv::Mat I0_in_gray, I1_in_gray, I0f_gray, I1f_gray;
      cv::cvtColor(I0_in, I0_in_gray, CV_BGR2GRAY);
      cv::cvtColor(I1_in, I1_in_gray, CV_BGR2GRAY);
      I0_in_gray.convertTo(I0f_gray, CV_32FC1);
      I1_in_gray.convertTo(I1f_gray, CV_32FC1);

      float sigma_d = 0.5;
      float sigma_i = 128.0;
      cv::Mat p_occl =
          ProbabilityOfOcclusion(I0f_gray, I1f_gray, *flow, sigma_d, sigma_i);
      *flow = DenoiseColorWeightedFilter(*flow, I0f_gray, p_occl, dn_opts);
    } else {
      cv::Mat I0_in_gray, I0f_gray;
      cv::cvtColor(I0_in, I0_in_gray, CV_BGR2GRAY);
      I0_in_gray.convertTo(I0f_gray, CV_32FC1);
      *flow = DenoiseColorWeightedFilter(*flow, I0f_gray, dn_opts);
    }
  }
}

bool OpticalFlowTensorFlowModel::NeedSlidingWindow(const cv::Size& sz) {
  // Returns 'true' only if the options are set to true, and the passed size
  // is larger than the network input dimensions.
  if (!opts_.sliding_window()) {
    return false;
  }
  if (sz.height < context_->input_shape.dim_size(0) ||
      sz.width < context_->input_shape.dim_size(1)) {
    LOG_FIRST_N(WARNING, 1)
        << "Your options indicated that you would like to run network "
           "in a 'sliding window' fashion, but the image is strictly "
           "smaller than the network input dimensions, so inference "
           "will be performed in 'one-shot', without 'sliding "
           "window'. If you _really_ insist on doing a sliding "
           "window, consider resizing (upscaling) inputs. Image dimensions "
           "were "
        << sz.height << "x" << sz.width << " and network input dimensions are: "
        << context_->input_shape.DebugString();
    return false;
  }
  return true;
}

}  // namespace flowthrone
