from __future__ import division
import cv2
import os
import utils
import random
import numpy as np
import tensorflow as tf
import glog as log
import re

def valid_datasets():
    return [
        x.__name__ for x in [SintelDataset, SDHomDataset, FlyingChairsDataset]
    ]


def create_dataset(kind, path):
    log.check(kind in valid_datasets())
    if kind == FlyingChairsDataset.__name__:
        return FlyingChairsDataset(path)
    if kind == SDHomDataset.__name__:
        return SDHomDataset(path)
    if kind == SintelDataset.__name__:
        return SintelDataset(path)
    log.fatal('You did not specify a valid dataset type {}'.format(kind))


class SintelDataset:
    """ Helper class for loading Sintel dataset. """

    def all_files(self):
        return self._all_file_list

    def train_files(self):
        return self._train_file_list

    def val_files(self):
        return self._val_file_list

    def __init__(self, dataset_path, num_splits=10):
        # Sintel is split into sequences, and the 'test' set can't be used
        # for validation, since the groundtruth flow is not provided.
        flow_path = os.path.join(dataset_path, 'training', 'flow')
        seqs = sorted([
            s for s in os.listdir(flow_path) if os.path.isdir(os.path.join(flow_path, s))])
        log.check_gt(
            len(seqs), 0, 'Did not find any sequences -- is the path correct?')
        train_seqs, val_seqs = self._split_sequences(seqs, num_splits)

        self._train_file_list = []
        self._val_file_list = []
        self._all_file_list = []

        for seq in train_seqs:
            self._train_file_list += self._process_sequence(dataset_path, seq)
        for seq in val_seqs:
            self._val_file_list += self._process_sequence(dataset_path, seq)
        self._all_file_list = self._train_file_list + self._val_file_list

    def _split_sequences(self, sequences, num_splits):
        train_seqs = []
        val_seqs = []
        for i, seq in enumerate(sequences):
            if i % num_splits == 0:
                val_seqs.append(seq)
            else:
                train_seqs.append(seq)
        return train_seqs, val_seqs

    def _process_sequence(self, dataset_path, seq):
        flow_path = os.path.join(dataset_path, 'training', 'flow', seq)
        img_path = os.path.join(dataset_path, 'training', 'final', seq)
        flo_files = sorted([f for f in os.listdir(flow_path) if f.endswith('flo')])
        output = []
        for f in flo_files:
            idx = int(re.findall('frame_([0-9]+).flo', f)[0])
            img1_base_filename = 'frame_{:04d}.png'.format(idx)
            img2_base_filename = 'frame_{:04d}.png'.format(idx + 1)
            flo_filename = os.path.join(flow_path, f)
            img1_filename = os.path.join(img_path, img1_base_filename)
            img2_filename = os.path.join(img_path, img2_base_filename)

            Dataset._check_files_exist(flo_filename, img1_filename,
                                       img2_filename)
            output.append([flo_filename, img1_filename, img2_filename])
        return output


class FlyingChairsDataset:
    """ Helper class for loading FlyingChairs dataset. """

    def train_files(self):
        return self._dataset.train_files()

    def val_files(self):
        return self._dataset.val_files()

    def all_files(self):
        return self._dataset.all_files()

    def __init__(self, dataset_path, num_splits=10):
        self._dataset = Dataset(
            dataset_path,
            num_splits=num_splits,
            matchers=flying_chairs_matchers())


