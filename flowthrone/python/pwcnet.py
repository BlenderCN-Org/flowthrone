"""
Implementation of PWC-net, as described in:
  https://arxiv.org/pdf/1709.02371.pdf
  "PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume",
    D. Sun, X. Yang, M.Y. Liu, and J. Kautz

but with some differences (to put it mildly).

Watch out: channel dimensions do not follow the ones described in the paper
(i did not attempt to replicate  the results), nor are they carefully chosen.
Additionally, some tricks used in authors' code (in particular vis-a-vis
scaled flow fields) are not used here. We also use batch norm whereas authors
don't seem to, we also use angular loss, etc...

Classes are organized roughly as follows:

- PWCNet:
    constructs the entire network. Most users should be using this class and
    shouldn't really care about anything else in this file.

- PWCNetTrainer:
    used for training PWCNet. If you only care about inference, you do not
    need this.

- OpticalFlowEstimator
    module that produces a NxN flow estimate given
        a) two NxN feature maps (corresponding to first and second image)
        b) N/2 x N/2 optical flow (from coarser level of the pyramid)
    This is one of the components described in the paper.

- FeaturePyramidExtractor
    module that extracts feature maps. This is roughly similar to an 'encoder'
    in a U-net type network. This is one of the components described in the
    paper.
    Note that this class is a 'singleton' in the sense that multiple instances
    will share the same weights (as in the paper).

- ContextEstimator
    module that 'refines' optical flow (this is just a deep version of
    bilateral/cross-bilateral/median filter sorcery common in classical
    optical flow methods).
"""

# Add parent directory to pythonpath.
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tensorflow as tf
import tf_utils
from training_manager import variable_summary
import warnings
from tensorflow.contrib.slim import conv2d
from tensorflow.contrib.slim import l2_regularizer
from tensorflow.contrib.layers import batch_norm
import glog as log
import pickle

GLOBAL_L2_REGULARIZATION = 1e-9


