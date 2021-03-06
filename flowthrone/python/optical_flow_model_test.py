import cv2
import numpy as np
import os
import unittest
import utils
from optical_flow_model import OpticalFlowModel
import tensorflow as tf

class OpticalFlowModelTest(unittest.TestCase):
    """ 
    A long and expensive integration test that verifies that a model can be
    loaded successfully.
    """

    # Travis-CI either times out on the 'unzip' stage of model downloading, or
    # maybe there are permissions issues. Either way, the test fails, so 
    # disable it for now.
    @unittest.skipIf('TRAVIS' in os.environ, 'Not well-supported in Travis-CI')
    def test_optical_flow_model_factory_method(self):
        """ 
        Verifies that the factory method is able to successfully load the
        latest model.
        """
        session = tf.Session() 
        model = OpticalFlowModel.create(session)


if __name__ == '__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = ''
    unittest.main(verbosity=2)
