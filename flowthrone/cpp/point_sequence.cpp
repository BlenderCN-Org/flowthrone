#include "point_sequence.h"
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include "glog/logging.h"
#include "utils.h"

namespace flowthrone {

namespace internal {

float NormSquared(const cv::Point2f& a, const cv::Point2f& b) {
  return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

}  // namespace internal

PointSequence::PointSequence(const cv::Point2f& pt, size_t n)
    : PointSequence(n) {
  pts_.push_back(pt);
  ++age_;
}

PointSequence::PointSequence(size_t n) : n_(n) {
  CHECK_GT(n, 0) << "Point sequences' lengths must have strictly positive.";
}

void PointSequence::Add(const cv::Point2f& pt) {
  pts_.push_back(pt);
  ++age_;
  while (pts_.size() > n_) {
    pts_.erase(pts_.begin());
  }
}
int PointSequence::Age() const { return age_; }
const std::vector<cv::Point2f>& PointSequence::Get() const { return pts_; }

const cv::Point2f* PointSequence::Last() const {
  if (pts_.empty()) {
    return nullptr;
  } else {
    return &pts_.back();
  }
}

bool PointSequence::IsValid(const cv::Size& imsize) const {
  constexpr int kMargin = 5;
  if (pts_.empty()) {
    return false;
  }
  const cv::Point2f& pt = pts_.back();
  return pt.x >= kMargin and pt.y <= imsize.width - 1 - kMargin and
         pt.y >= kMargin and pt.y <= imsize.height - 1 - kMargin;
}

void PointSequence::Draw(cv::Mat& image, const PointSequence& traj) {
  if (traj.pts_.empty()) {
    return;
  }

  constexpr int kMaxAge = 50;
  float age_normalized = std::min<float>(kMaxAge, traj.age_) / kMaxAge;

  cv::Scalar colour(0, 255 * (1.0 - age_normalized), 255 * age_normalized);
  for (size_t i = 0; i < traj.pts_.size() - 1; ++i) {
    cv::line(image, traj.pts_[i], traj.pts_[i + 1], colour, 1, CV_AA);
  }
  cv::circle(image, traj.pts_.back(), 2, colour, -1);
}

void PointSequence::Warp(const cv::Mat& flow, PointSequence& traj) {
  const cv::Point2f* last = traj.Last();
  if (!last) {
    return;
  }
  // Warp a single point with flow.
  // TODO: Currently just does the 'nearest neighbor' flow warping, which is
  // stupid and terrible, but easy.
  int x_rounded = std::max(std::min<int>(round(last->x), flow.cols - 1), 0);
  int y_rounded = std::max(std::min<int>(round(last->y), flow.rows - 1), 0);
  const cv::Vec2f& warp = flow.at<cv::Vec2f>(y_rounded, x_rounded);
  traj.Add(cv::Point2f(last->x + warp[0], last->y + warp[1]));
}

namespace internal {

std::vector<std::pair<float, float>> RegularPointGrid(const cv::Size& size,
                                                      int gap) {
  int cols = size.width;
  int rows = size.height;
  int nx = cols / gap;
  int ny = rows / gap;
  CHECK(nx > 0 && ny > 0);
  return Meshgrid(Linspace(0.0f + gap / 2.0, cols - gap / 2.0, nx),
                  Linspace(0.0f + gap / 2.0, rows - gap / 2.0, ny));
}

}  // namespace internal

void PointSequenceSet::Draw(cv::Mat& image,
                            const std::vector<PointSequence>& sequences) {
  for (const PointSequence& sequence : sequences) {
    PointSequence::Draw(image, sequence);
  }
}

void PointSequenceSet::Warp(const cv::Mat& flow,
                            std::vector<PointSequence>& sequences) {
  for (PointSequence& sequence : sequences) {
    PointSequence::Warp(flow, sequence);
  }
}

void PointSequenceSet::RemoveInvalid(const cv::Size& imsize,
                                     std::vector<PointSequence>& sequences) {
  sequences.erase(std::remove_if(sequences.begin(), sequences.end(),
                                 [&imsize](const PointSequence& t) {
                                   return !t.IsValid(imsize);
                                 }),
                  sequences.end());
}

// Returns the sequence whose latest point is closest to the provided point.
bool PointSequenceSet::ExistsWithin(const std::vector<PointSequence>& sequences,
                                    const cv::Point2f& pt, float l2_ball_sq) {
  for (const PointSequence& traj : sequences) {
    const cv::Point2f& last_pt = *CHECK_NOTNULL(traj.Last());
    if (internal::NormSquared(last_pt, pt) < l2_ball_sq) {
      return true;
    }
  }
  return false;
}

void PointSequenceSet::Initialize(const cv::Size& size, int gap,
                                  int sequence_length,
                                  std::vector<PointSequence>& sequences) {
  float gap_sq = gap * gap;
  auto points = internal::RegularPointGrid(size, gap);
  if (sequences.empty()) {
    // Easy case, initialize points from scratch.
    sequences.reserve(points.size());
    for (const std::pair<float, float>& point : points) {
      cv::Point2f pt(point.first, point.second);
      sequences.push_back(PointSequence(pt, sequence_length));
    }
  } else {
    // Add points only in places where they are needed.
    for (const std::pair<float, float>& point : points) {
      cv::Point2f pt(point.first, point.second);
      if (!PointSequenceSet::ExistsWithin(sequences, pt, gap_sq)) {
        sequences.push_back(PointSequence(pt, sequence_length));
      }
    }
  }
}

void PointSequenceSet::RemoveGreedy(int gap,
                                    std::vector<PointSequence>& sequences) {
  // Sort sequences by age, so that we end up keeping older ones.
  auto comparator = [](const PointSequence& x, const PointSequence& y) {
    return x.Age() > y.Age();
  };
  std::sort(sequences.begin(), sequences.end(), comparator);
  float gap_sq = gap * gap;
  for (size_t i = 0; i < sequences.size(); ++i) {
    const cv::Point2f& pt = *CHECK_NOTNULL(sequences[i].Last());
    auto remover = [gap_sq, &pt](const PointSequence& traj) {
      if (traj.Last() == &pt) {  // Don't self-remove.
        return false;
      }
      return internal::NormSquared(*CHECK_NOTNULL(traj.Last()), pt) < gap_sq;
    };
    sequences.erase(std::remove_if(sequences.begin(), sequences.end(), remover),
                    sequences.end());
  }
}

}  // namespace flowthrone