class OpticalFlowEstimator:
    """
    A network for producing an optical flow estimate given a pair of images
    and a subsampled input flow estimate.

    USAGE:
    >>> net = OpticalFlowEstimator(x1, x2, uv) # 'x1' and 'x2' should have the
    >>>                                        # same shape, while 'uv' must be
    >>>                                        # twice smaller.
    >>> output = net.get_flow() # accessor for the output of the network
    >>>                         # (flow estimate that has the same dimensions
    >>>                         # as the input feature maps)
    >>> # the class provides additional accessors (for debugging and for
    >>> # routing into other networks):
    >>> penultimate = net.get_penultimate_layer() # feature map immediately
    >>>                                           # before the output.
    >>> cost_volume = net.get_cost_volume() # output of the correlation layer.
    >>> x2_warped = net.get_x2_warped() # feature map warped by the input flow
    >>>                                 # estimate.
    """

    def __init__(self, x1, x2, uv, opt=None):
        OpticalFlowEstimator._verify_shapes(x1, x2, uv)

        self.options = opt if opt is not None else \
            OpticalFlowEstimatorOptions()

        name = 'OpticalFlowEstimator_{}x{}'.format(x1.shape[1], x1.shape[2])
        with tf.name_scope(None, name, [x1, x2, uv]):
            uv_upsampled = tf_utils.resample_flow(uv, x2.shape)
            self.x2_warped = tf_utils.warp_with_flow(x2, uv_upsampled)

            if self.options.USE_COST_VOLUME:
                self.cost_volume = tf_utils.correlation_layer(
                    x1, self.x2_warped, self.options.MAX_SHIFT)
                # TODO(vasiliy): it is very unfortunate that uv_upsampled was
                # originally incorrectly omitted from this line.
                # It may be worthwhile to 'normalize it' (something similar is
                # mentioned in the paper) to avoid values from increasing over
                # different layers.
                network_tail = tf.concat(
                    [self.cost_volume, x1, uv_upsampled], axis=3)
            else:
                network_tail = tf.concat(
                    [x1, self.x2_warped, uv_upsampled], axis=3)
                self.cost_volume = None
            self.layers = self._make_network_spine(network_tail)

    def get_x2_warped(self):
        """
        Returns tensor corresponding to 'x2' warped to 'x1' using the input
        flow.
        """
        return self.x2_warped

    def get_cost_volume(self):
        """
        Returns tensor corresponding to the 'cost volume', output of the
        correlation layer.
        """
        return self.cost_volume

    def get_flow(self):
        """ Returns tensor corresponding to the estimated optical flow. """
        return self.layers[-1]

    def get_penultimate_layer(self):
        """ Returns the penultimate feature map. """
        log.check_ge(
            len(self.layers), 2, 'Network doesnt have a penultimate layer.')
        return self.layers[-2]

    def debug_info(self):
        """ Prints network layers. """
        print "x2 warped layer: ", self.x2_warped
        if self.cost_volume is not None:
            print "cost volume: ", self.cost_volume
        else:
            print "cost volume was not instantiated."
        for i, layer in enumerate(self.layers):
            print "Spine layer {}:".format(i), layer

    def _make_network_spine(self, entree):
        """
        Returns a sequence of layers forming the 'spine' of the network.
        The input layer is the first element in the returned list, and the last
        element is the the output 'layer'. Spatial dimensions of the feature
        map are preserved.
        """
        outputs = [entree]
        for outs in self.options.NUM_FILTERS[0:-1]:
            outputs.append(
                self._conv2d_rectified(
                    outputs[-1], num_outputs=outs))
        # Add the final layer without ReLU following it.
        log.check_eq(
            2,
            self.options.NUM_FILTERS[-1],
            message=('Last filter in the list must have "num_outputs=2", '
                     'since its output is optical flow field.'))

        outputs.append(
            self._conv2d(
                entree=outputs[-1], num_outputs=self.options.NUM_FILTERS[-1]))

        return outputs

    def _conv2d_rectified(self, entree, num_outputs):
        """ Wrapper around conv2d. """
        use_batch_norm = self.options.is_training is not None
        return _maybe_add_batch_norm_or_activation_fn(
            self._conv2d(entree, num_outputs),
            use_batch_norm,
            self.options.is_training,
            activation_fn=tf.nn.leaky_relu)

    def _conv2d(self, entree, num_outputs):
        """
        Wrapper around conv2d with a smaller number of arguments, since all
        layers in feature pyramid extractor have padding 'SAME' and the same
        kernel size. This function does not apply any rectification.
        """
        return conv2d(
            entree,
            num_outputs=num_outputs,
            kernel_size=3,
            stride=1,
            padding='SAME',
            weights_regularizer=l2_regularizer(
                self.options.L2_REGULARIZATION_SCALE),
            activation_fn=None)

    @staticmethod
    def _verify_shapes(c1, c2, uv):
        log.check_eq(c1.shape[1:], c2.shape[1:],\
            "Shape of the two feature maps must match!")
        log.check_eq(len(set([c1.dtype, c2.dtype, uv.dtype])), 1, \
            "All datatypes must match")
        log.check(all([4 == len(nd) for nd in [c1.shape, c2.shape, uv.shape]]), \
                "Must be passed as NxHxWxC")
        log.check_eq(uv.shape[3], 2, "Did not pass flow where expected flow?")
        log.check_eq(2 * int(uv.shape[1]), c1.shape[1])
        log.check_eq(2 * int(uv.shape[2]), c1.shape[2])

