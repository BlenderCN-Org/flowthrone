""" Main script for training. """
import os
import sys
import cv2
import utils
from utils import compute_flow_color
from dataset_utils import Dataset, DataFeeder
import tensorflow as tf
from tensorflow.python.client import timeline
import numpy as np
import shutil
import time
from tf_utils import resample_flow, angular_flow_error
from flownet import FlowNet, FlowNetConfig
from training_manager import TrainingManager, \
        get_visualization_summary, variable_summary

DATASET_PATH = os.path.join(os.environ['HOME'], 'data',
                            'flying_chairs_384x384')
# Configuration used to run the training task.
config = {
    # How many examples to hold in memory
    'num_train': 3500,
    'num_test': 200,
    'num_iterations': 1000000,
    'batch_size': 28,
    'learning_rate': 1e-3,
    'learning_rate_alpha': 0.9,
    'learning_rate_step': 100000,
    'momentum': 0.95,
    'image_size': 384,
    # Path to the directory with images/groundtruth flow.
    'input_tf_records_train': '/data/flying_chairs_384x384_train.tfrecords',
    'input_tf_records_test': '/data/flying_chairs_384x384_test.tfrecords',
    'shuffle': False,
    # How often to save model/checkpoint.
    'save_model_iter': 5000,
    'save_checkpoint_iter': 10000,
    'test_batch_iter': 500,  # how often to evaluate on a test batch
    'visualization_iter': 1000,  # how often to save images
    'print_iter': 10,  # how often to print stuff

    # Experiment results will be written to:
    #   base_path/exp_name/{checkpoints, models}
    'base_path': '/persistent-tmp/',
    'exp_name': 'flownet384x384v7',
    # Wipe any data in the provided path (destroying any previous results),
    # and start anew.
    'fresh_start': False,
}

manager = TrainingManager(config)

imsize = config['image_size']
# Placeholders for input images.

iterator = tf.data.Iterator.from_structure(manager.dataset_train.output_types,
                                           manager.dataset_test.output_shapes)
train_init_op = iterator.make_initializer(manager.dataset_train)
test_init_op = iterator.make_initializer(manager.dataset_test)
x1, x2, y = iterator.get_next()

flownet_config = FlowNetConfig()
is_training = tf.placeholder(tf.bool, name='is_training')
flownet = FlowNet(x1, x2, is_training=is_training, config=flownet_config)
prediction = tf.identity(flownet.predictions[0], name='prediction')

# Config to turn on JIT compilation
session_config = tf.ConfigProto()
# Doesn't work due to CUDA/nvidia driver combination.
#session_config.graph_options.optimizer_options.global_jit_level = tf.OptimizerOptions.ON_1

with tf.Session(config=session_config) as sess:
    # Setup loss for training and the optimizer.
    flownet.set_endpoint_error_loss(y)
    flownet.set_angular_error_loss(y)
    #flownet.set_brightness_constancy_violation_loss()
    loss = flownet.get_loss()

    optimizer = manager.get_optimizer(loss)
    tf_iteration = tf.Variable(0, name='iteration_counter')

    with tf.name_scope('summary_prediction'):
        variable_summary(flownet.predictions[0])
    for var in [x1, x2, y, flownet.predictions[0]]:
        tf.add_to_collection('vars', var)
    tf.summary.scalar('learning_rate', manager.learning_rate)

    manager.restore_from_last_checkpoint_if_possible(sess)
    manager.setup_train_writer(sess)
    manager.setup_test_writer(sess)
    merged = tf.summary.merge_all()

    # Initialize the training iterrator
    sess.run(train_init_op)

    # Actually start training.
    for iter in range(tf_iteration.eval(sess), config['num_iterations']):
        if manager.sigint_happened:
            print "SIGINT was observed, saving checkpoint."
            manager.save_checkpoint(sess, iter)
            manager.save_model(sess, iter)
            break

        t_start = time.time()
        summary, _, avg_train_loss = sess.run(
            [merged, optimizer, loss],
            feed_dict={is_training: True},
            options=manager.run_options,
            run_metadata=manager.run_metadata)
        t_end = time.time()

        manager.add_train_writer_summary(summary, iter)
        if iter % config['print_iter'] == 0:
            print "On iteration {}, loss = {}, iteration took {:.4f} sec".format(
                iter, avg_train_loss, t_end - t_start)

        if np.isnan(avg_train_loss):
            print "Restoring from last checkpoint to avoid a nan..."
            manager.restore_from_last_checkpoint_if_possible(sess)

        # Run on a batch from validation set.
        if iter % config['test_batch_iter'] == 0:
            # This is not super great -- always initializes at the beginning
            # of the dataset.
            print "Switching to test iterator.."
            sess.run(test_init_op)
            summary, _ = sess.run([merged, loss],
                                  feed_dict={is_training: False})
            manager.add_test_writer_summary(summary, iter)
            # Add summaries for results at the three finest scales.
            if iter % config['visualization_iter'] == 0:
                sess.run(test_init_op)
                num = 10
                y_test, y_pred_tests = sess.run([y, flownet.predictions[0:3]],
                                                feed_dict={is_training: False})
                for y_pred_test in y_pred_tests:
                    name = 'visualization-{}x{}'.format(y_pred_test.shape[1],
                                                        y_pred_test.shape[2])
                    image_summary = get_visualization_summary(
                        sess,
                        y_pred_test[0:num],
                        y_test[0:num],
                        summary_name=name)
                    manager.add_test_writer_summary(image_summary, iter)
            print "Switching to train iterator..."
            sess.run(train_init_op)

        # Save model/checkpoint if the time is appropriate.
        manager.maybe_save_model(sess, iter)
        manager.maybe_save_checkpoint(sess, iter)

        sess.run(tf_iteration.assign_add(1))
