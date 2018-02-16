#include "point_trajectory.h"
#include "utils.h"
#include "glog/logging.h"
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

namespace flowthrone {

PointTrajectory::PointTrajectory(const cv::Point2f& pt, size_t n)
    : PointTrajectory(n) {
  pts_.push_back(pt);
}

PointTrajectory::PointTrajectory(size_t n) : n_(n) {
  CHECK_GT(n, 0) << "Point trajectories' lengths must have strictly positive.";
}

void PointTrajectory::Add(const cv::Point2f& pt) {
  pts_.push_back(pt);
  while (pts_.size() > n_) {
    pts_.erase(pts_.begin());
  }
}

const std::vector<cv::Point2f>& PointTrajectory::Get() const { return pts_; }

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
  if (traj.pts_.empty()) {
    return;
  }
  // Warp a single point with flow.
  float x = traj.pts_.back().x;
  float y = traj.pts_.back().y;
  // TODO: Currently just does the 'nearest neighbor' flow warping, which is
  // stupid and terrible, but easy.
  int x_rounded = std::max(std::min<int>(round(x), flow.cols - 1), 0);
  int y_rounded = std::max(std::min<int>(round(y), flow.rows - 1), 0);
  const cv::Vec2f& warp = flow.at<cv::Vec2f>(y_rounded, x_rounded);
  traj.Add(cv::Point2f(x + warp[0], y + warp[1]));
}

TrajectorySet TrajectorySet::InitializeRegularGrid(const cv::Size& size,
                                                   int gap,
                                                   int trajectory_length) {
  int cols = size.width;
  int rows = size.height;
  int nx = cols / gap;
  int ny = rows / gap;
  CHECK(nx > 0 && ny > 0);
  auto points = Meshgrid(Linspace(0.0f + gap / 2.0, cols - gap / 2.0, nx),
                         Linspace(0.0f + gap / 2.0, rows - gap / 2.0, ny));
  TrajectorySet set;
  set.trajectories_.reserve(points.size());
  for (auto& pair : points) {
    cv::Point2f pt(pair.first, pair.second);
    set.trajectories_.push_back(PointTrajectory(pt, trajectory_length));
  }
  return set;
}

void TrajectorySet::Draw(cv::Mat& image, const TrajectorySet& set) {
  for (const PointTrajectory& trajectory : set.trajectories_) {
    PointTrajectory::Draw(image, trajectory);
  }
}

void TrajectorySet::Warp(const cv::Mat& flow, TrajectorySet& set) {
  for (PointTrajectory& trajectory : set.trajectories_) {
    PointTrajectory::Warp(flow, trajectory);
  }
}

}  // namespace flowthrone