class OpticalFlowEstimatorOptions:
    def __init__(self):
        self.MAX_SHIFT = 1
        self.L2_REGULARIZATION_SCALE = GLOBAL_L2_REGULARIZATION
        self.NUM_FILTERS = [128, 64, 64, 32, 2]
        # cost-volume / correlation layer hasn't been properly vetted, so
        # 'off' by default.
        self.USE_COST_VOLUME = False
        # Unless this is 'None', will apply batch_norm after each
        # convolutional layer.
        self.is_training = None

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class FeaturePyramidExtractor:
    """
    A network for feature pyramid extraction.
    CAUTION: multiple instances of this network will share weights.

    USAGE:
    >>> net = FeaturePyramidExtractor(inp)
    >>> # different 'levels' in the pyramid can be accessed like so:
    >>> net.get_level(index) # index >= 0 and index <= 6

    >>> net.get_level(0) == inp # the first layer is exactly the tensor that
    >>>                         # you provided at input time.
    >>> # you may also access individual layers like so:
    >>> net.layers
    """

    def __init__(self, entree, opt=None):
        """ Returns a network """
        FeaturePyramidExtractor._verify_input(entree)
        self.options = opt if opt is not None \
            else FeaturePyramidExtractorOptions()

        self.layers = []
        self.layers.append(entree)
        with tf.variable_scope('feature_pyramid'):
            for index, outs in enumerate(self.options.NUM_FILTERS):
                self.layers.append(
                    self._conv2d_rectified(
                        self.layers[-1],
                        num_outputs=outs,
                        stride=2,
                        scope='conv{}a'.format(index)))
                self.layers.append(
                    self._conv2d_rectified(
                        self.layers[-1],
                        num_outputs=outs,
                        stride=1,
                        scope='conv{}b'.format(index)))
                # third layer is present in the pytorch implementation ?!
                self.layers.append(
                    self._conv2d_rectified(
                        self.layers[-1],
                        num_outputs=outs,
                        stride=1,
                        scope='conv{}c'.format(index)))

    def num_levels(self):
        return len(self.options.NUM_FILTERS) + 1

    def get_level(self, index):
        """ Returns 'layer' in the pyramid (called c_t^{index} in the paper).
            (The pyramid is split into 7 blocks, but each blocks actually has
            two conv layers). """
        log.check_ge(index, 0)
        log.check_le(index, self.options.NUM_FILTERS)
        return self.layers[3 * index]

    def debug_info(self):
        """ Prints layers """
        for i, layer in enumerate(self.layers):
            print "Feature pyramid extractor layer {}:".format(i), layer

    def _conv2d_rectified(self, entree, num_outputs, stride, scope):
        use_batch_norm = self.options.is_training is not None
        conv_op = self._conv2d(entree, num_outputs, stride, scope)
        return _maybe_add_batch_norm_or_activation_fn(
            conv_op,
            use_batch_norm,
            self.options.is_training,
            reuse=tf.AUTO_REUSE,
            scope=scope,
            activation_fn=tf.nn.leaky_relu)

    def _conv2d(self, entree, num_outputs, stride, scope):
        """
        Wrapper around conv2d with a smaller number of arguments, since all
        layers in feature pyramid extractor have padding 'SAME' and the same
        kernel size.
        Does not apply an activation function.
        """
        return conv2d(
            entree,
            num_outputs=num_outputs,
            kernel_size=3,
            stride=stride,
            padding='SAME',
            weights_regularizer=l2_regularizer(
                self.options.L2_REGULARIZATION_SCALE),
            activation_fn=None,
            reuse=tf.AUTO_REUSE,
            scope=scope)

    @staticmethod
    def _verify_input(entree):
        log.check_eq(len(entree.shape), 4, \
            ("Input must be NHWC (i.e. must have 4 dimensions) -- "
             "slim behaves poorly otherwise."))
        log.check_eq(entree.shape[-1], 3, "Input should have three channels.")