class SDHomDataset:
    """ Helper class for loading SDHom dataset
        (https://lmb.informatik.uni-freiburg.de/resources/datasets/FlyingChairs.en.html#chairssdhom)

        USAGE:
         >>> dataset = SDHomDataset('/path/to/my/flow/dataset/')
         >>> train_files = dataset.train_files()
         >>> val_files = dataset.val_files()
         >>> all_files = dataset.all_files()

    """
    _train_file_list = []
    _val_file_list = []
    _all_file_list = []

    _FLOW_MATCHER = None
    _IMG1_FN = None
    _IMG2_FN = None

    def train_files(self):
        return self._train_file_list

    def val_files(self):
        return self._val_file_list

    def all_files(self):
        return self._all_file_list

    def __init__(self, dataset_path):
        dataset_path = os.path.join(dataset_path, 'data')
        self._train_file_list = self._get_files(dataset_path, 'train')
        self._val_file_list = self._get_files(dataset_path, 'test')
        self._all_file_list = self._train_file_list + self._val_file_list

    def _get_files(self, dataset_path, kind):
        self._FLOW_MATCHER = '.pfm'
        self._IMG1_FN = '.png'
        self._IMG2_FN = '.png'

        flo_files = sorted([f for f in \
                os.listdir(os.path.join(dataset_path, kind, 'flow')) \
                            if f.endswith(self._FLOW_MATCHER)])
        files = []
        for i, f in enumerate(flo_files):
            flo_fn = os.path.join(dataset_path, kind, 'flow', f)
            i1_fn = os.path.join(dataset_path, kind, 't0',
                                 f.replace(self._FLOW_MATCHER, self._IMG1_FN))
            i2_fn = os.path.join(dataset_path, kind, 't1',
                                 f.replace(self._FLOW_MATCHER, self._IMG2_FN))
            files.append([flo_fn, i1_fn, i2_fn])
        return files


class Dataset:
    """ Helper class for loading optical flow datasets.
        Assumes that a 'dataset' is stored as a collection of image-pair/flow
        triplets in a single directory, as:
          $ ls -l /path/to/dataset/directory/
          $ 00000_img1.jpg
            00000_img2.jpg
            00000_flow1.flo
            00001_img1.jpg
            00001_img2.jpg
            00000_flow1.flo
            ...
        With these exact names and extensions.
        Effectively, the class will read the files in the directory, will
        organize them into (image1, image2, flow) triplets, and will also
        partition them into training/validation subsets.

        USAGE:
         >>> dataset = Dataset('/path/to/my/flow/dataset/', num_splits=10)
         >>> train_files = dataset.train_files()
         >>> val_files = dataset.val_files()
    """
    _train_file_list = []
    _val_file_list = []
    _all_file_list = []

    _FLOW_MATCHER = None
    _IMG1_FN = None
    _IMG2_FN = None

    def train_files(self):
        return self._train_file_list

    def val_files(self):
        return self._val_file_list

    def all_files(self):
        return self._all_file_list

    def __init__(self, dataset_path, num_splits=10, \
                       matchers=['flow1.flo', 'img1.jpg', 'img2.jpg']):
        self._FLOW_MATCHER = matchers[0]
        self._IMG1_FN = matchers[1]
        self._IMG2_FN = matchers[2]
        flo_files = sorted([f for f in os.listdir(dataset_path) \
                            if f.endswith(self._FLOW_MATCHER)])
        for i, f in enumerate(flo_files):
            flo_fn = os.path.join(dataset_path, f)
            i1_fn = os.path.join(dataset_path,
                                 f.replace(self._FLOW_MATCHER, self._IMG1_FN))
            i2_fn = os.path.join(dataset_path,
                                 f.replace(self._FLOW_MATCHER, self._IMG2_FN))
            try:
                Dataset._check_files_exist(flo_fn, i1_fn, i2_fn)
            except:
                continue

            if i % num_splits == 0:
                self._val_file_list.append([flo_fn, i1_fn, i2_fn])
            else:
                self._train_file_list.append([flo_fn, i1_fn, i2_fn])
            self._all_file_list.append([flo_fn, i1_fn, i2_fn])

    @staticmethod
    def _check_files_exist(flo_fn, i1_fn, i2_fn):
        if not (os.path.exists(flo_fn) and \
                os.path.exists(i1_fn) and \
                os.path.exists(i2_fn)):
            raise Exception(('Could not find {}, {}, {} tuple. Maybe the '
                             'dataset is not organized in the expected way? '
                             'The assumption is that each example is saved as '
                             'three files with identical prefix.').format(
                                 flo_fn, i1_fn, i2_fn))


def flying_chairs_matchers():
    return ['flow.flo', 'img1.ppm', 'img2.ppm']


def read_triplet(flo_fn, img1_fn, img2_fn):
    """ Reads and returns a triplet. """
    if flo_fn.endswith('pfm'):
        flow = utils.read_pfm(flo_fn)
    else:
        flow = utils.read_flo(flo_fn)
    img1 = cv2.imread(img1_fn)
    img2 = cv2.imread(img2_fn)
    return [flow, img1, img2]


