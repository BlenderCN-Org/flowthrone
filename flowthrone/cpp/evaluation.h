// Utilities for evaluating quality of optical flow.
// For details, see "A Database and Evaluation Methodology for Optical Flow"
// S. Baker, D. Scharstein, J.P. Lewis, S. Roth, M. Black, R. Szelinski,
// ICCV 2007.
#pragma once
#include <google/protobuf/repeated_field.h>
#include <opencv2/core/core.hpp>
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

// Returns a vector of average errors for a set of displacement intervals.
// As an example, for an interval [0, \infty), the function will simply return
// the average error; for an interval [0, 1) will return the average error for
// regions whose velocity (displacement) norm is <1, and so on.
// Precisely, for an interval [a, b), the corresponding returned value is
//  pred(x) =  1 if flow_gt(x) \in [a, b), 0 else
//  output = \sum_x pred(x) error(x) / \sum_x pred(x)
std::vector<float> AverageErrorByInterval(
    const cv::Mat& flow_gt, const cv::Mat& error,
    const google::protobuf::RepeatedPtrField<Interval>& intervals);

// Given a collection of results for each image pair, computes average summary
// statistics.
EvaluationOutput::Result ComputeAverageSummary(
    const google::protobuf::RepeatedPtrField<EvaluationOutput::Result>&
        results);

// Given a collection of results for each image pair, computes several
// percentile values.
google::protobuf::Map<int, EvaluationOutput::Result> ComputePercentileSummary(
    const google::protobuf::RepeatedPtrField<EvaluationOutput::Result>& results,
    const google::protobuf::RepeatedField<int>& percentiles);

// Returns a proto with performance statistics (endpoint/angular errors)
// for a given prediction/groundtruth pair.
EvaluationOutput::Result Evaluate(const cv::Mat& prediction,
                                  const cv::Mat& groundtruth,
                                  const EvaluationInput::Options& options);

// Returns the default set of evaluation options.
EvaluationInput::Options GetDefaultEvaluationOptions();

}  // namespace flowthrone
