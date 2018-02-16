#include <opencv2/core/core.hpp>

namespace flowthrone {

// Representation of a point over multiple frames.
class PointTrajectory {
 public:
  explicit PointTrajectory(size_t n = 5);
  explicit PointTrajectory(const cv::Point2f& pt, size_t n = 5);

  const std::vector<cv::Point2f>& Get() const;
  const cv::Point2f* Last() const;
  int Age() const;
  void Add(const cv::Point2f& pt);
  bool IsValid(const cv::Size& imsize) const;

  static void Draw(cv::Mat& image, const PointTrajectory& traj);
  static void Warp(const cv::Mat& flow, PointTrajectory& traj);
 private:
  std::vector<cv::Point2f> pts_;
  size_t age_ = 0;
  size_t n_ = 5;
};

// Class that creates a set of point trajectories, manages their death/birth
// events, and propagates them using dense optical flow.
class PointTrajectoryFlow {
 public:
  PointTrajectoryFlow(const cv::Size& size, int gap, int trajectory_length);

  void WarpForward(const cv::Mat& flow);

  const std::vector<PointTrajectory>& Get() const { return trajectories_; }

  void Draw(cv::Mat& image) const;

 private:
  cv::Size size_;
  int gap_;
  int traj_length_;
  std::vector<PointTrajectory> trajectories_;
};

// Static functions for dealing with a collection of PointTrajectory objects.
class TrajectorySet {
 public:
  TrajectorySet() = delete;
  // Overlays the set of trajectories on an image.
  static void Draw(cv::Mat& image,
                   const std::vector<PointTrajectory>& trajectories);

  // Warps the trajectories using the optical flow.
  // This performs a 'backward' warp, even though the 'forward' flow is passed.
  // In other words, the function warps points from the previous frame into
  // the current frame: I_t(x) = I_{t-1}(x-v(x))
  static void Warp(const cv::Mat& flow,
                   std::vector<PointTrajectory>& trajectories);

  // Iterates over the set and removes any invalid trajectories.
  static void RemoveInvalid(const cv::Size& imsize,
                            std::vector<PointTrajectory>& trajectories);

  // Returns true if there exists a trajectory whose latest point is within
  // std::sqrt(l2_ball_sq) of the provided point.
  static bool ExistsWithin(const std::vector<PointTrajectory>& trajectories,
                           const cv::Point2f& pt, float l2_ball_sq);

  // Inserts additional trajectories into the current set. Additional
  // trajectories are regularly spaced and are added in places where the
  // current set has 'gaps'.
  static void Initialize(const cv::Size& imsize, int gap, int trajectory_length,
                         std::vector<PointTrajectory>& trajectories);

  // Sorts trajectories by age and removes 'younger' trajectories.
  static void RemoveGreedy(int gap, std::vector<PointTrajectory>& trajectories);
};

}  // namespace flowthrone