def write_triplet(triplet, output_path, idx):
    """ Writes a (flow, image1, image2) tuple to the provided output path. """
    flo_fn = os.path.join(output_path, '{:06d}_flow1.flo'.format(idx))
    img1_fn = os.path.join(output_path, '{:06d}_img1.jpg'.format(idx))
    img2_fn = os.path.join(output_path, '{:06d}_img2.jpg'.format(idx))
    utils.write_flo(flo_fn, triplet[0])
    cv2.imwrite(img1_fn, triplet[1])
    cv2.imwrite(img2_fn, triplet[2])


def resize_triplet(triplet, scale):
    """ Isotropically resizes and returns the provided (flow, image1, image2)
    tuple. """
    sz = (int(triplet[0].shape[0] * scale), int(triplet[0].shape[1] * scale))
    return [
        utils.resample_flow(triplet[0], sz), cv2.resize(triplet[1], sz),
        cv2.resize(triplet[2], sz)
    ]


def generate_example(triplet, target_size, scale_range=[0.25, 0.75]):
    """ Given a (flow, image1, image2) tuple, creates and returns a random
    modified tuple. The allowed modifications are limited to scaling and
    cropping. """
    # Randomly rescale the original example.
    triplet = generate_example_triplet_scale(triplet, target_size, scale_range)
    # Randomly choose location where the crop should be taken
    triplet = generate_example_triplet_shift_and_crop(triplet, target_size)
    # Ideally here we could also perform 90-degree rotations/flips
    return triplet


def generate_example_triplet_scale(triplet,
                                   target_size,
                                   scale_range=[0.25, 0.75]):
    """ Resizes a triplet to a randomly chosen scale. """
    min_scale = max(target_size[0] / float(triplet[0].shape[0]),
                    target_size[1] / float(triplet[0].shape[1]))
    # Reset the lower bound if necessary. Otherwise, we run the risk of
    # choosing a too-small scale, and not being able to pick a
    # (target_size, target_size) sized crop later.
    if min_scale > scale_range[0]:
        scale_range[0] = min_scale
    if scale_range[0] > scale_range[1]:
        scale_range[1] = scale_range[0]
    scale = np.random.uniform(low=scale_range[0], high=scale_range[1])
    return resize_triplet(triplet, scale)


def generate_example_triplet_shift_and_crop(triplet, target_size):
    """ Given a (large) tiple and a (smaller) target size, take a randomly
    selected crop and return it as a triplet """
    rows = triplet[0].shape[0]
    cols = triplet[0].shape[1]
    assert target_size[0] <= rows and target_size[1] <= cols

    # Choose a random offset and crop.
    y_offset = 0
    x_offset = 0
    if rows > target_size[0]:
        y_offset = np.random.randint(0, rows - target_size[0])
    if cols > target_size[1]:
        x_offset = np.random.randint(0, cols - target_size[1])

    flow = triplet[0][y_offset:y_offset + target_size[0], x_offset:x_offset +
                      target_size[1], :]
    img1 = triplet[1][y_offset:y_offset + target_size[0], x_offset:x_offset +
                      target_size[1], :]
    img2 = triplet[2][y_offset:y_offset + target_size[0], x_offset:x_offset +
                      target_size[1], :]
    return [flow, img1, img2]


def generate_example_triplet_flip(triplet, flip_x=False, flip_y=False):
    """ Flips and returns a given triplet. """
    output = triplet
    if flip_y:
        output[1] = cv2.flip(output[1], 0)
        output[2] = cv2.flip(output[2], 0)
        output[0] = cv2.flip(output[0], 0)
        # negate flow along y.
        triplet[0][:, :, 1] *= -1
    if flip_x:
        output[1] = cv2.flip(output[1], 1)
        output[2] = cv2.flip(output[2], 1)
        output[0] = cv2.flip(output[0], 1)
        # negate flow along x.
        output[0][:, :, 0] *= -1
    return output


def generate_example_triplet_brightness(triplet, alpha=1.0, beta=0.0):
    """ Applies an affine transformation to image values and returns the
        triplet.
    """
    output = triplet
    output[1] = output[1] * alpha + beta
    output[2] = output[2] * alpha + beta
    return output


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _float_feature(value):
    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))


