#include "point_trajectory.h"
#include "utils.h"
#include "glog/logging.h"
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

namespace flowthrone {

namespace internal {

float NormSquared(const cv::Point2f& a, const cv::Point2f& b) {
  return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}

}  // namespace internal

PointTrajectory::PointTrajectory(const cv::Point2f& pt, size_t n)
    : PointTrajectory(n) {
  pts_.push_back(pt);
  ++age_;
}

PointTrajectory::PointTrajectory(size_t n) : n_(n) {
  CHECK_GT(n, 0) << "Point trajectories' lengths must have strictly positive.";
}

void PointTrajectory::Add(const cv::Point2f& pt) {
  pts_.push_back(pt);
  ++age_;
  while (pts_.size() > n_) {
    pts_.erase(pts_.begin());
  }
}

const std::vector<cv::Point2f>& PointTrajectory::Get() const { return pts_; }

const cv::Point2f* PointTrajectory::Last() const {
  if (pts_.empty()) {
    return nullptr;
  } else {
    return &pts_.back();
  }
}

bool PointTrajectory::IsValid(const cv::Size& imsize) const {
  constexpr int kMargin = 5;
  if (pts_.empty()) {
    return false;
  }
  const cv::Point2f& pt = pts_.back();
  return pt.x >= kMargin and pt.y <= imsize.width - 1 - kMargin and
         pt.y >= kMargin and pt.y <= imsize.height - 1 - kMargin;
}

void PointTrajectory::Draw(cv::Mat& image, const PointTrajectory& traj) {
  if (traj.pts_.empty()) {
    return;
  }
  cv::Scalar colour(0, 200, 0);
  for (size_t i = 0; i < traj.pts_.size() - 1; ++i) {
    cv::line(image, traj.pts_[i], traj.pts_[i + 1], colour, 1, CV_AA);
  }
  cv::circle(image, traj.pts_.back(), 2, colour, -1);
}

void PointTrajectory::Warp(const cv::Mat& flow, PointTrajectory& traj) {
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

void TrajectorySet::Draw(cv::Mat& image,
                         const std::vector<PointTrajectory>& trajectories) {
  for (const PointTrajectory& trajectory : trajectories) {
    PointTrajectory::Draw(image, trajectory);
  }
}

void TrajectorySet::Warp(const cv::Mat& flow,
                         std::vector<PointTrajectory>& trajectories) {
  for (PointTrajectory& trajectory : trajectories) {
    PointTrajectory::Warp(flow, trajectory);
  }
}

void TrajectorySet::RemoveInvalid(const cv::Size& imsize,
                                  std::vector<PointTrajectory>& trajectories) {
  trajectories.erase(std::remove_if(trajectories.begin(), trajectories.end(),
                                    [&imsize](const PointTrajectory& t) {
                                      return !t.IsValid(imsize);
                                    }),
                     trajectories.end());
}

// Returns the trajectory whose latest point is closest to the provided point.
bool TrajectorySet::ExistsWithin(
    const std::vector<PointTrajectory>& trajectories, const cv::Point2f& pt,
    float l2_ball_sq) {
  for (const PointTrajectory& traj : trajectories) {
    const cv::Point2f& last_pt = *CHECK_NOTNULL(traj.Last());
    if (internal::NormSquared(last_pt, pt) < l2_ball_sq) {
      return true;
    }
  }
  return false;
}

void TrajectorySet::Initialize(const cv::Size& size, int gap,
                               int trajectory_length,
                               std::vector<PointTrajectory>& trajectories) {
  float gap_sq = gap * gap;
  auto points = internal::RegularPointGrid(size, gap);
  if (trajectories.empty()) {
    // Easy case, initialize points from scratch.
    trajectories.reserve(points.size());
    for (const std::pair<float, float>& point : points) {
      cv::Point2f pt(point.first, point.second);
      trajectories.push_back(PointTrajectory(pt, trajectory_length));
    }
  } else {
    // Add points only in places where they are needed.
    for (const std::pair<float, float>& point : points) {
      cv::Point2f pt(point.first, point.second);
      if (!TrajectorySet::ExistsWithin(trajectories, pt, gap_sq)) {
        trajectories.push_back(PointTrajectory(pt, trajectory_length));
      }
    }
  }
}

void TrajectorySet::RemoveGreedy(int gap,
                                 std::vector<PointTrajectory>& trajectories) {
  float gap_sq = gap * gap;
  for (size_t i = 0; i < trajectories.size(); ++i) {
    const cv::Point2f& pt = *CHECK_NOTNULL(trajectories[i].Last());
    auto remover = [gap_sq, &pt](const PointTrajectory& traj) {
      if (traj.Last() == &pt) {  // Don't self-remove.
        return false;
      }
      return internal::NormSquared(*CHECK_NOTNULL(traj.Last()), pt) < gap_sq;
    };
    trajectories.erase(
        std::remove_if(trajectories.begin(), trajectories.end(), remover),
        trajectories.end());
  }
}

PointTrajectoryFlow::PointTrajectoryFlow(const cv::Size& size, int gap,
                                         int trajectory_length)
    : size_(size), gap_(gap), traj_length_(trajectory_length) {
  TrajectorySet::Initialize(size_, gap_, traj_length_, trajectories_);
}

void PointTrajectoryFlow::WarpForward(const cv::Mat& flow) {
  TrajectorySet::RemoveInvalid(size_, trajectories_);
  TrajectorySet::RemoveGreedy(gap_, trajectories_);
  TrajectorySet::Warp(flow, trajectories_);
  TrajectorySet::Initialize(size_, gap_, traj_length_, trajectories_);
}

void PointTrajectoryFlow::Draw(cv::Mat& image) const {
  TrajectorySet::Draw(image, trajectories_);
}

}  // namespace flowthrone
