#pragma once
#include <cstdlib>
#include <opencv2/core/core.hpp>

namespace flowthrone {

// Read a binary 'flo' file into a cv::Mat.
// WARNING: Returned image may contain NaNs, which correspond to 'unknown'
// flow values (e.g. occluded regions).
cv::Mat ReadFLO(const std::string& filename);

// Write cv::Mat into a binary 'flo' file.
void WriteFLO(const std::string& filename, const cv::Mat& flow);

}  // namespace flowthrone