def as_tf_example(x1, x2, flow):
    """ Returns triplet as a binary serialization of tf.train.Example. """
    assert x1.dtype == np.uint8
    assert x2.dtype == np.uint8
    assert flow.dtype == np.float32

    features = tf.train.Features(feature={
        'x1': _bytes_feature(x1.tostring()),
        'x2': _bytes_feature(x2.tostring()),
        'y': _bytes_feature(flow.tostring()),
    })
    return tf.train.Example(features=features).SerializeToString()


def decode_tf_example(serialized_example, imsize):
    """ Parses image pair and groundtruth flow from the given
        `serialized_example`. Returns x1, x2, y (pair of images, followed by
        optical flow. """

    features = tf.parse_single_example(
        serialized_example,
        features={
            'x1': tf.FixedLenFeature([], tf.string),
            'x2': tf.FixedLenFeature([], tf.string),
            'y': tf.FixedLenFeature([], tf.string),
        })

    x1 = tf.reshape(
        tf.decode_raw(
            features['x1'], out_type=tf.uint8, name='x1'),
        shape=[imsize, imsize, 3])
    x2 = tf.reshape(
        tf.decode_raw(
            features['x2'], out_type=tf.uint8, name='x2'),
        shape=[imsize, imsize, 3])
    y = tf.reshape(
        tf.decode_raw(
            features['y'], out_type=tf.float32, name='y'),
        shape=[imsize, imsize, 2])
    return x1, x2, y


def _flip_tf_example_left_right(x1, x2, y):
    x1 = tf.image.flip_left_right(x1)
    x2 = tf.image.flip_left_right(x2)
    y = tf.image.flip_left_right(y)
    # Negate flow along x. Is there really not a better way?
    wx, wy = tf.split(y, 2, axis=-1)
    wx = tf.multiply(wx, -1)
    y = tf.concat([wx, wy], axis=-1)
    return x1, x2, y


def _flip_tf_example_up_down(x1, x2, y):
    x1 = tf.image.flip_up_down(x1)
    x2 = tf.image.flip_up_down(x2)
    y = tf.image.flip_up_down(y)
    # Negate flow along x. Is there really not a better way?
    wx, wy = tf.split(y, 2, axis=-1)
    wy = tf.multiply(wy, -1)
    y = tf.concat([wx, wy], axis=-1)
    return x1, x2, y


def _identity(x1, x2, y):
    return x1, x2, y


def maybe_flip_tf_example(x1, x2, y, func, seed=0):
    """ Maybe flips and returns a given triplet, or maybe doesn't flip. """
    assert y.shape[-1] == 2
    flip_x = tf.less(tf.random_uniform([], 0, 1.0, seed=seed), 0.5)
    return tf.cond(
        flip_x,
        true_fn=lambda: func(x1, x2, y),
        false_fn=lambda: _identity(x1, x2, y))


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
        tf.image.adjust_contrast(
            x1, contrast_factor=c), delta=b)
    x2 = tf.image.adjust_brightness(
        tf.image.adjust_contrast(
            x2, contrast_factor=c), delta=b)
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


def maybe_flip_tf_example_left_right(x1, x2, y, seed=0):
    """ Maybe flips and returns a given triplet, or maybe doesn't flip. """
    return maybe_flip_tf_example(x1, x2, y, _flip_tf_example_left_right, seed)


def maybe_flip_tf_example_up_down(x1, x2, y, seed=0):
    """ Maybe flips and returns a given triplet, or maybe doesn't flip. """
    return maybe_flip_tf_example(x1, x2, y, _flip_tf_example_up_down, seed)


def write_tf_records_dataset(input_files_list, output_filename):
    """ Given a list of [flow, img1, img2] filename tuples, writes a
        TFRecordWriter file """

    for flow_fn, img1_fn, img2_fn in input_files_list:
        print "Wrote triplet from file: ", os.path.basename(flow_fn)
        flow, img1, img2 = read_triplet(flow_fn, img1_fn, img2_fn)
        img1 = img1.astype(dtype=np.uint8)
        img2 = img2.astype(dtype=np.uint8)
        flow = flow.astype(dtype=np.float32)
        example = as_tf_train_example(img1, img2, flow)
        record_writer.write(example.SerializeToString())
    record_writer.close()
