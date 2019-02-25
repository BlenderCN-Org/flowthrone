""" Main script for training. """
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils
from utils import compute_flow_color
import tensorflow as tf
from tensorflow.python.client import timeline
import numpy as np
import time
import pwcnet
from pwcnet import PWCNet, PWCNetOptions, PWCNetTrainer, PWCNetTrainerOptions
from training_manager import TrainingManager, \
        get_visualization_summary, variable_summary

# Configuration used to run the training task.
SHOULD_AUGMENT_DATASET=True
config = {
    'num_iterations': 10000000,
    'batch_size': 20,
    'learning_rate': 0.001,
    'learning_rate_alpha': 0.9,
    'learning_rate_step': 100000,
    'optimizer': 'ADAM',
    'momentum': 0.9,
    'adam_beta1': 0.95,
    'adam_beta2': 0.999,
    'image_size': 256,
    # Whether to augment training set.
    'augment_by_flips': False,
    'augment_by_brightness_contrast': True,
    'augment_by_transpose': False,
    # Path to the directory with images/groundtruth flow.
    'input_tf_records_train': [
        '/data/flying_chairs_256x256_val.tfrecords',
        '/data/sdhom_chairs_256x256_train.tfrecords',
    ],
    'input_tf_records_test': [
        '/data/flying_chairs_256x256_val.tfrecords',
        '/data/sdhom_chairs_256x256_val.tfrecords',
    ],
    'shuffle': False,
    # How often to save model/checkpoint.
    'save_model_iter': 1000000,
    'save_checkpoint_iter': 1000,
    'test_batch_iter': 500,  # how often to evaluate on a test batch
    'visualization_iter': 2000,  # how often to save images
    'print_iter': 10,  # how often to print stuff
    # Experiment results will be written to:
    #   base_path/exp_name/{checkpoints, models}
    'base_path': '/persistent-tmp/',
    'exp_name': 'flying_chairs_occ_256x256',
    # Wipe any data in the provided path (destroying any previous results),
    # and start anew.
    'fresh_start': False,
}

manager = TrainingManager(config)
#manager.run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)

imsize = config['image_size']
# Placeholders for input images.
with tf.device('/cpu:0'):
    handle = tf.placeholder(tf.string, shape=[])
    iterator = tf.data.Iterator.from_string_handle(
        handle, manager.dataset_train.output_types,
        manager.dataset_train.output_shapes)
    x1, x2, y = iterator.get_next()
    train_iterator = manager.dataset_train.make_one_shot_iterator()
    test_iterator = manager.dataset_test.make_one_shot_iterator()

# If you don't care about batch_norm, then set this to 'None'.
is_training = tf.Variable(True, dtype=tf.bool, name='is_training')

# image dimensions: 64 -> 32 -> 16 -> 8 -> 4
pwc_options = PWCNetOptions()
pwc_options.pyramid_opt.NUM_FILTERS = [16, 32, 64, 128, 128, 128]
# The same number of filters is used at different pyramid levels, which is
# strange (one expects that the number of parameters for estimating small
# coarse flow fields could be smaller).
pwc_options.estimator_opt = {}
for lvl in [5, 4, 3, 2, 1]:
    pwc_options.estimator_opt[lvl] = pwcnet.OpticalFlowEstimatorOptions()
    pwc_options.estimator_opt[lvl].MAX_SHIFT = 1
    pwc_options.estimator_opt[lvl].is_training = is_training
    pwc_options.estimator_opt[lvl].USE_COST_VOLUME = True
    
    if lvl == 4:
        pwc_options.estimator_opt[lvl].NUM_FILTERS = [128, 128, 128, 128, 3]
    if lvl == 3:
        pwc_options.estimator_opt[lvl].NUM_FILTERS = [128, 128, 128, 128, 3]
    if lvl == 2:
        pwc_options.estimator_opt[lvl].NUM_FILTERS = [128, 128, 128, 128, 3]
    if lvl == 1:
        pwc_options.estimator_opt[lvl].NUM_FILTERS = [128, 128, 128, 128, 3]


pwc_options.pyramid_opt.is_training = is_training
pwc_options.use_context_net = True
pwc_options.context_opt.is_training = is_training

pwc_train_options = PWCNetTrainerOptions()
pwc_train_options.USE_ANGULAR_LOSS = True
pwc_train_options.LOSS_WEIGHTS = [4.0, 2.0, 1.0, 1.0, 0.25, 0.125]

# Instantiate network with attached losses.
trainer = PWCNetTrainer(
    x1=x1,
    x2=x2,
    groundtruth=y,
    train_options=pwc_train_options,
    pwc_options=pwc_options)
loss = trainer.get_loss()
prediction = tf.identity(trainer.get_output_flow(), name='prediction')
occlusion = tf.identity(trainer.get_output_occlusion(), name='occlusion')

prediction_1 = trainer.get_network().get_raw_flow(1)
prediction_2 = trainer.get_network().get_raw_flow(2)
occlusion_1 = trainer.get_network().get_raw_occlusion(1)
occlusion_2 = trainer.get_network().get_raw_occlusion(2)

# Config to turn on JIT compilation
session_config = tf.ConfigProto()
session_config.gpu_options.allow_growth = True
# Doesn't work due to CUDA/nvidia driver combination.
#session_config.graph_options.optimizer_options.global_jit_level = \
#        tf.OptimizerOptions.ON_1

