import tensorflow as tf


def resample_flow(uv, out_shape):
    """ Rescales flow field. """
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


def angular_flow_error(x, y, w=None):
    """
    Computes angular error between two flow fields 'x' and 'y', with weights
    given by 'w' (typically the weights will be 0 in occluded regions, and 1
    otherwise)
    If you do not have 'weights' or an occlusion mask, consider passing None
    instead of "np.ones" for reasons of speed.
    """
    assert x.shape[3] == 2, "Flow field must have two channels!"
    assert y.shape[3] == 2, "Flow field must have two channels!"
    epsilon = 1e-2
    num = 1.0 + x[:, :, :, 0] * y[:, :, :, 0] + x[:, :, :, 1] * y[:, :, :, 1]
    den1 = tf.sqrt(1.0 + x[:, :, :, 0] * x[:, :, :, 0] +
                   x[:, :, :, 1] * x[:, :, :, 1] + epsilon)
    den2 = tf.sqrt(1.0 + y[:, :, :, 0] * y[:, :, :, 0] +
                   y[:, :, :, 1] * y[:, :, :, 1] + epsilon)
    lo_bound = -1.0 + epsilon
    hi_bound = 1.0 - epsilon
    ratio = tf.maximum(lo_bound,
                       tf.minimum(hi_bound, num / (epsilon + den1 * den2)))
    #ratio = num/(den1*den2)
    if w is not None:
        return tf.acos(ratio) * tf.reduce_mean(w, axis=3)
    else:
        return tf.acos(ratio)


def endpoint_flow_error(prediction, groundtruth, weights=None):
    """ Returns squared euclidean error over the flow field. """
    if weights is not None:
        return weights * (prediction - groundtruth)**2
    else:
        return (prediction - groundtruth)**2


def compute_residual(images0, images1, uv):
    """ Computes residual for a given optical flow: I0(x) - I1(w(x)) """
    assert images0.dtype == images1.dtype
    return images0 - warp_with_flow(images1, uv)


def l2_warp_error(images0, images1, uv, weights=None):
    """ Returns L2 squared 'interpolation error' """
    if weights is not None:
        return weights * compute_residual(images0, images1, uv)**2
    else:
        return compute_residual(images0, images1, uv)**2


def warp_with_flow(images, uv):
    """ Warps a batch of images (a 4D tensor) by the provided optical flow. """
    assert images.dtype == uv.dtype
    assert len(images.shape) == 4, "Tensor must have four dimensions!"
    assert len(uv.shape) == 4, "Tensor must have four dimensions!"
    assert uv.shape[3] == 2, "Flow field must have two channels!"

    height = images.shape[1]
    width = images.shape[2]
    flow = _get_flow_grid(uv)
    x = flow[:, :, :, 0]
    y = flow[:, :, :, 1]

    x0, y0, x1, y1 = _get_query_points(x, y)

    ## Get pixel value at corner coords
    Ia = _get_pixel_values(images, x0, y0)
    Ib = _get_pixel_values(images, x0, y1)
    Ic = _get_pixel_values(images, x1, y0)
    Id = _get_pixel_values(images, x1, y1)

    ## Recast as float for delta calculation.
    x0 = tf.cast(x0, images.dtype)
    x1 = tf.cast(x1, images.dtype)
    y0 = tf.cast(y0, images.dtype)
    y1 = tf.cast(y1, images.dtype)

    # Calculate weights.
    wa = (x1 - x) * (y1 - y)
    wb = (x1 - x) * (y - y0)
    wc = (x - x0) * (y1 - y)
    wd = (x - x0) * (y - y0)

    # Add dimension for addition.
    wa = tf.expand_dims(wa, axis=3)
    wb = tf.expand_dims(wb, axis=3)
    wc = tf.expand_dims(wc, axis=3)
    wd = tf.expand_dims(wd, axis=3)

    return tf.add_n([wa * Ia, wb * Ib, wc * Ic, wd * Id])


def _get_flow_grid(uv):
    """ Returns a 4D tensor representing with values out(x) = x + uv(x)
        USERS SHOULD NOT BE CALLING THIS FUNCTION.
    """
    assert len(uv.shape) == 4, "Tensor must have four dimensions!"
    assert uv.shape[3] == 2, "Flow field must have two channels!"
    height = uv.shape[1]
    width = uv.shape[2]

    xx, yy = tf.meshgrid(tf.range(width), tf.range(height))
    xx = tf.expand_dims(tf.expand_dims(xx, 0), 3)
    yy = tf.expand_dims(tf.expand_dims(yy, 0), 3)
    n = tf.shape(uv)[0]
    xx = tf.tile(xx, [n, 1, 1, 1])
    yy = tf.tile(yy, [n, 1, 1, 1])
    xx = tf.cast(xx, tf.float32)
    yy = tf.cast(yy, tf.float32)
    grid = tf.concat([xx, yy], axis=3)
    return grid + uv


def _clip_values(x, y):
    """ Clips points to be within image boundaries.
        USERS SHOULD NOT BE CALLING THIS FUNCTION. """
    assert x.shape[1] == y.shape[1]
    assert x.shape[2] == y.shape[2]
    assert x.dtype == y.dtype
    dtype = x.dtype
    max_y = tf.cast(x.shape[1] - 1, dtype)
    max_x = tf.cast(x.shape[2] - 1, dtype)
    zero = tf.zeros([], dtype=dtype)
    return tf.clip_by_value(x, zero, max_x), tf.clip_by_value(y, zero, max_y)


def _get_pixel_values(images, xx, yy):
    """ Returns a 4D tensor with points sampled at the given locations.
        USERS SHOULD BE CALLING THIS FUNCTION DIRECTLY. """
    assert xx.shape[1] == yy.shape[1]
    assert xx.shape[2] == yy.shape[2]
    # Points outside of image boundaries are truncated to the boundary pixels.
    n = tf.shape(xx)[0]
    xx_clipped, yy_clipped = _clip_values(xx, yy)
    batch_idx = tf.range(0, n)
    batch_idx = tf.reshape(batch_idx, [n, 1, 1])
    b = tf.tile(batch_idx, [1, xx.shape[1], xx.shape[2]])
    indices = tf.stack(
        [b, tf.cast(yy_clipped, tf.int32),
         tf.cast(xx_clipped, tf.int32)],
        axis=3)
    return tf.gather_nd(images, indices)


def _get_lower_upper_neighbors(x):
    x0 = tf.cast(x, tf.int32)
    x1 = x0 + 1
    return x0, x1


def _get_query_points(x, y):
    x0, x1 = _get_lower_upper_neighbors(x)
    y0, y1 = _get_lower_upper_neighbors(y)
    return x0, y0, x1, y1
