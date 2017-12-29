#pragma once
#include <cstdlib>
#include <opencv2/core/core.hpp>
#include <google/protobuf/message.h>

namespace flowthrone {

// Read a binary 'flo' file into a cv::Mat.
// WARNING: Returned image may contain NaNs, which correspond to 'unknown'
// flow values (e.g. occluded regions).
cv::Mat ReadFLO(const std::string& filename);

// Write cv::Mat into a binary 'flo' file.
void WriteFLO(const std::string& filename, const cv::Mat& flow);

// Return file contents as a string.
std::string ReadFile(const std::string& filename);

// Write string to a file. If file already exists, it is overwritten.
void WriteFile(const std::string& filename, const std::string& contents);

// Reads proto from file.
void ParseProtoFromFile(const std::string& filename,
                        google::protobuf::Message* message);

// Writes proto in text format or binary to file.
// If file already exists, it is overwritten.
void WriteProtoToFile(const std::string& filename,
                      const google::protobuf::Message& message,
                      bool as_text_format = true);

}  // namespace flowthrone
