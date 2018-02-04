import tensorflow as tf
from tf_utils import resample_flow, angular_flow_error, endpoint_flow_error

""" Class that instantiates a tensorflow net for computing optical flow,
    akin to https://arxiv.org/abs/1504.06852 but somewhat smaller, and
    probably with a worse choice of parameters.
    
    USAGE:
    
    >>> x1 = tf.placeholder(tf.float32, [None, 128, 128, 3], name='x1')
    >>> x2 = tf.placeholder(tf.float32, [None, 128, 128, 3], name='x2')
    >>> flownet = FlowNet(x1, x2)

    Outputs of the network (at different scales) are accessible by:
    
    >>> flownet.prediction

    If you are training the model, you should additionally do:
    
    >>> loss = flownet.set_loss(groundtruth, weights)

    and use the returned loss in the tf session.run call.
"""
class FlowNet:
    # Prediction layers. 
    predictions = []

    # Endpoint-error losses for different layers.
    endpoint_loss = []
    # Angular losses for different layers.
    angular_loss = []
    # Total loss used in training.
    total_loss = None


    # 0: 64x64, 1: 32x32, 2: 16x16, 3: 14x14, 4: 12x12, 5: 10x10
    conv = [[]]*6
    # 0: 128x128, 1: 64x64, 2: 32x32, 3: 16x16, 4: 14x14, 5: 12x12
    deconv = [[]]*6
    
    # Intermediate outputs.
    predict = [[]]*7
    
    # Weights for loss at each layer. Earlier entries in the array correspond
    # to larger patches, and seem to need smaller weights.
    loss_weights  = [0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0]
    # How much to weigh angular loss relative to the euclidean endpoint error.
    angular_loss_weight = 10.0

    def __init__(self, x1, x2, l2_scale=1e-2, normalize=True):
        from tensorflow.contrib.layers import conv2d
        from tensorflow.contrib.layers import conv2d_transpose
        from tensorflow.contrib.layers import max_pool2d
        from tensorflow.contrib.layers import fully_connected
        from tensorflow.contrib.layers import l2_regularizer
        if not x1.shape[1] == 128 or not x1.shape[2] == 128 or \
           not x2.shape[1] == 128 or not x2.shape[2] == 128:
            raise Exception('Input dimensions must be 128x128')
        
        
        x1 = tf.cast(x1, dtype='float32')
        x2 = tf.cast(x2, dtype='float32')
        if normalize:
            x1 = (x1 - 128.0)/128.0
            x2 = (x2 - 128.0)/128.0

        x_concat = tf.concat([x1, x2], axis=3)

        # NOTE: These do not follow the scales used in the paper.
        conv_outputs = [64, 64, 128, 256, 512, 512]
        deconv_outputs = [128, 192, 256, 256, 512, 512]
        # Add convolutional layers
        self.conv[0] = conv2d(x_concat,
                            num_outputs=conv_outputs[0],
                            kernel_size=3, stride=2, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale))
        self.conv[1] = conv2d(self.conv[0],
                            num_outputs=conv_outputs[1],
                            kernel_size=3, stride=2, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale))
        self.conv[2] = conv2d(self.conv[1],
                            num_outputs=conv_outputs[2],
                            kernel_size=3, stride=2, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale))
        self.conv[3] = conv2d(self.conv[2],
                            num_outputs=conv_outputs[3],
                            kernel_size=3, stride=1, padding='VALID',
                            weights_regularizer=l2_regularizer(l2_scale))
        self.conv[4] = conv2d(self.conv[3],
                            num_outputs=conv_outputs[4],
                            kernel_size=3, stride=1, padding='VALID',
                            weights_regularizer=l2_regularizer(l2_scale))
        self.conv[5] = conv2d(self.conv[4],
                            num_outputs=conv_outputs[5],
                            kernel_size=3, stride=1, padding='VALID',
                            weights_regularizer=l2_regularizer(l2_scale))
        # --------------------------- 10x10 -> 12x12 --------------------------
        self.deconv[5] = conv2d_transpose(self.conv[5],
                            num_outputs=deconv_outputs[5],
                            kernel_size=3, stride=1, padding='VALID',
                            weights_regularizer=l2_regularizer(l2_scale))
        self.predict[6] = conv2d(self.conv[5],
                            num_outputs=2, kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
       
        # --------------------------- 12x12 -> 14x14 --------------------------
        concat = self._concat_inputs(self.conv[4], self.deconv[5], self.predict[6])
        self.predict[5] = conv2d(concat,
                            num_outputs=2, kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        self.deconv[4] = conv2d_transpose(concat,
                            num_outputs=deconv_outputs[4],
                            kernel_size=3, stride=1, padding='VALID',
                            weights_regularizer=l2_regularizer(l2_scale))
        
        # --------------------------- 14x14 -> 16x16 --------------------------
        concat = self._concat_inputs(self.conv[3], self.deconv[4], self.predict[5])
        self.predict[4] = conv2d(concat,
                            num_outputs=2, kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        self.deconv[3] = conv2d_transpose(concat,
                            num_outputs=deconv_outputs[3],
                            kernel_size=3, stride=1, padding='VALID',
                            weights_regularizer=l2_regularizer(l2_scale))
        
        # --------------------------- 16x16 -> 32x32 --------------------------
        concat = self._concat_inputs(self.conv[2], self.deconv[3], self.predict[4])
        self.predict[3] = conv2d(concat,
                            num_outputs=2,
                            kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        self.deconv[2] = conv2d_transpose(concat,
                            num_outputs=deconv_outputs[2],
                            kernel_size=3, stride=2, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale))
        
        # --------------------------- 32x32 -> 64x64 --------------------------
        concat = self._concat_inputs(self.conv[1], self.deconv[2], self.predict[3])
        self.predict[2] = conv2d(concat,
                            num_outputs=2,
                            kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        self.deconv[1] = conv2d_transpose(concat,
                            num_outputs=deconv_outputs[1],
                            kernel_size=3, stride=2, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale))
        
        # -------------------------- 64x64 -> 128x128 -------------------------
        concat = self._concat_inputs(self.conv[0], self.deconv[1], self.predict[2])
        self.predict[1] = conv2d(concat,
                            num_outputs=2,
                            kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
       
        self.deconv[0] = conv2d_transpose(concat,
                            num_outputs=deconv_outputs[0],
                            kernel_size=3, stride=2, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        
        # prediction at 128x128
        concat = self._concat_inputs(x_concat, self.deconv[0], self.predict[1])
        self.predict[0] = conv2d(concat,
                            num_outputs=2,
                            kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
 
        # Add named identity layers.
        for i, layer in enumerate(self.predict):
            layer_name = 'prediction-{}x{}'.format(layer.shape[1], layer.shape[2])
            self.predictions.append(tf.identity(layer, name=layer_name))
       
    """ Utility function for building the network.
        Concatenates three inputs: convolution output, deconvolution output,
        and optical flow prediction from another layer.
        Optical flow prediction is 'resampled' as necessary (i.e. resized and
        values are rescaled).
    """
    def _concat_inputs(self, conv, deconv, prediction):
        imsize = [conv.shape[1], conv.shape[2]]
        prediction_resized = resample_flow(prediction, imsize)
        assert conv.shape[1] == deconv.shape[1] and \
                deconv.shape[1] == prediction_resized.shape[1]
        assert conv.shape[2] == deconv.shape[2] and \
                deconv.shape[2] == prediction_resized.shape[2]
        return tf.concat([conv, deconv, prediction_resized], axis=3)
    
    """ Calculates endpoint loss at a given scale.
        'groundtruth' and 'weights' are given at the original scale, while 
        prediction (optical flow) may be at a coarser scale. Loss is computed
        by downscaling groundtruth and weights.
    """
    @staticmethod
    def get_endpoint_loss_at_scale(prediction, groundtruth, weights=None):
        if not prediction.shape == groundtruth.shape:
            sz = [prediction.shape[1], prediction.shape[2]]
            groundtruth_scaled = resample_flow(groundtruth, prediction.shape)
            if weights is not None:
                weights_scaled = tf.image.resize_images(weights, sz)
            else:
                weights_scaled = None
            return tf.reduce_mean(endpoint_flow_error(
                prediction, groundtruth_scaled, weights_scaled))
        else:
            return tf.reduce_mean(endpoint_flow_error(
                prediction, groundtruth, weights))

    """ Returns the angular loss at a given scale.
        'groundtruth' and 'weights' are given at the original scale, while 
        prediction (optical flow) may be at a coarser scale. Loss is computed
        by downscaling groundtruth and weights.
    """
    @staticmethod
    def get_angular_loss_at_scale(prediction, groundtruth, weights=None):
        if not prediction.shape == groundtruth.shape:
            sz = [prediction.shape[1], prediction.shape[2]]
            if weights is not None:
                weights_scaled = tf.image.resize_images(weights, sz)
            else:
                weights_scaled = None
            groundtruth_scaled = resample_flow(groundtruth, prediction.shape)
            return tf.reduce_mean(angular_flow_error(
                    groundtruth_scaled, prediction, weights_scaled))
        else:
            return tf.reduce_mean(angular_flow_error(groundtruth, prediction, weights))

    """ Sets and returns loss for training. """
    def set_loss(self, groundtruth, weights=None):
        # Add endpoint losses.
        for i, prediction in enumerate(self.predict):
            loss_name = 'endpoint_loss-{}x{}'.format(
                    prediction.shape[1], prediction.shape[2])
            loss = FlowNet.get_endpoint_loss_at_scale(\
                    prediction, groundtruth, weights) * FlowNet.loss_weights[i]
            tf.summary.scalar(loss_name, loss)
            self.endpoint_loss.append(loss)
        
        # Add angular losses.
        for i, prediction in enumerate(self.predict):
            loss_name = 'angular_loss-{}x{}'.format(
                    prediction.shape[1], prediction.shape[2])
            w = FlowNet.loss_weights[i] * FlowNet.angular_loss_weight
            loss = FlowNet.get_angular_loss_at_scale(\
                    self.predict[i], groundtruth, weights) * w
            tf.summary.scalar(loss_name, loss)
            self.angular_loss.append(loss)

        self.total_loss = sum(self.angular_loss) + sum(self.endpoint_loss) 
        tf.summary.scalar('total_loss', self.total_loss)

        return self.total_loss


