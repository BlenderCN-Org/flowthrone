import tensorflow as tf

""" Rescales flow field. """
def resample_flow(uv, out_shape):
    assert uv.shape[3] == 2, "Flow field must have two channels!"
    uv_shape = uv.get_shape().as_list()
    if len(out_shape) == 4:
        out_shape = [int(out_shape[1]), int(out_shape[2])]
    elif len(out_shape) == 2:
        out_shape = [int(out_shape[0]), int(out_shape[1])]
    else:
        raise Exception('Could not interpret shape argument.')
    scale_x = out_shape[0] / float(uv_shape[1])
    scale_y = out_shape[1] / float(uv_shape[2])
    assert scale_x == scale_y, \
            "Currently flow resampling can only be isotropic."
    return tf.image.resize_images(uv, [out_shape[0], out_shape[1]]) * scale_x

""" Computes angular error between two flow fields 'x' and 'y', with weights
    given by 'w' (typically the weights will be 0 in occluded regions, and 1
    otherwise)
    If you do not have 'weights' or an occlusion mask, consider passing None
    instead of "np.ones" for reasons of speed.
"""
def angular_flow_error(x, y, w=None):
    assert x.shape[3] == 2, "Flow field must have two channels!"
    assert y.shape[3] == 2, "Flow field must have two channels!"
    epsilon = 1e-2 
    num = 1.0 + x[:,:,:,0] * y[:,:,:,0] + x[:,:,:,1] * y[:,:,:,1]
    den1 = tf.sqrt(1.0 + x[:,:,:,0] * x[:,:,:,0] + 
                         x[:,:,:,1] * x[:,:,:,1] + epsilon)
    den2 = tf.sqrt(1.0 + y[:,:,:,0] * y[:,:,:,0] + 
                         y[:,:,:,1] * y[:,:,:,1] + epsilon)
    lo_bound = -1.0 + epsilon
    hi_bound = 1.0 - epsilon
    ratio = tf.maximum(lo_bound, tf.minimum(hi_bound, num/(epsilon + den1*den2)))
    #ratio = num/(den1*den2)
    if w is not None:
        return tf.acos(ratio) * tf.reduce_mean(w, axis=3)
    else:
        return tf.acos(ratio)

""" Returns squared euclidean error over the flow field. """
def endpoint_flow_error(prediction, groundtruth, weights=None):
    if weights is not None:
        return weights * (prediction - groundtruth)**2
    else:
        return (prediction - groundtruth)**2