class FeaturePyramidExtractorOptions:
    def __init__(self):
        self.L2_REGULARIZATION_SCALE = GLOBAL_L2_REGULARIZATION
        self.NUM_FILTERS = [16, 32, 64, 96, 128, 192]
        # If set to something other than 'None', will apply batch
        # normalization.
        self.is_training = None

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class ContextEstimator:
    """
    The context network that takes in a flow estimate and a feature map,
    and produces a 'refined' flow field.

    USAGE:
    >>> net = ContextEstimator(inputs, uv)
    >>> output = net.get_flow() # accessor for the final flow estimate.
    >>> # additionally, you can access intermediate layers by e.g.:
    >>> [print layer for layer in net.layers ]
    >>> # the last element in that array is the 'delta' flow estimated by the
    >>> # network.
    """

    def __init__(self, entree, uv, opt=None):
        ContextEstimator._verify_input(entree, uv)

        self.options = opt if opt is not None \
            else ContextEstimatorOptions()

        inp_concat = tf.concat([entree, uv], axis=3)
        with tf.name_scope('context'):
            self.layers = self._make_network_spine(inp_concat)
            # Add the final layer without ReLU following it.
            self.layers.append(
                conv2d(
                    inputs=self.layers[-1],
                    num_outputs=2,
                    kernel_size=3,
                    padding='SAME',
                    weights_regularizer=l2_regularizer(
                        self.options.L2_REGULARIZATION_SCALE),
                    activation_fn=None))
        # The two estimates (the 'delta' estimate from the network and the
        # original estimate) are combined by a simple addition.
        self.flow = self.layers[-1] + uv

    def get_flow(self):
        """ Returns the final flow estimate. """
        return self.flow

    def _make_network_spine(self, inp):
        log.check_eq(
            len(self.options.NUM_FILTERS),
            len(self.options.NUM_DILATIONS),
            'NUM_FILTERS and NUM_DILATIONS must be equally sized!')
        layers = [inp]
        for i in range(len(self.options.NUM_FILTERS)):
            layers.append(
                self._conv2d(
                    layers[-1],
                    num_outputs=self.options.NUM_FILTERS[i],
                    rate=self.options.NUM_DILATIONS[i]))
        return layers

    def _conv2d(self, entree, num_outputs, rate):
        use_batch_norm = self.options.is_training is not None
        conv_layer = conv2d(
            entree,
            num_outputs=num_outputs,
            kernel_size=3,
            stride=1,
            padding='SAME',
            rate=rate,
            weights_regularizer=l2_regularizer(
                self.options.L2_REGULARIZATION_SCALE),
            activation_fn=None)
        return _maybe_add_batch_norm_or_activation_fn(
            conv_layer,
            use_batch_norm,
            self.options.is_training,
            activation_fn=tf.nn.leaky_relu)

    @staticmethod
    def _verify_input(entree, uv):
        log.check_eq(4, len(entree.shape))
        log.check_eq(4, len(uv.shape))
        log.check_eq(uv.shape[1:3], entree.shape[1:3])
        log.check_eq(2, uv.shape[3])


