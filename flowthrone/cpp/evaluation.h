// Utilities for evaluating quality of optical flow.
// For details, see "A Database and Evaluation Methodology for Optical Flow"
// S. Baker, D. Scharstein, J.P. Lewis, S. Roth, M. Black, R. Szelinski,
// ICCV 2007.
#pragma once
#include <opencv2/core/core.hpp>
#include <google/protobuf/repeated_field.h>
#include "flowthrone.pb.h"

namespace flowthrone {

// Returns average endpoint error, calculated as:
//   \frac{1}{N} \sum || (u,v) - (u_gt, v_gt) ||_2
// where N is the number of pixels in the image.
// Optionally can fill 'flow_error'. Input images must be CV_32FC2, and if
// specified, 'flow_error' will be CV_32FC1.
float FlowEndpointError(const cv::Mat& flow, const cv::Mat& flow_gt,
                        cv::Mat* flow_error = nullptr);

// Returns average angular error, calculated as:
//   X = (u, v, 1), Y = (u_gt, v_gt, 1)
//   \frac{1}{N} \sum acos( X^T Y / ||X|| ||Y|| )
// where N is the number of pixels in the image.
// Optionally can fill 'flow_error'. Input images must be CV_32FC2, and if
// specified, 'flow_error' will be CV_32FC1.
float FlowAngularError(const cv::Mat& flow, const cv::Mat& flow_gt,
                       cv::Mat* flow_error = nullptr);

// Given a collection of results for each image pair, computes average summary
// statistics.
EvaluationOutput::Result ComputeAverageSummary(
    const google::protobuf::RepeatedPtrField<EvaluationOutput::Result>&
        results);

// Given a collection of results for each image pair, computes several
// percentile values.
google::protobuf::Map<int, EvaluationOutput::Result> ComputePercentileSummary(
    const google::protobuf::RepeatedPtrField<EvaluationOutput::Result>& results,
    const std::vector<int>& percentiles);

}  // namespace flowthrone
