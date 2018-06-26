import cv2
import tensorflow as tf
import os
import unittest
import tf_utils
import numpy as np

# TODO(vasiliy):!!!
class TestDataAugmentation(unittest.TestCase):
    tolerance = 1e-3

    def setUp(self):
        pass

if __name__ == '__main__':
    # There is absolutely no reason to use GPU for these tests, and this
    # appears to be the most reliable way to disable GPU usage in tensorflow.
    os.environ['CUDA_VISIBLE_DEVICES'] = ''
    unittest.main(verbosity=2)