class ContextEstimatorOptions:
    def __init__(self):
        self.L2_REGULARIZATION_SCALE = GLOBAL_L2_REGULARIZATION
        self.NUM_FILTERS = [128, 128, 128, 96, 64, 32]
        self.NUM_DILATIONS = [1, 2, 4, 8, 16, 1]
        self.is_training = None

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class PWCNet:
    """
    Class that creates the network described in: arxiv.org/pdf/1709.02371.pdf
    """

    def __init__(self, x1, x2, options=None):
        self.options = PWCNetOptions() if options is None else options

        PWCNet._verify_input(x1, x2)
        # One would normalize and rescale CV_8UC3 images here.
        x1_float = PWCNet._convert_to_float_and_normalize(x1)
        x2_float = PWCNet._convert_to_float_and_normalize(x2)

        # Instantiate a feature extractor network. Weights of the two
        # towers should be shared.
        # Higher levels of the pyramid are 'more coarse'
        self.pyramid1 = FeaturePyramidExtractor(
            x1_float, opt=self.options.pyramid_opt)
        self.pyramid2 = FeaturePyramidExtractor(
            x2_float, opt=self.options.pyramid_opt)

        # Initializes a list of flow estimators at different levels.
        self.estimator_net = PWCNet._initialize_flow_estimators(
            self.pyramid1, self.pyramid2, self.options.estimator_opt)

        # Maybe initialize a network estimating 'context' (refined flow).
        if self.options.use_context_net:
            self.context_net = ContextEstimator(
                self.estimator_net[-1].get_penultimate_layer(),
                self.estimator_net[-1].get_flow(),
                opt=self.options.context_opt)

            PWCNet._verify_left_is_half_scale_of_right(
                self.context_net.get_flow().shape, x1.shape)
            self.output_flow = tf_utils.resample_flow(
                self.context_net.get_flow(), x1.shape)
        else:
            self.context_net = None
            self.output_flow = tf_utils.resample_flow(
                self.estimator_net[-1].get_flow(), x1.shape)

    def get_output_flow(self):
        """ Returns the final flow estimate. """
        return self.output_flow

    def get_raw_flow(self, level):
        """
        Returns an estimate of flow without context network applied to it.
        Larger levels correspond to finer-resolution estimates.
        """
        log.check(level >= 0 and level < len(self.estimator_net))
        return self.estimator_net[level].get_flow()

    def debug_info(self):
        print "Pyramid1:"
        self.pyramid1.debug_info()
        print "Pyramid2:"
        self.pyramid2.debug_info()
        for i, estimator in enumerate(self.estimator_net):
            print "Flow estimator {}:".format(i)
            estimator.debug_info()
        if self.context_net is not None:
            print "Context estimator:"
            context_net.debug_info()
        else:
            print "Context estimator is not instantiated."
        print "Output flow:", self.output_flow

    @staticmethod
    def _initialize_flow_estimators(pyramid1, pyramid2, options):
        log.check(isinstance(options, dict))

        batch_size = tf.shape(pyramid1.get_level(0))[0]
        # get the shape of the last level in the pyramid, and downscale it by
        # 2 to get the initial (null) flow shape.
        num_levels = pyramid1.num_levels()

        # Reverse levels, since this is how we wil lbe iterating over them
        # below.
        pyramid_levels_to_use = sorted(options.keys())
        pyramid_levels_to_use.reverse()

        smallest_level_shape = \
            pyramid1.get_level(pyramid_levels_to_use[0]).shape.as_list()
        initial_flow_shape = [
            batch_size, smallest_level_shape[1] / 2,
            smallest_level_shape[2] / 2, 2
        ]
        # Initialize zero flow.
        last_flow = tf.zeros(initial_flow_shape, dtype=tf.float32)

        # The very last (0-th) level for the pyramid is not used in the paper,
        # instead the flow is just upsampled by 2x. If it were used, the input
        # feature maps would have to be raw images (i.e. NxNx3).
        estimator_net = []
        for lvl in pyramid_levels_to_use:
            print lvl, pyramid1.get_level(lvl)
            if isinstance(options, dict):
                opts = options[lvl]
            else:
                opts = options
            estimator_net.append(
                OpticalFlowEstimator(
                    pyramid1.get_level(lvl),
                    pyramid2.get_level(lvl), last_flow, opts))
            last_flow = estimator_net[-1].get_flow()
        return estimator_net

    #@staticmethod
    #def _initialize_flow_estimators(pyramid1, pyramid2, options):
    #    batch_size = tf.shape(pyramid1.get_level(0))[0]
    #    # get the shape of the last level in the pyramid, and downscale it by
    #    # 2 to get the initial (null) flow shape.
    #    num_levels = pyramid1.num_levels()

    #    smallest_level_shape = pyramid1.get_level(num_levels -
    #                                              1).shape.as_list()
    #    initial_flow_shape = [
    #        batch_size, smallest_level_shape[1] / 2,
    #        smallest_level_shape[2] / 2, 2
    #    ]
    #    # Initialize zero flow.
    #    last_flow = tf.zeros(initial_flow_shape, dtype=tf.float32)

    #    # The very last (0-th) level for the pyramid is not used in the paper,
    #    # instead the flow is just upsampled by 2x. If it were used, the input
    #    # feature maps would have to be raw images (i.e. NxNx3).
    #    pyramid_levels_to_use = range(num_levels - 1, 0, -1)
    #    estimator_net = []
    #    for lvl in pyramid_levels_to_use:
    #        print lvl, pyramid1.get_level(lvl)
    #        if isinstance(options, dict):
    #            opts = options[lvl]
    #        else:
    #            opts = options
    #        estimator_net.append(
    #            OpticalFlowEstimator(
    #                pyramid1.get_level(lvl),
    #                pyramid2.get_level(lvl), last_flow, opts))
    #        last_flow = estimator_net[-1].get_flow()
    #    return estimator_net

    @staticmethod
    def _verify_input(x1, x2):
        log.check_eq(x1.dtype, tf.uint8)
        log.check_eq(x2.dtype, tf.uint8)
        log.check_eq(4, len(x1.shape))
        log.check_eq(4, len(x2.shape))
        log.check_eq(x1.shape[1:4].as_list(), x2.shape[1:4].as_list())
        log.check_eq(3, x1.shape[3], message="Must be a three channel image.")

    @staticmethod
    def _verify_left_is_half_scale_of_right(shape1, shape2):
        log.check_eq(len(shape1), len(shape2))
        log.check_eq(len(shape1), 4)
        log.check_eq(shape1[1], shape2[1] / 2)
        log.check_eq(shape1[2], shape2[2] / 2)

    @staticmethod
    def _convert_to_float_and_normalize(x):
        return (tf.cast(x, dtype='float32') - 128.0) / 128.0


