import cv2
import tensorflow as tf
import os
import unittest
import tf_utils
import numpy as np 

class TestWarpWithFlow(unittest.TestCase):
  image = None
  uv = None
  n = 3
  rows = 4
  cols = 8
  tolerance = 1e-3

  def setUp(self):
    self.image = tf.convert_to_tensor(
            np.random.uniform(0, 1, [self.n, self.rows, self.cols, 3]), 
            dtype=tf.float32)
    self.uv = tf.constant(2.0, tf.float32, [self.n, self.rows, self.cols, 2])

  """ Verifies that we can correctly produce a trivial sampling grid. """
  def test_flow_grid(self):
    session = tf.Session()
    identity_uv = tf.constant(0.0, tf.float32, [self.n, self.rows, self.cols, 2])
    grid = tf_utils._get_flow_grid(identity_uv)

    with session.as_default(): 
      tf_grid = grid.eval()
      np_grid = np.stack(np.meshgrid(range(self.cols), range(self.rows)), axis=2)
      error = np.linalg.norm(tf_grid - np_grid)
      self.assertLessEqual(error, self.tolerance)

  """ Verifies a trivial case of get_pixel_values (queried points is the
      grid itself). """
  def test_get_image_values(self):
    identity_uv = tf.constant(0.0, tf.float32, [self.n, self.rows, self.cols, 2])
    grid = tf_utils._get_flow_grid(identity_uv)

    image_samples = tf_utils._get_pixel_values(
            self.image, grid[:,:,:,0], grid[:,:,:,1])

    session = tf.Session()
    with session.as_default():
      image_samples_values = image_samples.eval()
      image_values = self.image.eval()
      error = np.linalg.norm(image_values - image_samples_values)
      self.assertLessEqual(error, self.tolerance)

  """ Verifies that identity warp is correct. """
  def test_warp_with_flow_identity(self):
    identity_uv = tf.constant(0.0, tf.float32, [self.n, self.rows, self.cols, 2])
    
    image_warped = tf_utils.warp_with_flow(self.image, identity_uv)
    session = tf.Session()
    with session.as_default():
      warped_image_values = image_warped.eval()
      image_values = self.image.eval()
      error = np.linalg.norm(image_values - warped_image_values)
      self.assertLessEqual(error, self.tolerance)
   
    
  """ Verifies that a simple constant 1-pixel shift works correctly. """
  def test_warp_with_nonzero_flow(self):
    image = np.zeros([self.n, self.rows, self.cols, 1])
    image[0, 2, 2:5, 0] = 1
    warped_image_gt = np.zeros([self.n, self.rows, self.cols, 1])
    warped_image_gt[0, 2, 1:4, 0] = 1

    self.image = tf.convert_to_tensor(image, dtype=tf.float32)
    # Horizontal 1 pixel shift.
    uv = np.zeros([self.n, self.rows, self.cols, 2])
    uv[:,:,:,0] = 1
    uv[:,:,:,1] = 0
    uv = tf.convert_to_tensor(uv, dtype=tf.float32)

    image_warped = tf_utils.warp_with_flow(self.image, uv)
    session = tf.Session()
    with session.as_default():
      warped_image_values = image_warped.eval()
      error = np.linalg.norm(warped_image_gt - warped_image_values)
      self.assertLessEqual(error, self.tolerance)
 


if __name__ == '__main__':
  # There is absolutely no reason to use GPU for these tests, and this
  # appears to be the most reliable way to disable GPU usage in tensorflow.
  os.environ['CUDA_VISIBLE_DEVICES'] = ''
  unittest.main(verbosity=2)

