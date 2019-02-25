import cv2
import glog as log
import numpy as np
import os
import tensorflow as tf
from pwcnet import PWCNet, PWCNetOptions
from utils import resample_flow

""" 
Wrapper around a tensorflow model for running optical flow.
PARAMETERS:
    session     - TF session
    size        - Dimensions of the instantiated network (e.g. 512x256 or 
                  512x384). Specified as width, height. This must be n-th
                  power of two for some n.
                  Specifically it corresponds to the size of the input/output
                  feature maps in the network.
                  TODO: this is a place where interface 'leaks'. This option
                        should not be mandatory (for example the trained
                        network knows its 'default' size.
    model_path  - Path to the saved model/checkpoint. Must contain inside:
                    checkpoint/checkpoint
                    checkpoint/model.ckpt*
                    checkpoint/options.pkl
USAGE:
    >>> checkpoint_path = '/tmp/best-optical-flow-model/'
    >>> # path should contain the following files:
    >>> #   checkpoint/options.pkl
    >>> #   checkpoint/model.ckpt
    >>> sess = tf.Session()
    >>> model = OpticalFlowModel(sess, (256, 256), model_path=checkpoint_path)
    >>> # load images/video from somewhere as numpy arrays.
    >>> uv = model.run(image1=image1, image2=image2)
    >>> # visualize flow field.
    >>> cv.imshow("uv", compute_flow_color(uv))
    >>> cv.waitKey(0)
"""
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
        # TODO: figure out how to do this in a nicer way. Some network were
        # trained without batch_norm -- in those cases, is_training is not 
        # needed.
        self.is_training = None  #tf.placeholder(dtype=tf.bool, name='is_training')

        model_options_filename = os.path.join(model_path, 'checkpoint',
                                              'options.pkl')
        model_checkpoint_filename = os.path.join(model_path, 'checkpoint',
                                                 'model.ckpt')
        log.check(
            os.path.exists(model_options_filename),
            "Did not find '{}'".format(model_options_filename))
        log.check(
            os.path.exists(os.path.dirname(model_checkpoint_filename)),
            "Did not find '{}'".format(
                os.path.dirname(model_checkpoint_filename)))

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
            feed_dict=self.__get_feed_dict(_image1, _image2))
        output_flow = output_flow[0, :, :, :]
        output_flow = resample_flow(output_flow, image1.shape)
        return output_flow

    def __get_feed_dict(self, image1, image2):
        if self.is_training is None:
            return {self.x1: image1, self.x2: image2}
        else:
            return {self.is_training: False, self.x1: image1, self.x2: image2}
