#include <opencv2/core/core.hpp>

namespace flowthrone {

// Representation of a 2D point over multiple frames.
class PointSequence {
 public:
  explicit PointSequence(size_t n = 5);
  explicit PointSequence(const cv::Point2f& pt, size_t n = 5);

  // Returns a sequence of points, sorted by age. The most recent point (if
  // it exists) can be accessed by point_sequence.Get().back().
  const std::vector<cv::Point2f>& Get() const;
  // Returns the last (most-recent) point, if any.
  const cv::Point2f* Last() const;
  int Age() const;
  void Add(const cv::Point2f& pt);

  // Returns true if the last point in the sequence exists (!) and is within
  // the provided image boundaries.
  bool IsValid(const cv::Size& imsize) const;

  // Given the point in t-1, warps it into the frame t and adds it to the
  // sequence.
  // This performs a 'backward' warp, even though the 'forward' flow is passed.
  // In other words, the function warps points from the previous frame into
  // the current frame: I_t(x) = I_{t-1}(x-v(x))
  static void Warp(const cv::Mat& flow, PointSequence& traj);

  // Draws the sequence of points on the provided image.
  static void Draw(cv::Mat& image, const PointSequence& traj);

 private:
  std::vector<cv::Point2f> pts_;
  size_t age_ = 0;
  size_t n_ = 5;
};

// Static functions for dealing with a collection of PointSequence objects.
class PointSequenceSet {
 public:
  PointSequenceSet() = delete;
  // Overlays the set of sequences on an image.
  static void Draw(cv::Mat& image, const std::vector<PointSequence>& sequences);

  // Warps the sequences using the optical flow.
  // This performs a 'backward' warp, even though the 'forward' flow is passed.
  // In other words, the function warps points from the previous frame into
  // the current frame: I_t(x) = I_{t-1}(x-v(x))
  static void Warp(const cv::Mat& flow, std::vector<PointSequence>& sequences);

  // Iterates over the set and removes any invalid sequences.
  static void RemoveInvalid(const cv::Size& imsize,
                            std::vector<PointSequence>& sequences);

  // Returns true if there exists a sequence whose latest point is within
  // std::sqrt(l2_ball_sq) of the provided point.
  static bool ExistsWithin(const std::vector<PointSequence>& sequences,
                           const cv::Point2f& pt, float l2_ball_sq);

  // Inserts additional sequences into the current set. Additional
  // sequences are regularly spaced and are added in places where the
  // current set has 'gaps'.
  // If the provided vector is empty, will initialize a regular grid of points.
  static void Initialize(const cv::Size& imsize, int gap, int trajectory_length,
                         std::vector<PointSequence>& sequences);

  // Sorts sequences by age and removes 'younger' sequences that are within
  // 'gap' of some older sequence.
  static void RemoveGreedy(int gap, std::vector<PointSequence>& sequences);
};

}  // namespace flowthrone