class PWCNetOptions:
    def __init__(self):
        self.pyramid_opt = FeaturePyramidExtractorOptions()
        self.estimator_opt = OpticalFlowEstimatorOptions()
        self.context_opt = ContextEstimatorOptions()
        self.use_context_net = True
    
    @staticmethod
    def load(filename, is_training=None):
        opt = pickle.load(open(filename, 'rb'))
        log.check(isinstance(opt, PWCNetOptions))
        opt.set_is_training(is_training)
        return opt

    def dump(self, filename):
        pickle.dump(self, open(filename, 'wb'))

    def set_is_training(self, is_training=None):
        self.context_opt.is_training = is_training
        self.pyramid_opt.is_training = is_training
        if isinstance(self.estimator_opt, dict):
            for k in self.estimator_opt.keys():
                self.estimator_opt[k].is_training = is_training
        else:
            self.estimator_opt.is_training = is_training

    def __str__(self):
        estimator_opt_str = ''
        if isinstance(self.estimator_opt, dict):
            for k in sorted(self.estimator_opt.keys()):
                estimator_opt_str += '{}: {}\n\n'.format(k, self.estimator_opt[k])
        else:
            estimator_opt_str = '{}'.format(self.estimator_opt)
        return ("use_context_net: {}\n".format(self.use_context_net) +
                "context_opt: {}\n\n".format(self.context_opt.__str__()) + 
                "pyramid_opt: {}\n\n".format(self.pyramid_opt.__str__()) +
                estimator_opt_str)


