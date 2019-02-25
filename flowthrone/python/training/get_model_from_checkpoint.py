""" Creates a SavedModel from a checkpoint. This script is meant to be a
    temporary companion to train_tool.py which generates checkpoints, but not 
    SavedModel's.
"""

import os
import tensorflow as tf
import numpy as np
from flownet import FlowNet, FlowNetConfig
from training_manager import TrainingManager

# Configuration used to run the training task.
config = {
    'num_iterations': 1000000,
    'batch_size': 12,
    'learning_rate': 1e-4,
    'learning_rate_alpha': 0.9,
    'learning_rate_step': 100000,
    'momentum': 0.95,
    'image_size': 384,
    # Whether to augment training set.
    'augment_by_flips': True,
    'augment_by_brightness_contrast': True,
    'augment_by_transpose': True,
    # Path to the directory with images/groundtruth flow.
    'input_tf_records_train': '/data/flying_chairs_384x384_train.tfrecords',
    'input_tf_records_test': '/data/flying_chairs_384x384_test.tfrecords',
    'shuffle': False,
    # How often to save model/checkpoint.
    'save_model_iter': 1000000,
    'save_checkpoint_iter': 10000,
    'test_batch_iter': 100,  # how often to evaluate on a test batch
    'visualization_iter': 1000,  # how often to save images
    'print_iter': 10,  # how often to print stuff

    # Experiment results will be written to:
    #   base_path/exp_name/{checkpoints, models}
    'base_path': '/persistent-tmp/',
    'exp_name': 'flownet384x384v8',
    # Wipe any data in the provided path (destroying any previous results),
    # and start anew.
    'fresh_start': False,
}

manager = TrainingManager(config)

imsize = config['image_size']

flownet_config = FlowNetConfig()
x1 = tf.placeholder(tf.uint8, [None, imsize, imsize, 3], name='x1')
x2 = tf.placeholder(tf.uint8, [None, imsize, imsize, 3], name='x2')
is_training = tf.placeholder(tf.bool, name='is_training')
flownet = FlowNet(x1, x2, is_training=is_training, config=flownet_config)
prediction = tf.identity(flownet.predictions[0], name='prediction')

with tf.Session() as sess:
    manager.restore_from_last_checkpoint_if_possible(sess)
    manager.save_model(sess, int(1e6))
