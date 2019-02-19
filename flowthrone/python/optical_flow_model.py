import cv2
import glog as log
import numpy as np
import os
import tensorflow as tf
from pwcnet import PWCNet, PWCNetOptions
from utils import resample_flow

class OpticalFlowModel:
    def __init__(self, session, size, model_path):
        self.session = session
        self.height = size[1]
        self.width = size[0]
        self.x1 = tf.placeholder(
            dtype=tf.uint8,
            shape=[None, self.height, self.width, 3],
            name='x1')
        self.x2 = tf.placeholder(
            dtype=tf.uint8,
            shape=[None, self.height, self.width, 3],
            name='x2')
        self.is_training = tf.placeholder(dtype=tf.bool, name='is_training')

        model_options_filename = os.path.join(model_path, 'checkpoint', 'options.pkl')
        model_checkpoint_filename = os.path.join(model_path, 'checkpoint', 'model.ckpt')
        log.check(os.path.exists(model_options_filename),
                "Did not find '{}'".format(model_options_filename))
        log.check(os.path.exists(os.path.dirname(model_checkpoint_filename)),
                "Did not find '{}'".format(os.path.dirname(model_checkpoint_filename)))

        pwc_options = PWCNetOptions.load(model_options_filename,
                                         self.is_training)
        self.net = PWCNet(x1=self.x1, x2=self.x2, options=pwc_options)
        self.output_flow_op = self.net.get_output_flow()
        tf.train.Saver().restore(self.session, model_checkpoint_filename)

    def run(self, image1, image2):
        _image1 = cv2.resize(image1, (self.width, self.height))
        _image2 = cv2.resize(image2, (self.width, self.height))
        _image1 = np.reshape(_image1, [1] + list(_image1.shape))
        _image2 = np.reshape(_image2, [1] + list(_image2.shape))

        output_flow, = self.session.run(
            [self.output_flow_op],
            feed_dict={self.is_training: False,
                       self.x1: _image1,
                       self.x2: _image2})
        output_flow = output_flow[0, :, :, :]
        output_flow = resample_flow(output_flow, image1.shape)
        return output_flow
