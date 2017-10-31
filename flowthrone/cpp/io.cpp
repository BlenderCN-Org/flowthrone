#include "io.h"
#include "glog/logging.h"

namespace flowthrone {

cv::Mat ReadFLO(const std::string &filename) {
  constexpr float TAG_FLOAT = 202021.25;  // Check this when reading the file.
  FILE *fid = CHECK_NOTNULL(fopen(filename.c_str(), "rb"));
  int width, height;
  float tag;
  CHECK_EQ(1, fread(&tag, sizeof(float), 1, fid));
  CHECK_EQ(1, fread(&width, sizeof(int), 1, fid));
  CHECK_EQ(1, fread(&height, sizeof(int), 1, fid));
  CHECK_EQ(TAG_FLOAT, tag);
  CHECK(1 < width && width < 100000);
  CHECK(1 < height && height < 100000);

  cv::Mat image(height, width, CV_32FC2);
  for (int r = 0; r < height; ++r) {
    float *ptr = image.ptr<float>(r);
    CHECK_EQ(2 * width, fread(ptr, sizeof(float), 2 * width, fid));
    for (int c = 0; c < 2 * width; c+=2) {
      // Values greater than 1e9 (either |u| or |v|) is considered to be
      // unknown and set to 'nan'.
      // Typically, these values are occluded pixels in groundtruth datasets.
      if (std::abs(ptr[c]) > 1e9 or std::abs(ptr[c+1]) > 1e9) {
        ptr[c] = nanf("");
        ptr[c+1] = nanf("");
      }
    }
  }
  fclose(fid);
  return image;
}

void WriteFLO(const std::string &filename, const cv::Mat &flow) {
  constexpr const char *TAG_STRING = "PIEH";
  CHECK_EQ(CV_32FC2, flow.type()) << "Must be CV_32FC2";

  int rows = flow.rows;
  int cols = flow.cols;
  FILE *fid = CHECK_NOTNULL(fopen(filename.c_str(), "wb"));
  fprintf(fid, TAG_STRING);
  CHECK_EQ(1, fwrite(&cols, sizeof(int), 1, fid));
  CHECK_EQ(1, fwrite(&rows, sizeof(int), 1, fid));
  for (int r = 0; r < rows; ++r) {
    const float *ptr = flow.ptr<float>(r);
    CHECK_EQ(2 * cols, fwrite(ptr, sizeof(float), 2 * cols, fid));
  }
  fclose(fid);
}

}  // namespace flowthrone
