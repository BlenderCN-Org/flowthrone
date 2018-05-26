#include "optical_flow_tf_model.h"

#include "flow_smoothing.h"
#include "opencv2/imgproc/imgproc.hpp"
#include "optical_flow_tf_internal.h"
#include "tensorflow/cc/saved_model/loader.h"
#include "tensorflow/core/public/session_options.h"
#include "tf_utils.h"
#include "utils.h"

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

}  // namespace

OpticalFlowTensorFlowModel::OpticalFlowTensorFlowModel(
    const OpticalFlowTensorFlowModelOptions& opts)
    : opts_(opts) {
  const std::string kModelTag = "train";
  context_ = internal::Context::CreateFromSavedModel(opts, opts_.export_dir(),
                                                     kModelTag);
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

  cv::Mat output_flow = cv::Mat(I0.size(), CV_32FC2, cv::Scalar(0.0f));
  if (!opts_.sliding_window()) {
    context_->RunInference(I0, I1, &output_flow);
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
      cv::Mat flow_patch;
      context_->RunInference(I0_patch, I1_patch, &flow_patch);

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

  Postprocess(I0_in, I1_in, &output_flow);
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
    *flow = DenoiseColorWeightedFilter(*flow, I0_in, dn_opts);
  }
}

}  // namespace flowthrone
