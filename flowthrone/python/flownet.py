# Add parent directory to pythonpath.                                           
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tensorflow as tf
from tf_utils import resample_flow, angular_flow_error, endpoint_flow_error


""" Class that instantiates a tensorflow net for computing optical flow,
    akin to https://arxiv.org/abs/1504.06852 but somewhat smaller.
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


    # 0: 128x128, 1: 64x64, 2: 32x32, 3: 16x16, 4: 14x14, 5: 12x12, 6: 10x10
    conv = [[]]*7
    # 0: 256x256, 1: 128x128, 2: 64x64, 3: 32x32, 4: 16x16, 5: 14x14, 6: 12x12
    deconv = [[]]*7
    
    # Intermediate outputs.
    predict = [[]]*8
    loss_weights  = [0.25, 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0]
    angular_loss_weight = 5.0
    l2_scale = 1e-2
    is_training = None
    use_batch_norm = False

    def __init__(self, x1, x2, use_batch_norm = False,
                 is_training = None, l2_scale=1e-2, normalize=True):
        from tensorflow.contrib.layers import conv2d
        from tensorflow.contrib.layers import conv2d_transpose
        from tensorflow.contrib.layers import max_pool2d
        from tensorflow.contrib.layers import fully_connected
        from tensorflow.contrib.layers import l2_regularizer
        from tensorflow.contrib.layers import batch_norm
        # Should think hwo to generalize this a little bit, as it's getting
        # ridiculous otherwise.
        if not x1.shape[1] == 256 or not x1.shape[2] == 256 or \
           not x2.shape[1] == 256 or not x2.shape[2] == 256:
            raise Exception('Input dimensions must be 256x256')
        
        self.l2_scale = l2_scale
        self.is_training = is_training
        self.use_batch_norm = use_batch_norm

        x1 = tf.cast(x1, dtype='float32')
        x2 = tf.cast(x2, dtype='float32')
        if normalize:
            x1 = (x1 - 128.0)/128.0
            x2 = (x2 - 128.0)/128.0

        x_concat = tf.concat([x1, x2], axis=3)

        # NOTE: These do not follow the scales used in the paper.
        conv_outputs = [64, 64, 64, 64, 128, 256, 512, 512]
        deconv_outputs = [128, 128, 128, 256, 256, 512, 512]
        # Add convolutional layers
        index = 0
        self.conv[index] = self._add_conv2d_relu(
                x_concat, 
                num_outputs=conv_outputs[index], 
                kernel_size=3, stride=2, padding='SAME')

        index = 1
        self.conv[index] = self._add_conv2d_relu(
                self.conv[index-1], 
                num_outputs=conv_outputs[index], 
                kernel_size=3, stride=2, padding='SAME')

        index = 2
        self.conv[index] = self._add_conv2d_relu(
                self.conv[index-1], 
                num_outputs=conv_outputs[index], 
                kernel_size=3, stride=2, padding='SAME')
        
        index = 3
        self.conv[index] = self._add_conv2d_relu(
                self.conv[index-1], 
                num_outputs=conv_outputs[index], 
                kernel_size=3, stride=2, padding='SAME')
        
        index = 4
        self.conv[index] = self._add_conv2d_relu(
                self.conv[index-1], 
                num_outputs=conv_outputs[index], 
                kernel_size=3, stride=1, padding='VALID')
       
        index = 5
        self.conv[index] = self._add_conv2d_relu(
                self.conv[index-1], 
                num_outputs=conv_outputs[index], 
                kernel_size=3, stride=1, padding='VALID')
       
        index = 6
        self.conv[index] = self._add_conv2d_relu(
                self.conv[index-1], 
                num_outputs=conv_outputs[index], 
                kernel_size=3, stride=1, padding='VALID')
       
        index = 7
        self.predict[index] = conv2d(self.conv[index-1],
                            num_outputs=2, kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
 
        # --------------------------- 10x10 -> 12x12 --------------------------
        index = 6
        self.deconv[index] = self._add_con2d_transpose_relu(
                self.conv[index], num_outputs=deconv_outputs[index],
                kernel_size=3, stride=1, padding='VALID')
      
        # --------------------------- 12x12 -> 14x14 --------------------------
        index = 6
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(concat,
                            num_outputs=2, kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        self.deconv[index-1] = self._add_con2d_transpose_relu(
                concat, num_outputs=deconv_outputs[index-1],
                kernel_size=3, stride=1, padding='VALID')
      
        # --------------------------- 14x14 -> 16x16 --------------------------
        index = 5
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(concat,
                            num_outputs=2, kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        self.deconv[index-1] = self._add_con2d_transpose_relu(
                concat, num_outputs=deconv_outputs[index-1],
                kernel_size=3, stride=1, padding='VALID')
        # --------------------------- 16x16 -> 32x32 --------------------------
        index = 4
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(concat,
                            num_outputs=2,
                            kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        self.deconv[index-1] = self._add_con2d_transpose_relu(
                concat, num_outputs=deconv_outputs[index-1],
                kernel_size=3, stride=2, padding='SAME')
        
        # --------------------------- 32x32 -> 64x64 --------------------------
        index = 3
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(concat,
                            num_outputs=2,
                            kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        self.deconv[index-1] = self._add_con2d_transpose_relu(
                concat, num_outputs=deconv_outputs[index-1],
                kernel_size=3, stride=2, padding='SAME')
        
        # -------------------------- 64x64 -> 128x128 -------------------------
        index = 2
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(concat,
                            num_outputs=2,
                            kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        self.deconv[index-1] = self._add_con2d_transpose_relu(
                concat, num_outputs=deconv_outputs[index-1],
                kernel_size=3, stride=2, padding='SAME')
        
        # -------------------------- 128x128 -> 256x256 -------------------------
        index = 1
        concat = self._concat_conv_deconv_predict(index)
        self.predict[index] = conv2d(concat,
                            num_outputs=2,
                            kernel_size=3, stride=1, padding='SAME',
                            weights_regularizer=l2_regularizer(l2_scale),
                            activation_fn=None)
        self.deconv[index-1] = self._add_con2d_transpose_relu(
                concat, num_outputs=deconv_outputs[index-1],
                kernel_size=3, stride=2, padding='SAME')
        
        # prediction at the original resolution.
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
     
    def _concat_conv_deconv_predict(self, index):
        return self._concat_inputs(self.conv[index-1], self.deconv[index], self.predict[index+1])

    """ Adds and returns conv2d and relu/batch norm """
    def _add_conv2d_relu(self, layer, num_outputs, kernel_size, stride, padding):
        from tensorflow.contrib.layers import conv2d
        from tensorflow.contrib.layers import l2_regularizer
        out = conv2d(layer,
                     num_outputs=num_outputs,
                     kernel_size=kernel_size, stride=stride, padding=padding,
                     weights_regularizer=l2_regularizer(self.l2_scale),
                     activation_fn=None)
        return self.add_batch_norm_or_relu(out, self.use_batch_norm, self.is_training)

    """ Adds and returns conv2d_transpose and relu/batch norm """
    def _add_con2d_transpose_relu(self, layer, num_outputs, kernel_size, stride, padding):
        from tensorflow.contrib.layers import conv2d_transpose
        from tensorflow.contrib.layers import l2_regularizer
        out = conv2d_transpose(layer,
                            num_outputs=num_outputs,
                            kernel_size=kernel_size, stride=stride, padding=padding,
                            weights_regularizer=l2_regularizer(self.l2_scale),
                            activation_fn=None)
        return self.add_batch_norm_or_relu(out, self.use_batch_norm, self.is_training)
 


    """ Adds and returns a batch norm layer, or returns a ReLU layer. """
    def add_batch_norm_or_relu(self, layer, use_batch_norm=False, is_training=None):
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
            loss = FlowNet.get_angular_loss_at_scale(\
                    self.predict[i], groundtruth, weights) * FlowNet.loss_weights[i] * FlowNet.angular_loss_weight
            tf.summary.scalar(loss_name, loss)
            self.angular_loss.append(loss)

        self.total_loss = sum(self.angular_loss) + sum(self.endpoint_loss) 
        tf.summary.scalar('total_loss', self.total_loss)

        return self.total_loss

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

    """ Returns the angular loss. """
    @staticmethod
    def get_angular_loss(prediction, groundtruth, weights):
        raise NotImplementedError


    """ Calculates endpoint loss at multiple scales.
        'groundtruth' and 'weights' are provided at the original scale, while 
        'predictions' is a list of predictions at various scales.
    """
    @staticmethod
    def get_endpoint_loss(predictions, groundtruth, weights):
        # Sort predictions so that smaller scales appear first.
        predictions.sort(key=lambda x : x.shape.as_list()[1]*x.shape.as_list()[2])
        losses = [FlowNet.endpoint_loss_at_scale(
            prediction, groundtruth, weights) for prediction in predictions]
        loss = 0
        for weight, loss in zip(FlowNet.loss_weights, losses):
            loss += weight * loss
        return loss
