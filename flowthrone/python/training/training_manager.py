import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import compute_flow_color, resample_flow
import dataset_utils
import tensorflow as tf
import numpy as np
import shutil
import errno
import signal
import augmentation
import glog as log


class TrainingManager:
    """
    Class that wraps some logic around training a tensorflow model:
    saving of / restoring from checkpoints, saving models, etc.
    """
    _config = None
    _train_writer = None
    _test_writer = None

    dataset_train = None
    dataset_test = None

    sigint_happened = False

    # Only in specific situations will these need to be set up differently.
    run_options = tf.RunOptions()
    run_metadata = tf.RunMetadata()

    learning_rate = None
    global_step = None

    def __init__(self, config):
        # Create additional entries in the config
        if not 'base_path' in config or not 'exp_name' in config:
            raise Exception('Incomplete config!')
        config['output_path'] = os.path.join(config['base_path'],
                                             config['exp_name'])
        config['model_checkpoint_path'] = os.path.join(config['output_path'],
                                                       'checkpoints')
        config['export_dir'] = os.path.join(config['output_path'], 'model')
        # Remove anything that was created before.
        if config['fresh_start']:
            self._remove_paths(config)

        # Create necessary directories
        self._create_paths(config)
        self._config = config
        self._print_tensorboard_hint(config['output_path'])

        self.dataset_train = tf.data.TFRecordDataset(
            config['input_tf_records_train'])
        self.dataset_test = tf.data.TFRecordDataset(
            config['input_tf_records_test'])

        self.dataset_train = self.dataset_train.map(
            lambda x: dataset_utils.decode_tf_example(x, config['image_size']))
        self.dataset_train = self.dataset_train.batch(config['batch_size'])
        if config['augment_by_flips']:
            self.dataset_train = self.dataset_train.map(
                lambda x1, x2, y: augmentation.maybe_flip_tf_example_left_right(x1, x2, y),
                num_parallel_calls=config['batch_size'])
            self.dataset_train = self.dataset_train.map(
                lambda x1, x2, y: augmentation.maybe_flip_tf_example_up_down(x1, x2, y),
                num_parallel_calls=config['batch_size'])
        if config['augment_by_brightness_contrast']:
            self.dataset_train = self.dataset_train.map(
                lambda x1, x2, y: augmentation.adjust_tf_example_brightness_contrast(
                    x1, x2, y, contrast=[0.9, 1.1], brightness=[-0.125, 0.125]),
                num_parallel_calls=config['batch_size'])
        if config['augment_by_transpose']:
            self.dataset_train = self.dataset_train.map(
                lambda x1, x2, y: augmentation.maybe_transpose_tf_example(x1, x2, y),
                num_parallel_calls=config['batch_size'])

        self.dataset_train = self.dataset_train.repeat()
        self.dataset_train = self.dataset_train.prefetch(config['batch_size'])
        # set up test dataset.
        self.dataset_test = self.dataset_test.map(
            lambda x: dataset_utils.decode_tf_example(x, config['image_size']))
        self.dataset_test = self.dataset_test.batch(
            config['batch_size']).repeat().prefetch(config['batch_size'])

        if config['shuffle']:
            print "Going to shuffle!"
            shuffle_buffer = 1024
            self.dataset_train = self.dataset_train.shuffle(
                shuffle_buffer, reshuffle_each_iteration=True)
            self.dataset_test = self.dataset_test.shuffle(
                shuffle_buffer, reshuffle_each_iteration=True)

        signal.signal(signal.SIGINT, self._sigint_handler)

    def config(self):
        return self._config

    def checkpoints(self):
        """ Returns a list of existing model checkpoints """
        return sorted([os.path.join(self._config['model_checkpoint_path'], f) \
                for f in os.listdir(self._config['model_checkpoint_path'])])

    def restore_from_checkpoint(self, tf_session, checkpoint_path):
        """ Restores model from the provided checkpoint. """
        model_checkpoint_fn = os.path.join(checkpoint_path, 'model.ckpt')
        print "Restoring model from an existing checkpoint '{}'".format(
            model_checkpoint_fn)
        tf.train.Saver().restore(tf_session, model_checkpoint_fn)

    def restore_from_last_checkpoint_if_possible(self, tf_session):
        """ Restores from last checkpoints, if any checkpoints exist; otherwise
            calls default variable initialization. """
        pts = self.checkpoints()
        if len(pts) > 0:
            self.restore_from_checkpoint(tf_session, pts[-1])
        else:
            print("Could not find any saved checkpoints; will instead "
                  "default initialize all variables.")
            tf_session.run(tf.global_variables_initializer())

    def save_model(self, tf_session, iteration):
        """ Saves a model (for inference elsewhere). """
        output_path = os.path.join(self._config['export_dir'],
                                   '{:08d}'.format(iteration))
        print "Saving model in {}".format(output_path)
        if os.path.exists(output_path):
            print "Removing {} to resave model..".format(output_path)
            shutil.rmtree(output_path)
        builder = tf.saved_model.builder.SavedModelBuilder(output_path)
        builder.add_meta_graph_and_variables(
            tf_session, [tf.saved_model.tag_constants.TRAINING])
        builder.save()

    def delete_old_checkpoints(self):
        MIN_CHECKPOINTS_TO_KEEP = 50
        p = self._config['model_checkpoint_path']
        if not os.path.exists(p):
            return
        files = sorted([os.path.join(p, f) for f in os.listdir(p)])
        num_to_delete = max(0, len(files) - MIN_CHECKPOINTS_TO_KEEP)
        for f in files[0:num_to_delete]:
            if os.path.isdir(f):
                shutil.rmtree(f)
                print "Removed {}".format(f)

    def save_checkpoint(self, tf_session, iteration):
        """ Saves a model checkpoint (for restarting training.) """
        p = os.path.join(self._config['model_checkpoint_path'],
                         '{:08d}'.format(iteration))
        if not os.path.exists(p):
            os.mkdir(p)
        model_checkpoint_fn = os.path.join(p, 'model.ckpt')
        save_path = tf.train.Saver().save(tf_session, model_checkpoint_fn)
        print "Saved model checkpoint to '{}'".format(save_path)

    def maybe_save_checkpoint(self, tf_session, iteration):
        """ Saves a checkpoint if the time is right. """
        if iteration > 0 and (iteration == 1 or \
                iteration % self._config['save_checkpoint_iter'] == 0):
            self.save_checkpoint(tf_session, iteration)

    def maybe_save_model(self, tf_session, iteration):
        """ Saves a model if the time is right. """
        if iteration > 0 and (iteration == 1 or \
                iteration % self._config['save_model_iter'] == 0):
            self.save_model(tf_session, iteration)

    def _print_tensorboard_hint(self, output_path):
        print('To see training progress, you may launch tensorboard as: '
              'tensorboard --logdir {}').format(output_path)

    def setup_train_writer(self, tf_session):
        self._train_writer = tf.summary.FileWriter(
            os.path.join(self._config['output_path'], 'train'))
        self._train_writer.add_graph(tf_session.graph)

    def setup_test_writer(self, tf_session):
        self._test_writer = tf.summary.FileWriter(
            os.path.join(self._config['output_path'], 'test'))
        self._test_writer.add_graph(tf_session.graph)

    def add_test_writer_summary(self, summary, iteration):
        self._test_writer.add_summary(summary, iteration)

    def add_train_writer_summary(self, summary, iteration):
        self._train_writer.add_summary(summary, iteration)

    def write_step_stats_timeline(self, output_filename):
        from tensorflow.python.client import timeline
        fetched_timeline = timeline.Timeline(self.run_metadata.step_stats)
        chrome_trace = fetched_timeline.generate_chrome_trace_format()
        with open(output_filename, 'w') as fid:
            fid.write(chrome_trace)
        print "Wrote a timeline object to '{}'".format(output_filename)

    def _get_exponential_decay_learning_rate(self, global_step):
        """ Returns a tf exponential decay based on the config."""
        return tf.train.exponential_decay(
            self._config['learning_rate'],
            global_step,
            self._config['learning_rate_step'],
            self._config['learning_rate_alpha'],
            staircase=True)

    def get_optimizer(self, loss):
        """ Returns the optimizer. """
        self.global_step = tf.Variable(0, trainable=False)
        self.learning_rate = self._get_exponential_decay_learning_rate(
            self.global_step)
        if self._config['optimizer'] == 'SGD':
            opt = tf.train.MomentumOptimizer(
                learning_rate=self.learning_rate,
                momentum=self._config['momentum'],
                use_nesterov=True)
        elif self._config['optimizer'] == 'ADAM':
            opt = tf.train.AdamOptimizer(
                learning_rate=self.learning_rate,
                beta1=self._config['adam_beta1'],
                beta2=self._config['adam_beta2'])
        else:
            log.fatal("UNRECOGNIZED OPTIMIZER TYPE")

        gradients, variables = zip(*opt.compute_gradients(loss))
        if 'max_gradient_norm' in self._config:
            gradients, _ = tf.clip_by_global_norm(
                gradients, self._config['max_gradient_norm'])

        with tf.name_scope('gradients'):
            variable_summary(tf.global_norm(gradients))
        return opt.apply_gradients(zip(gradients, variables))

    def _sigint_handler(self, signum, frame):
        """ Sets a member variable if sigint was captured. """
        print "Captured a signal: {} frame: {}".format(signum, frame)
        self.sigint_happened = True

    # Creates all directories needed for training.
    def _create_paths(self, config):
        for k in ['output_path', 'model_checkpoint_path', 'export_dir']:
            p = config[k]
            try:
                os.makedirs(p)
                print "Creating '{}'".format(p)
            except OSError as exception:
                if exception.errno == errno.EEXIST and os.path.isdir(p):
                    pass
                else:
                    raise Exception('Could not create {}'.format(p))

    # Removes all directories that were previously used for training.
    def _remove_paths(self, config):
        for k in ['output_path', 'model_checkpoint_path', 'export_dir']:
            p = config[k]
            if not os.path.exists(p):
                continue
            try:
                shutil.rmtree(p)
                print "Removing '{}'".format(p)
            except OSError as exception:
                raise Exception('Could not remove {}'.format(p))


