#pragma once
#include <cstdlib>
#include <opencv2/core/core.hpp>

namespace flowthrone {

// Returns a random flow image, of a given size.
cv::Mat GetRandomFlow(int rows, int cols);

}  // namespace flowthrone
