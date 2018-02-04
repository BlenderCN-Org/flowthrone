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
from flownet128 import FlowNet
from training_manager import TrainingManager, \
        get_visualization_summary, variable_summary

DATASET_PATH = os.path.join(os.environ['HOME'], 'data', 'flying_chairs_128x128')
# Configuration used to run the training task.
config = {
    'num_train': 20000,
    'num_test': 1000,
    'num_iterations': 1000000,
    'batch_size': 70,
    'learning_rate': 5e-4,
    'learning_rate_alpha': 0.9,
    'learning_rate_step': 100000,
    'momentum': 0.9,

    'image_size': 128,
    # Path to the directory with images/groundtruth flow.
    'dataset_path': DATASET_PATH,
    'train_test_num_splits': 10,
    # How often to save model/checkpoint.
    'save_model_iter': 5000,
    'save_checkpoint_iter': 1000,
    
    'test_batch_iter': 50, # how often to evaluate on a test batch
    'visualization_iter': 1000, # how often to save images
    'print_iter':10, # how often to print stuff
    
    # How often to reload dataset. If your dataset is small, or if you have
    # a lot of memory, you can set this to zero (or a very large number), and
    # never do it. But if you cannot fit the entire dataset into memory, this
    # can be used to load the dataset every few iterations and select a
    # different fraction of it.
    'dataset_reload_iter': 1000, # how often to reload the dataset.
    # Experiment results will be written to:
    #   base_path/exp_name/{checkpoints, models}
    'base_path': '/persistent-tmp/',
    'exp_name': 'flownet128x128v5',
    # Wipe any data in the provided path (destroying any previous results),
    # and start anew.
    'fresh_start': False,
}

manager = TrainingManager(config)

imsize = config['image_size']
# Placeholders for input images.
x1 = tf.placeholder(tf.float32, [None, imsize, imsize, 3], name='x1')
x2 = tf.placeholder(tf.float32, [None, imsize, imsize, 3], name='x2')
# Placeholder for groundtruth.
y = tf.placeholder(tf.float32, [None, imsize, imsize, 2], name='y')

# Placeholder for weights. For many datasets (all datasets without notion of
# occlusions), weights are identically 1 everywhere. In these cases, for speed
# reasons, they can be omitted.
# w = tf.placeholder(tf.float32, [None, imsize, imsize, 2], name='w')

flownet = FlowNet(x1, x2)

# Config to turn on JIT compilation
session_config = tf.ConfigProto()
session_config.graph_options.optimizer_options.global_jit_level = tf.OptimizerOptions.ON_1

with tf.Session(config=session_config) as sess:
    # Setup loss for training and the optimizer.
    loss = flownet.set_loss(y)
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
    
    # Actually start training.
    for iter in range(tf_iteration.eval(sess), config['num_iterations']):
        if manager.sigint_happened:
            print "SIGINT was observed, saving checkpoint."
            manager.save_checkpoint(sess, iter)
            break

        if iter > 0 and iter % config['dataset_reload_iter'] == 0:
            manager.load_data_train()
            manager.load_data_test()

        x1_train, x2_train, y_train,_ = manager.feeder_train.next_batch()

        t_start = time.time()
        summary, _, avg_train_loss = sess.run(
                [merged, optimizer, loss], 
                feed_dict={x1: x1_train, x2: x2_train, y: y_train},
                            options=manager.run_options,
                            run_metadata=manager.run_metadata)
        t_end = time.time()

        manager.add_train_writer_summary(summary, iter)
        if iter % config['print_iter'] == 0:
            print "On iteration {}, loss = {}, iteration took {:.4f} sec".format(
                    iter, avg_train_loss, t_end-t_start)

        if np.isnan(avg_train_loss):
            print "Restoring from last checkpoint to avoid a nan..."
            manager.restore_from_last_checkpoint_if_possible(sess)
       
        # Run on a batch from validation set.
        if iter % config['test_batch_iter'] == 0:
            x1_test, x2_test, y_test,_ = manager.feeder_test.next_batch()
            summary, _ = sess.run([merged, loss],
                    feed_dict={x1: x1_test, x2: x2_test, y: y_test})
            manager.add_test_writer_summary(summary, iter)
          
        # Add summaries for results at the three finest scales.
        if iter % config['visualization_iter'] == 0:
            num = 10
            y_pred_tests = sess.run(flownet.predictions[0:3],
                    feed_dict={x1: x1_test[0:num], x2: x2_test[0:num],
                        y: y_test[0:num]})
            for y_pred_test in y_pred_tests:
                name = 'visualization-{}x{}'.format(
                        y_pred_test.shape[1], y_pred_test.shape[2])
                image_summary = get_visualization_summary(
                        sess, y_pred_test[0:num], y_test[0:num], 
                        summary_name=name)
                manager.add_test_writer_summary(image_summary, iter)

        # Save model/checkpoint if the time is appropriate.
        manager.maybe_save_model(sess, iter)
        manager.maybe_save_checkpoint(sess, iter)
        
        sess.run(tf_iteration.assign_add(1))
