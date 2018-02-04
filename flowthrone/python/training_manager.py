import os
import sys
from utils import compute_flow_color, resample_flow
from dataset_utils import Dataset, DataFeeder
import tensorflow as tf
import numpy as np
import shutil
import errno
import signal

""" Class that wraps some logic around training a tensorflow model:
    saving of / restoring from checkpoints, saving models, etc.  """
class TrainingManager:
    _config = None
    _train_writer = None
    _test_writer = None

    dataset = None
    feeder_train = None
    feeder_test = None
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
        config['output_path'] = os.path.join(config['base_path'], config['exp_name'])
        config['model_checkpoint_path'] = os.path.join(config['output_path'], 'checkpoints')
        config['export_dir'] = os.path.join(config['output_path'], 'model')
        # Remove anything that was created before.
        if config['fresh_start']:
            self._remove_paths(config)

        # Create necessary directories 
        self._create_paths(config)
        self._config = config
        self._print_tensorboard_hint(config['output_path'])

        # Initialize the dataset.
        self.dataset = Dataset(config['dataset_path'], 
                               config['train_test_num_splits'])
   
        # Load data.
        self.load_data_train()
        self.load_data_test()

        signal.signal(signal.SIGINT, self._sigint_handler)
        

    def config(self):
        return self._config
   
    """ Returns a list of existing model checkpoints """
    def checkpoints(self):
        return sorted([os.path.join(self._config['model_checkpoint_path'], f) \
                for f in os.listdir(self._config['model_checkpoint_path'])])

    """ Restores model from the provided checkpoint. """
    def restore_from_checkpoint(self, tf_session, checkpoint_path):
        model_checkpoint_fn = os.path.join(checkpoint_path, 'model.ckpt')
        print "Restoring model from an existing checkpoint '{}'".format(model_checkpoint_fn)
        tf.train.Saver().restore(tf_session, model_checkpoint_fn)
    
    """ Restores from last checkpoints, if any checkpoints exist; otherwise 
        calls default variable initialization. """
    def restore_from_last_checkpoint_if_possible(self, tf_session):
        pts = self.checkpoints()
        if len(pts) > 0:
            self.restore_from_checkpoint(tf_session, pts[-1])
        else:
            print ("Could not find any saved checkpoints; will instead "
                   "default initialize all variables.")
            tf_session.run(tf.global_variables_initializer())

    """ Saves a model (for inference elsewhere). """
    def save_model(self, tf_session, iteration):
        output_path = os.path.join(self._config['export_dir'], 
                                   '{:08d}'.format(iteration))
        print "Saving model in {}".format(output_path)
        if os.path.exists(output_path):
            print "Removing {} to resave model..".format(output_path)
            shutil.rmtree(output_path)
        builder = tf.saved_model.builder.SavedModelBuilder(output_path)
        builder.add_meta_graph_and_variables(tf_session, 
                [tf.saved_model.tag_constants.TRAINING])
        builder.save()

    """ Saves a model checkpoint (for restarting training.) """
    def save_checkpoint(self, tf_session, iteration):
        p = os.path.join(self._config['model_checkpoint_path'], 
                         '{:08d}'.format(iteration))
        if not os.path.exists(p):
            os.mkdir(p)
        model_checkpoint_fn = os.path.join(p, 'model.ckpt')
        save_path = tf.train.Saver().save(tf_session, model_checkpoint_fn)
        print "Saved model checkpoint to '{}'".format(save_path)

    """ Saves a checkpoint if the time is right. """
    def maybe_save_checkpoint(self, tf_session, iteration):
        if iteration > 0 and (iteration == 1 or \
                iteration % self._config['save_checkpoint_iter'] == 0):
            self.save_checkpoint(tf_session, iteration)

    """ Saves a model if the time is right. """
    def maybe_save_model(self, tf_session, iteration):
        if iteration > 0 and (iteration == 1 or \
                iteration % self._config['save_model_iter'] == 0):
            self.save_model(tf_session, iteration)
    
    def _print_tensorboard_hint(self, output_path):
        print ('To see training progress, you may launch tensorboard as: '
               'tensorboard --logdir {}').format(output_path)

    def load_data_train(self):
        print "Loading training data."
        self.feeder_train = None
        self.feeder_train = DataFeeder(self.dataset.train_files(),
                                       image_size=self._config['image_size'],
                                       batch_size=self._config['batch_size'],
                                       max_examples_to_use=self._config['num_train'])

    def load_data_test(self):
        print "Loading validation data."
        self.feeder_test = None
        self.feeder_test = DataFeeder(self.dataset.val_files(),
                                      image_size=self._config['image_size'],
                                      batch_size=self._config['batch_size'],
                                      max_examples_to_use=self._config['num_test'])

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


    def write_step_stats_timeline(self, run_metadata, output_filename):
        from tensorflow.python.client import timeline
        fetched_timeline = timeline.Timeline(run_metadata.step_stats)       
        chrome_trace = fetched_timeline.generate_chrome_trace_format()      
        with open(output_filename, 'w') as fid:                      
            fid.write(chrome_trace)
        print "Wrote a timeline object to '{}'".format(output_filename)


    """ Returns a tf exponential decay based on the config."""
    def _get_exponential_decay_learning_rate(self, global_step):
        return tf.train.exponential_decay(
                self._config['learning_rate'], global_step, 
                self._config['learning_rate_step'], 
                self._config['learning_rate_alpha'], staircase=True)
  
    """ Returns the optimizer. """
    def get_optimizer(self, loss):
        self.global_step = tf.Variable(0, trainable=False)
        self.learning_rate = self._get_exponential_decay_learning_rate(self.global_step)
        return tf.train.MomentumOptimizer(learning_rate=self.learning_rate, 
                momentum=self._config['momentum']).minimize(loss, self.global_step)

    """ Sets a member variable if sigint was captured. """
    def _sigint_handler(self, signum, frame):
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


""" Given batches of predictions, groundtruth, and a list of indices, returns
    a visualization of prediction/groundtruth flow. """
def get_flow_images(prediction, groundtruth, idx):
    flow_images = []
    for i in idx:
        flow_gt = np.squeeze(groundtruth[i])
        flow_pred = np.squeeze(prediction[i])
        if not flow_gt.shape[0] == flow_pred.shape[0] or \
                not flow_gt.shape[1] == flow_pred.shape[1]:
            flow_gt = resample_flow(flow_gt, flow_pred.shape)
        flow_gt = compute_flow_color(uv=flow_gt)
        flow_pred = compute_flow_color(uv=flow_pred)
        flow_images.append(np.concatenate([flow_gt, flow_pred], axis=1))
    return np.concatenate(flow_images, axis=1)



def get_visualization_summary(tf_session, prediction, groundtruth, summary_name):
    image_summary_ops = []
    idx = range(len(groundtruth))
    flow_images = get_flow_images(prediction, groundtruth, idx)
    flow_image = tf.reshape(flow_images, [1] + list(flow_images.shape))
    return tf_session.run(tf.summary.image(summary_name, flow_image))


def variable_summary(var):
    with tf.name_scope('summary'):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', tf.reduce_mean(var))
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.scalar('min', tf.reduce_min(var))