with tf.Session(config=session_config) as sess:
    # The `Iterator.string_handle()` method returns a tensor that can be
    # evaluated and used to feed the `handle` placeholder.
    train_itr_handle = sess.run(train_iterator.string_handle())
    test_itr_handle = sess.run(test_iterator.string_handle())

    optimizer = manager.get_optimizer(loss)
    tf_iteration = tf.Variable(0, name='iteration_counter', trainable=False)
    tf_iteration_increment_op = tf.assign(tf_iteration, tf_iteration + 1)
    for var in [x1, x2, y, prediction, occlusion]:
        tf.add_to_collection('vars', var)
    tf.summary.scalar('learning_rate', manager.learning_rate)
    
    with tf.name_scope('prediction'):
        variable_summary(prediction)
    with tf.name_scope('occlusion'):
        variable_summary(prediction)

    for dim in sorted(trainer.groundtruth.keys()):
        gt = trainer.groundtruth[dim]
        gt_name = 'groundtruth_{}x{}'.format(gt.shape[1], gt.shape[2])
        with tf.name_scope(gt_name):
            variable_summary(gt)

    manager.restore_from_last_checkpoint_if_possible(sess)
    manager.delete_old_checkpoints()
    manager.setup_train_writer(sess)
    manager.setup_test_writer(sess)
    merged = tf.summary.merge_all()

    # Actually start training.
    t_last = time.time()
    for iter in range(tf_iteration.eval(sess), config['num_iterations']):
        t1 = time.time()
        if manager.sigint_happened:
            print "SIGINT was observed, saving checkpoint."
            manager.save_checkpoint(sess, iter)
            manager.save_model(sess, iter)
            break

        t_start = time.time()
        summary, _, avg_train_loss, _ = sess.run(
            [merged, optimizer, loss, tf_iteration_increment_op],
            feed_dict={is_training: True,
                       handle: train_itr_handle},
            options=manager.run_options,
            run_metadata=manager.run_metadata)
        t_end = time.time()
        
        #manager.write_step_stats_timeline('/tmp/blah_{:3d}.json'.format(iter))
        
        if iter % 100 == 0:
            manager.add_train_writer_summary(summary, iter)
        
        if iter % config['print_iter'] == 0:
            print ("On iteration {}, loss = {}, iteration took {:.4f} sec;"
                   "since last call: {:.4f} sec").format(
                iter, avg_train_loss, t_end - t_start, time.time() - t_last)
            t_last = time.time()

        if np.isnan(avg_train_loss):
            print "Restoring from last checkpoint to avoid a nan..."
            manager.restore_from_last_checkpoint_if_possible(sess)

        # Run on a batch from validation set.
        if iter % config['test_batch_iter'] == 0:
            t_start = time.time()
            summary, _ = sess.run(
                [merged, loss],
                feed_dict={is_training: False,
                           handle: test_itr_handle})
            manager.add_test_writer_summary(summary, iter)
            # Add summaries for results at the three finest scales.
            if iter % config['visualization_iter'] == 0:
                num = 10
                sess_outs = sess.run(
                    [y, prediction, occlusion, prediction_1, occlusion_1, prediction_2, occlusion_2],
                    feed_dict={is_training: False,
                               handle: test_itr_handle})

                y_gt = sess_outs[0]
                y_pred_tests = [[sess_outs[1], sess_outs[2]],
                                [sess_outs[3], sess_outs[4]],
                                [sess_outs[5], sess_outs[6]]]
                for y_pred_test, y_occ_test in y_pred_tests:
                    name = 'visualization-{}x{}'.format(y_pred_test.shape[1],
                                                        y_pred_test.shape[2])
                    print name
                    image_summary = get_visualization_summary(
                        sess,
                        y_pred_test[0:num, :, :, :],
                        y_occ_test[0:num, :, :, :],
                        y_gt[0:num, :, :, :],
                        summary_name=name)
                    manager.add_test_writer_summary(image_summary, iter)
                # Another attempt for training set.
                sess_outs = sess.run(
                    [y, prediction, occlusion, prediction_1, occlusion_1, prediction_2, occlusion_2],
                    feed_dict={is_training: False,
                               handle: train_itr_handle})

                y_gt = sess_outs[0]
                y_preds = [[sess_outs[1], sess_outs[2]],
                           [sess_outs[3], sess_outs[4]],
                           [sess_outs[5], sess_outs[6]]]
                for y_pred, y_occ in y_preds:
                    name = 'train-visualization-{}x{}'.format(y_pred.shape[1],
                                                              y_pred.shape[2])
                    image_summary = get_visualization_summary(
                        sess,
                        y_pred[0:num, :, :, :],
                        y_occ[0:num, :, :, :],
                        y_gt[0:num, :, :, :],
                        summary_name=name)
                    manager.add_test_writer_summary(image_summary, iter)


            t_end = time.time()
            print "Test iteration took {:.4f} sec".format(t_end - t_start)

        # Save model/checkpoint if the time is appropriate.
        #manager.maybe_save_model(sess, iter)
        manager.maybe_save_checkpoint(sess, iter)
        manager.delete_old_checkpoints()
