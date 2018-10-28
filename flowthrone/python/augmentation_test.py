import cv2
from augmentation import *
import os
import unittest
import numpy as np
from utils import compute_residual


class TestDataAugmentation(unittest.TestCase):
    image = None
    uv = None
    tolerance = 1e-3

    def setUp(self):
        image1 = np.ones([20, 20, 3]) * 0.5
        image2 = np.ones([20, 20, 3]) * 0.5
        uv = np.zeros([20, 20, 2])
        image1[5:15, 5:15, :] = 1.0
        image2[8:18, 7:17, :] = 1.0
        uv[5:15, 5:15, 0] = 2
        uv[5:15, 5:15, 1] = 3

        self.image1 = tf.convert_to_tensor(image1, dtype=tf.float32)
        self.image2 = tf.convert_to_tensor(image2, dtype=tf.float32)
        self.uv = tf.convert_to_tensor(uv, dtype=tf.float32)

    def _internal_tester(self, func):
        """
        Verify that residual error before and after applying |func| is the
        same. This is a cheap way to verify that flow did not become
        inconsistent with image data. """
        x1 = self.image1
        x2 = self.image2
        y = self.uv
        session = tf.Session()
        with session.as_default():
            x1_flip, x2_flip, y_flip = func(x1, x2, y)
            x1, x2, y, x1_flip, x2_flip, y_flip = \
                session.run([x1, x2, y, x1_flip, x2_flip, y_flip])

            residual = compute_residual(x1, x2, y)
            residual_flip = compute_residual(x1_flip, x2_flip, y_flip)

            error = np.abs(
                np.linalg.norm(residual_flip) - np.linalg.norm(residual))
            self.assertLessEqual(error, self.tolerance)

    def test_flip_left_right(self):
        self._internal_tester(flip_tf_example_left_right)
    
    def test_flip_up_down(self):
        self._internal_tester(flip_tf_example_up_down)

    def test_transpose_tf_example(self):
        self._internal_tester(transpose_tf_example)


if __name__ == '__main__':
    # There is absolutely no reason to use GPU for these tests, and this
    # appears to be the most reliable way to disable GPU usage in tensorflow.
    os.environ['CUDA_VISIBLE_DEVICES'] = ''
    unittest.main(verbosity=2)
