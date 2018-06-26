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
        self.uv = tf.constant(2.0, tf.float32,
                              [self.n, self.rows, self.cols, 2])

    def test_flow_grid(self):
        """ Verifies that we can correctly produce a trivial sampling grid. """
        session = tf.Session()
        identity_uv = tf.constant(0.0, tf.float32,
                                  [self.n, self.rows, self.cols, 2])
        grid = tf_utils._get_flow_grid(identity_uv)

        with session.as_default():
            tf_grid = grid.eval()
            np_grid = np.stack(
                np.meshgrid(range(self.cols), range(self.rows)), axis=2)
            error = np.linalg.norm(tf_grid - np_grid)
            self.assertLessEqual(error, self.tolerance)

    def test_get_image_values(self):
        """
        Verifies a trivial case of get_pixel_values (queried points is the
        grid itself).
        """
        identity_uv = tf.constant(0.0, tf.float32,
                                  [self.n, self.rows, self.cols, 2])
        grid = tf_utils._get_flow_grid(identity_uv)

        image_samples = tf_utils._get_pixel_values(
            self.image, grid[:, :, :, 0], grid[:, :, :, 1])

        session = tf.Session()
        with session.as_default():
            image_samples_values = image_samples.eval()
            image_values = self.image.eval()
            error = np.linalg.norm(image_values - image_samples_values)
            self.assertLessEqual(error, self.tolerance)

    def test_warp_with_flow_identity(self):
        """ Verifies that identity warp is correct. """
        identity_uv = tf.constant(0.0, tf.float32,
                                  [self.n, self.rows, self.cols, 2])

        image_warped = tf_utils.warp_with_flow(self.image, identity_uv)
        session = tf.Session()
        with session.as_default():
            warped_image_values = image_warped.eval()
            image_values = self.image.eval()
            error = np.linalg.norm(image_values - warped_image_values)
            self.assertLessEqual(error, self.tolerance)

    def test_warp_with_nonzero_flow(self):
        """ Verifies that a simple constant 1-pixel shift works correctly. """
        image = np.zeros([self.n, self.rows, self.cols, 1])
        image[0, 2, 2:5, 0] = 1
        warped_image_gt = np.zeros([self.n, self.rows, self.cols, 1])
        warped_image_gt[0, 2, 1:4, 0] = 1

        self.image = tf.convert_to_tensor(image, dtype=tf.float32)
        # Horizontal 1 pixel shift.
        uv = np.zeros([self.n, self.rows, self.cols, 2])
        uv[:, :, :, 0] = 1
        uv[:, :, :, 1] = 0
        uv = tf.convert_to_tensor(uv, dtype=tf.float32)

        image_warped = tf_utils.warp_with_flow(self.image, uv)
        session = tf.Session()
        with session.as_default():
            warped_image_values = image_warped.eval()
            error = np.linalg.norm(warped_image_gt - warped_image_values)
            self.assertLessEqual(error, self.tolerance)


class TestCorrelationLayer(unittest.TestCase):

    def test_correlation_layer_shape(self):
        """ Verifies that output shape is as large as it should be. """
        x = tf.convert_to_tensor(
            np.random.uniform(0, 1, [1, 16, 18, 10]), dtype=tf.float32)
        y = tf.convert_to_tensor(
            np.random.uniform(0, 1, [1, 16, 18, 10]), dtype=tf.float32)
        out = tf_utils.correlation_layer(x, y, max_shift=1)
        self.assertEqual([1, 16, 18, 3*3], out.shape)
      
    def test_translation_list_sanity(self):
        EXPECTED_TX = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 0], [0, 1],
            [1, -1], [1, 0], [1, 1],
        ]
        tx = tf_utils._get_translation_list_for_correlation(1)
        self.assertEqual(EXPECTED_TX, tx)

    def test_correlation_layer_zeros(self):
        """ 
        Test documents that feature maps are zeroed out when shifts are applied.
        This essentially because the input feature maps are zeroed out when
        shifted.
        """
        from numpy.linalg import norm 
        shape = [1, 3, 3, 4]
        x = tf.convert_to_tensor(
            np.random.uniform(0, 1, shape), dtype=tf.float32)
        y = tf.convert_to_tensor(
            np.random.uniform(0, 1, shape), dtype=tf.float32)
        correlation = tf_utils.correlation_layer(x, y, max_shift=1)
 
        session = tf.Session()
        with session.as_default():
            corr_values = correlation.eval()
            corr_values = corr_values[0, :, :, :]
            
            values = corr_values[:,:,0] # (-1, -1)
            self.assertEqual(norm(values[:,-1]), 0,
                    "Right-most column should be zero!")
            self.assertEqual(norm(values[-1,:]), 0,
                    "Bottom-most row should be zero!")

            values = corr_values[:,:,8] # (1, 1)
            self.assertEqual(norm(values[0,:]), 0, "Top row should be zero.")
            self.assertEqual(norm(values[:,0]), 0,
                    "Left-most column should be zero.")


if __name__ == '__main__':
    # There is absolutely no reason to use GPU for these tests, and this
    # appears to be the most reliable way to disable GPU usage in tensorflow.
    os.environ['CUDA_VISIBLE_DEVICES'] = ''
    unittest.main(verbosity=2)
