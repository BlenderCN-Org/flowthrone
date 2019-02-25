"""
Functions for data augmentation (geometric transformations + brightness/
contrast changes).
"""
import tensorflow as tf
import glog as log


def maybe_flip_tf_example_left_right(x1, x2, y, seed=0):
    """ Maybe flips and returns a given triplet, or maybe doesn't flip. """
    return _maybe_flip_tf_example(x1, x2, y, flip_tf_example_left_right, seed)


def maybe_flip_tf_example_up_down(x1, x2, y, seed=0):
    """ Maybe flips and returns a given triplet, or maybe doesn't flip. """
    return _maybe_flip_tf_example(x1, x2, y, flip_tf_example_up_down, seed)


def flip_tf_example_left_right(x1, x2, y):
    """ Flips image horizontally and negatives horizontal flow. """
    x1 = tf.image.flip_left_right(x1)
    x2 = tf.image.flip_left_right(x2)
    y = tf.image.flip_left_right(y)
    # Negate flow along x. Is there really not a better way?
    wx, wy = tf.split(y, 2, axis=-1)
    wx = tf.multiply(wx, -1)
    y = tf.concat([wx, wy], axis=-1)
    return x1, x2, y


def flip_tf_example_up_down(x1, x2, y):
    """ Flips image vertically and negatives vertical flow. """
    x1 = tf.image.flip_up_down(x1)
    x2 = tf.image.flip_up_down(x2)
    y = tf.image.flip_up_down(y)
    # Negate flow along x. Is there really not a better way?
    wx, wy = tf.split(y, 2, axis=-1)
    wy = tf.multiply(wy, -1)
    y = tf.concat([wx, wy], axis=-1)
    return x1, x2, y


def adjust_tf_example_brightness_contrast(x1,
                                          x2,
                                          y,
                                          contrast=[0.75, 1.25],
                                          brightness=[-0.125, 0.125],
                                          seed=0):
    """ Adjusts brightness/contrast of both images by a uniformly chosen
        amount, and leaves flow field untouched. """
    c = tf.random_uniform([], contrast[0], contrast[1], seed=seed)
    b = tf.random_uniform([], brightness[0], brightness[1], seed=seed)
    x1 = tf.image.adjust_brightness(
        tf.image.adjust_contrast(x1, contrast_factor=c), delta=b)
    x2 = tf.image.adjust_brightness(
        tf.image.adjust_contrast(x2, contrast_factor=c), delta=b)
    return x1, x2, y


def transpose_tf_example(x1, x2, y):
    """ Transposes x and y dimensions of the example, i.e.
        image1_out(x, y) = image1_in(y, x)
        image2_out(x, y) = image2_in(y, x)
        [flow_x(x, y), flow_y(x, y)] = [flow_y(y, x), flow_x(y, x)]
    """
    x1_t = tf.image.transpose_image(x1)
    x2_t = tf.image.transpose_image(x2)
    y_t = tf.image.transpose_image(y)
    wx, wy = tf.split(y_t, 2, axis=-1)
    y_t = tf.concat([wy, wx], axis=-1)
    return x1_t, x2_t, y_t


def maybe_transpose_tf_example(x1, x2, y, seed=0):
    """ Maybe transposes a given triplet, or maybe doesn't """
    assert y.shape[-1] == 2
    should_transpose = tf.less(tf.random_uniform([], 0, 1.0, seed=seed), 0.5)
    return tf.cond(
        should_transpose,
        true_fn=lambda: transpose_tf_example(x1, x2, y),
        false_fn=lambda: _identity(x1, x2, y))


def _identity(x1, x2, y):
    return x1, x2, y


def _maybe_flip_tf_example(x1, x2, y, func, seed=0):
    """ Maybe flips and returns a given triplet, or maybe doesn't flip. """
    assert y.shape[-1] == 2
    flip_x = tf.less(tf.random_uniform([], 0, 1.0, seed=seed), 0.5)
    return tf.cond(
        flip_x,
        true_fn=lambda: func(x1, x2, y),
        false_fn=lambda: _identity(x1, x2, y))
