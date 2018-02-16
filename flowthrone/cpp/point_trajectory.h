#include <opencv2/core/core.hpp>

namespace flowthrone {

class PointTrajectory {
public:
  explicit PointTrajectory(size_t n=5);
  explicit PointTrajectory(const cv::Point2f& pt, size_t n=5);

  void Add(const cv::Point2f& pt);
  const std::vector<cv::Point2f>& Get() const;


  static void Draw(cv::Mat& image, const PointTrajectory& traj);
  static void Warp(const cv::Mat& flow, PointTrajectory& traj);
private:
  std::vector<cv::Point2f> pts_;
  size_t n_;
};

class TrajectorySet {
public:
  const std::vector<PointTrajectory>& Get() const {
    return trajectories_;  
  }
  std::vector<PointTrajectory>& Get() {
    return trajectories_;  
  }

  static TrajectorySet InitializeRegularGrid(const cv::Size& size, int gap, int trajectory_length);
  static void Draw(cv::Mat& image, const TrajectorySet& set);
  
  static void Warp(const cv::Mat& flow, TrajectorySet& set);
private:
  std::vector<PointTrajectory> trajectories_;
};

} // namespace flowthrone
