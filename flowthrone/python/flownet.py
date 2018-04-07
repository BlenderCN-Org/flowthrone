# Add parent directory to pythonpath.
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tensorflow as tf
from tf_utils import resample_flow, angular_flow_error, endpoint_flow_error, l2_warp_error
import warnings


class FlowNetConfig:
    """ Configuration for instantiating/training FlowNet network. """
    # Weights applied to different layers (from high res to low res).
    loss_weights = [0.25, 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0]
    # Weight applied to angular loss.
    angular_loss_weight = 5.0
    # L2 regularization on the filters.
    l2_scale = 1e-2
    # Whether the network should normalize images to be in [-1, 1].
    normalize_input = True
    # Whether batch norm should be used or not.
    use_batch_norm = False


class FlowNet:
    """
    Class that instantiates a tensorflow net for computing optical flow,
    akin to https://arxiv.org/abs/1504.06852 but somewhat smaller.
    USAGE:

    >>> x1 = tf.placeholder(tf.float32, [None, 128, 128, 3], name='x1')
    >>> x2 = tf.placeholder(tf.float32, [None, 128, 128, 3], name='x2')
    >>> flownet = FlowNet(x1, x2)

    Outputs of the network (at different scales) are accessible by:

    >>> flownet.prediction

    If you are training the model, you should additionally do:

    >>> flownet.set_angular_error_loss(groundtruth, weights)
    >>> flownet.set_endpoint_error_loss(groundtruth, weights)
    >>> flownet.set_brightness_constancy_violation_loss(weights)
    >>> loss = flownet.get_loss()

    and use the returned loss in the tf session.run call.
    If it not necessary to use all losses (you may avoid using angular loss,
    or BCC violation loss, for example).

    Note that some losses require supervision (i.e. groundtruth flow), and
    some do not (e.g. BCC constraint violation).
    """

    # Prediction layers.
    predictions = []

    # Endpoint-error losses for different layers.
    endpoint_loss = []
    # Angular losses for different layers.
    angular_loss = []
    # Warping error.
    brightness_constancy_error_loss = []

    # Total loss used in training.
    total_loss = None

    x1 = None
    x2 = None

    # 0: 128x128, 1: 64x64, 2: 32x32, 3: 16x16, 4: 14x14, 5: 12x12, 6: 10x10
    conv = [[]] * 7
    # 0: 256x256, 1: 128x128, 2: 64x64, 3: 32x32, 4: 16x16, 5: 14x14, 6: 12x12
    deconv = [[]] * 7

    # Intermediate outputs.
    predict = [[]] * 8

    is_training = None
    config = None

    def __init__(self, x1, x2, is_training=None, config=FlowNetConfig()):
        from tensorflow.contrib.layers import conv2d
        from tensorflow.contrib.layers import conv2d_transpose
        from tensorflow.contrib.layers import max_pool2d
        from tensorflow.contrib.layers import fully_connected
        from tensorflow.contrib.layers import l2_regularizer
        from tensorflow.contrib.layers import batch_norm
        # Should think how to generalize this a little bit, as it's getting
        # ridiculous otherwise.
        if not x1.shape[1] == 256 or not x1.shape[2] == 256 or \
           not x2.shape[1] == 256 or not x2.shape[2] == 256:
            raise Exception('Input dimensions must be 256x256')

        self.config = config
        self.config.use_batch_norm = is_training is not None
        self.is_training = is_training

        self.x1 = tf.cast(x1, dtype='float32')
        self.x2 = tf.cast(x2, dtype='float32')
        if self.config.normalize_input:
            self.x1 = (self.x1 - 128.0) / 128.0
            self.x2 = (self.x2 - 128.0) / 128.0

        x_concat = tf.concat([self.x1, self.x2], axis=3)

        # NOTE: These do not follow the scales used in the paper.
        conv_outputs = [64, 64, 64, 64, 128, 256, 512, 512]
        deconv_outputs = [128, 128, 128, 256, 256, 512, 512]
        # Add convolutional layers
        index = 0
        self.conv[index] = self._add_conv2d_relu(
            x_concat,
            num_outputs=conv_outputs[index],
            kernel_size=3,
            stride=2,
            padding='SAME')

        index = 1
        self.conv[index] = self._add_conv2d_relu(
            self.conv[index - 1],
            num_outputs=conv_outputs[index],
            kernel_size=3,
            stride=2,
            padding='SAME')

        index = 2
        self.conv[index] = self._add_conv2d_relu(
            self.conv[index - 1],
            num_outputs=conv_outputs[index],
            kernel_size=3,
            stride=2,
            padding='SAME')

        index = 3
        self.conv[index] = self._add_conv2d_relu(
            self.conv[index - 1],
            num_outputs=conv_outputs[index],
            kernel_size=3,
            stride=2,
            padding='SAME')

        index = 4
        self.conv[index] = self._add_conv2d_relu(
            self.conv[index - 1],
            num_outputs=conv_outputs[index],
            kernel_size=3,
            stride=1,
            padding='VALID')

        index = 5
        self.conv[index] = self._add_conv2d_relu(
            self.conv[index - 1],
            num_outputs=conv_outputs[index],
            kernel_size=3,
            stride=1,
            padding='VALID')

        index = 6
        self.conv[index] = self._add_conv2d_relu(
            self.conv[index - 1],
            num_outputs=conv_outputs[index],
            kernel_size=3,
            stride=1,
            padding='VALID')

        index = 7
        self.predict[index] = conv2d(
            self.conv[index - 1],
            num_outputs=2,
            kernel_size=3,
            stride=1,
            padding='SAME',
            weights_regularizer=l2_regularizer(self.config.l2_scale),
            activation_fn=None)

        # --------------------------- 10x10 -> 12x12 --------------------------
        index = 6
        self.deconv[index] = self._add_con2d_transpose_relu(
            self.conv[index],
            num_outputs=deconv_outputs[index],
            kernel_size=3,
            stride=1,
            padding='VALID')

        # --------------------------- 12x12 -> 14x14 --------------------------
        index = 6
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(
            concat,
            num_outputs=2,
            kernel_size=3,
            stride=1,
            padding='SAME',
            weights_regularizer=l2_regularizer(self.config.l2_scale),
            activation_fn=None)
        self.deconv[index - 1] = self._add_con2d_transpose_relu(
            concat,
            num_outputs=deconv_outputs[index - 1],
            kernel_size=3,
            stride=1,
            padding='VALID')

        # --------------------------- 14x14 -> 16x16 --------------------------
        index = 5
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(
            concat,
            num_outputs=2,
            kernel_size=3,
            stride=1,
            padding='SAME',
            weights_regularizer=l2_regularizer(self.config.l2_scale),
            activation_fn=None)
        self.deconv[index - 1] = self._add_con2d_transpose_relu(
            concat,
            num_outputs=deconv_outputs[index - 1],
            kernel_size=3,
            stride=1,
            padding='VALID')
        # --------------------------- 16x16 -> 32x32 --------------------------
        index = 4
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(
            concat,
            num_outputs=2,
            kernel_size=3,
            stride=1,
            padding='SAME',
            weights_regularizer=l2_regularizer(self.config.l2_scale),
            activation_fn=None)
        self.deconv[index - 1] = self._add_con2d_transpose_relu(
            concat,
            num_outputs=deconv_outputs[index - 1],
            kernel_size=3,
            stride=2,
            padding='SAME')

        # --------------------------- 32x32 -> 64x64 --------------------------
        index = 3
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(
            concat,
            num_outputs=2,
            kernel_size=3,
            stride=1,
            padding='SAME',
            weights_regularizer=l2_regularizer(self.config.l2_scale),
            activation_fn=None)
        self.deconv[index - 1] = self._add_con2d_transpose_relu(
            concat,
            num_outputs=deconv_outputs[index - 1],
            kernel_size=3,
            stride=2,
            padding='SAME')

        # -------------------------- 64x64 -> 128x128 -------------------------
        index = 2
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(
            concat,
            num_outputs=2,
            kernel_size=3,
            stride=1,
            padding='SAME',
            weights_regularizer=l2_regularizer(self.config.l2_scale),
            activation_fn=None)
        self.deconv[index - 1] = self._add_con2d_transpose_relu(
            concat,
            num_outputs=deconv_outputs[index - 1],
            kernel_size=3,
            stride=2,
            padding='SAME')

        # -------------------------- 128x128 -> 256x256 -------------------------
        index = 1
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(
            concat,
            num_outputs=2,
            kernel_size=3,
            stride=1,
            padding='SAME',
            weights_regularizer=l2_regularizer(self.config.l2_scale),
            activation_fn=None)
        self.deconv[index - 1] = self._add_con2d_transpose_relu(
            concat,
            num_outputs=deconv_outputs[index - 1],
            kernel_size=3,
            stride=2,
            padding='SAME')

        # prediction at the original resolution.
        concat = self._concat_inputs(x_concat, self.deconv[0], self.predict[1])
        self.predict[0] = conv2d(
            concat,
            num_outputs=2,
            kernel_size=3,
            stride=1,
            padding='SAME',
            weights_regularizer=l2_regularizer(self.config.l2_scale),
            activation_fn=None)

        # Add named identity layers.
        for i, layer in enumerate(self.predict):
            layer_name = 'prediction-{}x{}'.format(layer.shape[1],
                                                   layer.shape[2])
            self.predictions.append(tf.identity(layer, name=layer_name))

    def _concat_conv_deconv_predict(self, index):
        return self._concat_inputs(self.conv[index - 1], self.deconv[index],
                                   self.predict[index + 1])

    def _add_conv2d_relu(self, layer, num_outputs, kernel_size, stride,
                         padding):
        """ Adds and returns conv2d and relu/batch norm """
        from tensorflow.contrib.layers import conv2d
        from tensorflow.contrib.layers import l2_regularizer
        out = conv2d(
            layer,
            num_outputs=num_outputs,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            weights_regularizer=l2_regularizer(self.config.l2_scale),
            activation_fn=None)
        return self._add_batch_norm_or_relu(out, self.config.use_batch_norm,
                                            self.is_training)

    def _add_con2d_transpose_relu(self, layer, num_outputs, kernel_size,
                                  stride, padding):
        """ Adds and returns conv2d_transpose and relu/batch norm """
        from tensorflow.contrib.layers import conv2d_transpose
        from tensorflow.contrib.layers import l2_regularizer
        out = conv2d_transpose(
            layer,
            num_outputs=num_outputs,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            weights_regularizer=l2_regularizer(self.config.l2_scale),
            activation_fn=None)
        return self._add_batch_norm_or_relu(out, self.config.use_batch_norm,
                                            self.is_training)

    def _add_batch_norm_or_relu(self,
                                layer,
                                use_batch_norm=False,
                                is_training=None):
        """ Adds and returns a batch norm layer, or returns a ReLU layer. """
        kEpsilon = 1e-2
        kDecay = 0.9999
        from tensorflow.contrib.layers import batch_norm
        if use_batch_norm:
            return batch_norm(
                layer,
                epsilon=kEpsilon,
                decay=kDecay,
                activation_fn=tf.nn.relu,
                is_training=is_training,
                updates_collections=None)
        else:
            return tf.nn.relu(layer)

    def set_endpoint_error_loss(self, groundtruth, weights=None):
        """ Sets endpoint error loss. This function can be called only once. """
        assert len(self.endpoint_loss) == 0, "Endpoint loss is already set?"
        for i, prediction in enumerate(self.predict):
            loss_name = 'endpoint_loss-{}x{}'.format(prediction.shape[1],
                                                     prediction.shape[2])
            loss_weight = self.config.loss_weights[i]
            loss = FlowNet.get_endpoint_loss_at_scale(\
                    prediction, groundtruth, weights) * loss_weight
            tf.summary.scalar(loss_name, loss)
            self.endpoint_loss.append(loss)
        return self.get_loss()

    def set_angular_error_loss(self, groundtruth, weights=None):
        """ Sets angular error loss. This function can be called only once. """
        assert len(self.angular_loss) == 0, "Angular loss is already set?"
        for i, prediction in enumerate(self.predict):
            loss_name = 'angular_loss-{}x{}'.format(prediction.shape[1],
                                                    prediction.shape[2])
            loss_weight = self.config.loss_weights[
                i] * self.config.angular_loss_weight
            loss = FlowNet.get_angular_loss_at_scale(\
                    self.predict[i], groundtruth, weights) * loss_weight
            tf.summary.scalar(loss_name, loss)
            self.angular_loss.append(loss)
        return self.get_loss()

    def set_brightness_constancy_violation_loss(self, weights=None):
        """ Sets brightness-constancy-constraint violation loss.
            This function can be called only once. """
        warnings.warn("This feature is experimental", Warning)

        kWarpLossScale = 50
        loss_name = 'interpolation_loss-{}x{}'.format(self.predict[0].shape[1],
                                                      self.predict[0].shape[2])
        loss = tf.reduce_mean(
            l2_warp_error(self.x1, self.x2, self.predict[0],
                          weights)) * kWarpLossScale
        self.brightness_constancy_error_loss.append(loss)
        tf.summary.scalar(loss_name, loss)
        return self.get_loss()

    def get_loss(self):
        """ Returns loss used for training. """
        self.total_loss = \
                sum(self.angular_loss) + \
                sum(self.endpoint_loss) + \
                sum(self.brightness_constancy_error_loss)
        tf.summary.scalar('total_loss', self.total_loss)
        return self.total_loss

    def _concat_inputs(self, conv, deconv, prediction):
        """
        Utility function for building the network.
        Concatenates three inputs: convolution output, deconvolution output,
        and optical flow prediction from another layer.
        Optical flow prediction is 'resampled' as necessary (i.e. resized and
        values are rescaled).
        """
        imsize = [conv.shape[1], conv.shape[2]]
        prediction_resized = resample_flow(prediction, imsize)
        assert conv.shape[1] == deconv.shape[1] and \
                deconv.shape[1] == prediction_resized.shape[1]
        assert conv.shape[2] == deconv.shape[2] and \
                deconv.shape[2] == prediction_resized.shape[2]
        return tf.concat([conv, deconv, prediction_resized], axis=3)

    @staticmethod
    def get_endpoint_loss_at_scale(prediction, groundtruth, weights=None):
        """
        Calculates endpoint loss at a given scale.
        'groundtruth' and 'weights' are given at the original scale, while
        prediction (optical flow) may be at a coarser scale. Loss is computed
        by downscaling groundtruth and weights.
        """
        if not prediction.shape == groundtruth.shape:
            sz = [prediction.shape[1], prediction.shape[2]]
            groundtruth_scaled = resample_flow(groundtruth, prediction.shape)
            if weights is not None:
                weights_scaled = tf.image.resize_images(weights, sz)
            else:
                weights_scaled = None
            return tf.reduce_mean(
                endpoint_flow_error(prediction, groundtruth_scaled,
                                    weights_scaled))
        else:
            return tf.reduce_mean(
                endpoint_flow_error(prediction, groundtruth, weights))

    @staticmethod
    def get_angular_loss_at_scale(prediction, groundtruth, weights=None):
        """
        Returns the angular loss at a given scale.
        'groundtruth' and 'weights' are given at the original scale, while
        prediction (optical flow) may be at a coarser scale. Loss is computed
        by downscaling groundtruth and weights.
        """
        if not prediction.shape == groundtruth.shape:
            sz = [prediction.shape[1], prediction.shape[2]]
            if weights is not None:
                weights_scaled = tf.image.resize_images(weights, sz)
            else:
                weights_scaled = None
            groundtruth_scaled = resample_flow(groundtruth, prediction.shape)
            return tf.reduce_mean(
                angular_flow_error(groundtruth_scaled, prediction,
                                   weights_scaled))
        else:
            return tf.reduce_mean(
                angular_flow_error(groundtruth, prediction, weights))