class PWCNetTrainer:
    """
    Class that creates a PWC network and attaches training losses.
    USAGE:
    >>> trainer = PWCNetTrainer(x1, x2, y, training_options, net_options)
    >>> net = trainer.get_network() # returns the network (if you need if for
    >>>                             # some reason.
    >>> loss = trainer.get_loss()   # can be fed into session.run call.
    >>> # network options and training options can be inspected using the
    >>> # following two calls:
    >>> trainer.get_training_options()
    >>> trainer.get_pwc_options()
    """
    MAXIMUM_FLOW_VALUE = 50.0

    def __init__(self,
                 x1,
                 x2,
                 groundtruth,
                 weights=None,
                 train_options=None,
                 pwc_options=None):
        PWCNetTrainer._verify_inputs(x1, x2, groundtruth, weights)

        self.train_options = train_options if train_options is not None \
            else PWCNetTrainerOptions()
        self.pwc_options = pwc_options if pwc_options is not None \
            else PWCNetOptions()

        # Instantiate network.
        self.pwcnet = PWCNet(x1, x2, self.pwc_options)
        # Add training losses.
        self._add_training_loss(self.pwcnet, groundtruth, weights)
        # Add statistics for network layers.
        PWCNetTrainer._add_pwc_variable_summary(self.pwcnet)

    def get_loss(self):
        return self.total_loss

    def get_training_options(self):
        return self.train_options

    def get_pwc_options(self):
        return self.pwc_options

    def get_network(self):
        return self.pwcnet

    def get_output_flow(self):
        return self.pwcnet.get_output_flow()

    def get_magic_scale_value(self):
        return self.MAXIMUM_FLOW_VALUE

    def _initialize_scaled_groundtruth(self, pwcnet, groundtruth):
        # Initializes a map from size (height or width) to 'groundtruth' flow.
        self.groundtruth = {}

        dim = groundtruth.shape.as_list()[1]
        self.groundtruth[dim] = groundtruth

        # At this point we can apply some scaling factors to the flow.
        for estimator in pwcnet.estimator_net:
            p_shape = estimator.get_flow().shape.as_list()
            scale_x = p_shape[1] / float(groundtruth.shape.as_list()[1])
            scale_y = p_shape[2] / float(groundtruth.shape.as_list()[2])
            log.check_eq(scale_x, scale_y)

            dim = p_shape[1]
            self.groundtruth[dim] = tf_utils.resample_flow(groundtruth,
                                                           p_shape)

    def _add_training_loss(self, pwcnet, groundtruth, weights=None):
        """ Adds training losses """
        # Figure out how many
        self._initialize_scaled_groundtruth(pwcnet, groundtruth)

        self.endpoint_loss = PWCNetTrainer._get_endpoint_error_loss(
            pwcnet, self.train_options.LOSS_WEIGHTS, self.groundtruth, weights,
            self.train_options.USE_HUBER_LOSS)
        if self.train_options.USE_ANGULAR_LOSS:
            self.angular_loss = PWCNetTrainer._get_angular_error_loss(
                pwcnet, self.train_options.LOSS_WEIGHTS, self.groundtruth,
                weights)
        else:
            self.angular_loss = [tf.Variable(0.0, trainable=False)]

        self.regularization_loss = tf.losses.get_regularization_loss()
        tf.summary.scalar('regularization_loss', self.regularization_loss)

        self.total_loss = sum(self.angular_loss) + sum(
            self.endpoint_loss) + self.regularization_loss
        tf.summary.scalar('total_loss', self.total_loss)

    def get_loss(self):
        return self.total_loss

    @staticmethod
    def _verify_inputs(x1, x2, groundtruth, weights=None):
        log.check_eq(4, len(x1.shape))
        log.check_eq(4, len(x2.shape))
        log.check_eq(4, len(groundtruth.shape))
        log.check_eq(x1.shape[1:4], x2.shape[1:4])
        log.check_eq(x1.shape[1:3], groundtruth.shape[1:3])
        log.check_eq(2, groundtruth.shape[3])
        if weights is not None:
            log.check_eq(4, len(weights.shape))
            dlog.check_eq(x1.shape[1:3], weights.shape[1:3])

    @staticmethod
    def _add_pwc_variable_summary(net):
        """ Adds statistics for most interesting layers in the network. """
        with tf.name_scope('pyramid1'):
            for i in range(net.pyramid1.num_levels()):
                with tf.name_scope('level{}'.format(i)):
                    variable_summary(net.pyramid1.get_level(i))
        with tf.name_scope('pyramid2'):
            for i in range(net.pyramid2.num_levels()):
                with tf.name_scope('level{}'.format(i)):
                    variable_summary(net.pyramid2.get_level(i))
        for estimator_net in net.estimator_net:
            flow = estimator_net.get_flow()
            with tf.name_scope(
                    'flow_{}x{}'.format(flow.shape[1], flow.shape[2])):
                variable_summary(flow)

    @staticmethod
    def _get_endpoint_error_loss(net,
                                 loss_weights,
                                 groundtruths,
                                 weights=None,
                                 use_huber_loss=False):
        """ Returns scaled endpoint error losses. """
        losses = []
        log.check_eq(len(groundtruths), len(loss_weights))
        log.check_eq(len(net.estimator_net) + 1, len(loss_weights), \
            ("You do not have an appropriate number of loss weights. "
             "Should have {}".format(1 + len(net.estimator_net))))
        with tf.name_scope('endpoint_loss'):
            for i, w in enumerate(loss_weights):
                if i < len(loss_weights) - 1:
                    prediction = net.estimator_net[i].get_flow()
                else:
                    if net.options.use_context_net is False:
                        log.warn(
                            'Context network is not set up, so there is no ' +
                            'need to penalize flow at the finest resolution.')
                        break
                    prediction = net.get_output_flow()

                dim = prediction.shape.as_list()[1]
                loss_name = '{}x{}'.format(dim, dim)

                gt_at_scale = groundtruths[dim]
                log.check_eq(gt_at_scale.shape.as_list()[1],
                             prediction.shape.as_list()[1])
                log.check_eq(gt_at_scale.shape.as_list()[2],
                             prediction.shape.as_list()[2])

                if use_huber_loss:
                    loss = tf_utils.endpoint_huber_loss_at_scale(
                        prediction, gt_at_scale, weights) * w
                else:
                    loss = tf_utils.endpoint_loss_at_scale(
                        prediction, gt_at_scale, weights) * w

                tf.summary.scalar(loss_name, loss)
                losses.append(loss)
        return losses

    @staticmethod
    def _get_angular_error_loss(net, loss_weights, groundtruths, weights=None):
        """ Returns scaled angular error losses. """
        losses = []
        log.check_eq(len(groundtruths), len(loss_weights))
        log.check_eq(len(net.estimator_net), len(loss_weights) - 1, \
            "You do not have an appropriate number of loss weights.")
        RELATIVE_WEIGHT = 5.0

        with tf.name_scope('angular_loss'):
            for i, w in enumerate(loss_weights):
                if i < len(loss_weights) - 1:
                    prediction = net.estimator_net[i].get_flow()
                else:
                    if net.options.use_context_net is False:
                        log.warn(
                            'Context network is not set up, so there is no ' +
                            'need to penalize flow at the finest resolution.')
                        break
                    prediction = net.get_output_flow()

                dim = prediction.shape.as_list()[1]
                gt_at_scale = groundtruths[dim]
                loss_name = '{}x{}'.format(dim, dim)

                log.check_eq(gt_at_scale.shape.as_list()[1],
                             prediction.shape.as_list()[1])
                log.check_eq(gt_at_scale.shape.as_list()[2],
                             prediction.shape.as_list()[2])

                loss = tf_utils.angular_loss_at_scale(
                    prediction, gt_at_scale, weights) * w * RELATIVE_WEIGHT
                tf.summary.scalar(loss_name, loss)
                losses.append(loss)
        return losses


class PWCNetTrainerOptions:
    LOSS_WEIGHTS = [0.32, 0.08, 0.02, 0.01, 0.005]
    USE_ANGULAR_LOSS = True
    USE_HUBER_LOSS = None



def _maybe_add_batch_norm_or_activation_fn(entree,
                                           use_batch_norm=False,
                                           is_training=None,
                                           activation_fn=tf.nn.leaky_relu,
                                           reuse=None,
                                           scope=None,
                                           bn_epsilon=1e-2,
                                           bn_decay=0.9):
    """
    Either returns the provided activation function (e.g. ReLU) applied to the
    input, or applies batch norm and activation function and returns it.
    """
    if use_batch_norm:
        log.check(is_training is not None,
                  ('You specified that batch_norm should be used, but '
                   '"is_training" parameter was not set!'))
        return batch_norm(
            entree,
            epsilon=bn_epsilon,
            decay=bn_decay,
            activation_fn=activation_fn,
            is_training=is_training,
            reuse=reuse,
            scope=scope,
            updates_collections=None)
    else:
        return activation_fn(entree)