def _visualize_uncertainty_prediction(log_uncertainty):
    MAX_VAL = 10
    occl = np.nan_to_num(log_uncertainty, 0.0)
    occl = np.squeeze(occl)
    occl = np.clip(occl, -MAX_VAL, MAX_VAL)
    occl = np.exp(occl)
    min_val = np.min(occl)
    max_val = np.max(occl)
    occl = 255.0*(occl - min_val) / (max_val - min_val + 1e-6)
    occl = np.reshape(occl, [occl.shape[0], occl.shape[1], 1])
    # reshape as [rows, cols, 3] (as if this were a bgr image).
    occl = np.concatenate([occl, occl, occl], axis=2)
    return occl


def get_flow_images(prediction, occlusion, groundtruth, idx):
    """ Given batches of predictions, groundtruth, and a list of indices,
        returns a visualization of prediction/groundtruth flow. """
    flow_images = []
    for i in idx:
        flow_gt = np.squeeze(groundtruth[i])
        flow_pred = np.squeeze(prediction[i])
        occl_pred = _visualize_uncertainty_prediction(occlusion[i])

        if not flow_gt.shape[0] == flow_pred.shape[0] or \
                not flow_gt.shape[1] == flow_pred.shape[1]:
            flow_gt = resample_flow(flow_gt, flow_pred.shape)
        flow_cat = np.concatenate([flow_gt, flow_pred], axis=1)
        flow_cat_vis = compute_flow_color(uv=flow_cat)
        flow_images.append(np.concatenate([occl_pred, flow_cat_vis], axis=1))
    return np.concatenate(flow_images, axis=1)


def get_visualization_summary(tf_session, prediction, occlusion, groundtruth,
                              summary_name):
    image_summary_ops = []
    idx = range(len(groundtruth))
    flow_images = get_flow_images(prediction, occlusion, groundtruth, idx)
    flow_image = tf.reshape(flow_images, [1] + list(flow_images.shape))
    return tf_session.run(tf.summary.image(summary_name, flow_image))


def variable_summary(var):
    with tf.name_scope('summary'):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', tf.reduce_mean(var))
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.scalar('min', tf.reduce_min(var))
        frac_nonzero = tf.cast(
            tf.count_nonzero(var), dtype=tf.float32) / tf.cast(
                tf.size(var), dtype=tf.float32)
        tf.summary.scalar('nnz', frac_nonzero)
