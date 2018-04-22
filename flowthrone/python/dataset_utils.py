from __future__ import division
import cv2
import os
import utils
import random
import numpy as np


class DataFeeder:
    """
    Helper class for loading flow triplets (image pair, flow), and providing
    them as 'batches'.
    USAGE:
        >>> feeder = DataFeeder(triplet_files, image_size=64, batch_size=16)

    The argument `triplet_files` is a list of length-3 lists, where each 3-list
    contains a path to an image pair, and a path to the .flo groundtruth.
    [ ['/path/to/00000_flow1.flo',
       '/path/to/00000_img1.jpg',
       '/path/to/00000_img2.jpg'],
      ['/path/to/00001_flow1.flo',
       '/path/to/00001_img1.jpg',
       '/path/to/00001_img2.jpg'],
      ...
    ]
    Next batch can be obtained like so:
        >>> images1, images2, flows, weights = feeder.next_batch()

    Weights are binary masks -- '0' wherever flow field had NaNs
    (i.e. at occluded regions), and '1' otherwise. If your flow groundtruth does
    not have annotations for occluded regions, you may omit weights entirely.
    """
    _image_size = None
    _files = []
    _cur_idx = 0
    _batch_size = 1

    _I1s = []
    _I2s = []
    _flos = []
    _weights = []

    def __init__(self,
                 files,
                 image_size=64,
                 batch_size=1,
                 max_examples_to_use=None):
        """Args:
            files: List of 3-tuples, each containing paths to flow groundtruth
                   and a corresponding image pair.
            image_size: Target size of the returned square image patches.
            batch_size: Number of tuples to return on each call of `next_batch`.
        """
        self._files = files
        if max_examples_to_use is not None:
            print ("Asked to use {} out of {} examples. Will shuffle and "
                   "clip the dataset.".format(\
                    max_examples_to_use, len(self._files)))
            random.shuffle(self._files)
            self._files = self._files[0:max_examples_to_use]

        self._batch_size = batch_size
        self._image_size = image_size
        self._load_all()
        # After the files are loaded, shuffle them once.
        self._maybe_shuffle_dataset(p=1.0)

    def _maybe_shuffle_dataset(self, p):
        """Rolls a die and shuffles the loaded dataset."""
        if np.random.uniform(0, 1) <= p:
            print "Shuffling the dataset."
            self.shuffle()

    def shuffle(self):
        """Shuffles the dataset.
        This ensures that the same entries do not appear in the same batch
        over and over, on multiple iterations through the dataset.
        """
        idx = range(len(self._files))
        np.random.shuffle(idx)
        assert len(self._files) == len(self._I1s)
        assert len(self._I1s) == len(self._I2s)
        assert len(self._I2s) == len(self._flos)
        assert len(self._flos) == len(self._weights)

        self._files = [self._files[i] for i in idx]
        self._I1s = [self._I1s[i] for i in idx]
        self._I2s = [self._I2s[i] for i in idx]
        self._flos = [self._flos[i] for i in idx]
        self._weights = [self._weights[i] for i in idx]

    def next_batch(self):
        """Returns a collection of images at t, images at t+1, flow fields,
           and weights. Weights are binary masks that are 'zero' at occluded
           regions, and are 'one' otherwise.
        """
        # 1/ number of iterations to go over dataset.
        shuffle_prob = float(self._batch_size) / len(self._files)
        self._maybe_shuffle_dataset(shuffle_prob)

        n = len(self._I1s)
        idx = range(self._cur_idx, self._cur_idx + self._batch_size)
        idx = np.mod(idx, n)
        self._cur_idx = (idx[-1] + 1) % n

        return zip(* [[
            self._I1s[i], self._I2s[i], self._flos[i], self._weights[i]
        ] for i in idx])

        ##pts = []
        ##for i in idx:
        ##    I1 = self._I1s[i]
        ##    I2 = self._I2s[i]
        ##    uv = self._flos[i]
        ##    triplet = [uv, I1, I2]
        ##    triplet = generate_example_triplet_flip(triplet, \
        ##            flip_x=random.randint(0, 1), flip_y=random.randint(0, 1))
        ##    pts.append([triplet[1], triplet[2], triplet[0], self._weights[i]])
        ##return zip(*pts)

    def _load_all(self):
        self._I1s = []
        self._I2s = []
        self._flos = []
        self._weights = []

        target_size = (self._image_size, self._image_size)
        files = []
        for idx, f in enumerate(self._files):
            print "Loading {}/{}: {}".format(idx, len(self._files), f)
            I1, I2, flo = self._load_triple(f, normalize=False)
            if I1 is None or I2 is None or len(I1.shape) == 0 or len(
                    I2.shape) == 0:
                print "Encountered invalid triple, skipping: ", f
                continue
                # TODO: this create inconsistency between self.files length and
                # I1/I2 length.
            if self._image_size is not I1.shape[0]:
                I1 = cv2.resize(I1, target_size)
                I2 = cv2.resize(I2, target_size)
                # BAD!!! DO NOT DO THIS!!!
                orig_width = flo.shape[1]
                orig_height = flo.shape[0]
                flo[:, :, 0] *= target_size[0] / orig_height
                flo[:, :, 1] *= target_size[1] / orig_width
                flo = cv2.resize(flo, target_size)

            # Set weights to be 1 - occlusion mask.
            weights = np.ones([I1.shape[0], I1.shape[1], 2])
            weights[np.isnan(flo)] = 0.0
            # Zero out invalid pixels.
            flo[np.isnan(flo)] = 0.0

            flip_x = random.randint(0, 1)
            flip_y = random.randint(0, 1)
            print "Flipping: {} {}".format(flip_x, flip_y)
            flo, I1, I2 = generate_example_triplet_flip([flo, I1, I2], flip_x,
                                                        flip_y)

            self._I1s.append(I1)
            self._I2s.append(I2)
            self._flos.append(flo)
            self._weights.append(weights)
            files.append(f)
        self._files = files

    def _load_triple(self, fn_triplet, normalize):
        flo = np.asarray(utils.read_flo(fn_triplet[0]), dtype='float32')
        #I1 = np.asarray(cv2.imread(fn_triplet[1]), dtype='float32')
        #I2 = np.asarray(cv2.imread(fn_triplet[2]), dtype='float32')
        I1 = cv2.imread(fn_triplet[1])
        I2 = cv2.imread(fn_triplet[2])
        if normalize:
            assert False
            I1 = (I1 - 128.0) / 128.0
            I2 = (I2 - 128.0) / 128.0
        return (I1, I2, flo)


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
            #try:
            Dataset._check_files_exist(flo_fn, i1_fn, i2_fn)
            #except:
            #    continue

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


def read_triplet(flo_fn, img1_fn, img2_fn):
    """ Reads and returns a triplet. """
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
    import tensorflow as tf
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _float_feature(value):
    import tensorflow as tf
    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))


def as_tf_train_example(x1, x2, flow):
    """ Returns triplet as tf.train.Example instance. """
    import tensorflow as tf
    assert x1.dtype == np.uint8
    assert x2.dtype == np.uint8
    assert flow.dtype == np.float32

    features = tf.train.Features(feature={
        'x1': _bytes_feature(x1.tostring()),
        'x2': _bytes_feature(x2.tostring()),
        'y': _bytes_feature(flow.tostring()),
    })
    return tf.train.Example(features=features)


def decode_tf_example(serialized_example, imsize):
    """ Parses image pair and groundtruth flow from the given
        `serialized_example`. Returns x1, x2, y (pair of images, followed by
        optical flow. """
    import tensorflow as tf
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


def write_tf_records_dataset(input_files_list, output_filename):
    """ Given a list of [flow, img1, img2] filename tuples, writes a
        TFRecordWriter file """
    import tensorflow as tf

    for flow_fn, img1_fn, img2_fn in input_files_list:
        print "Wrote triplet from file: ", os.path.basename(flow_fn)
        flow, img1, img2 = read_triplet(flow_fn, img1_fn, img2_fn)
        img1 = img1.astype(dtype=np.uint8)
        img2 = img2.astype(dtype=np.uint8)
        flow = flow.astype(dtype=np.float32)
        example = as_tf_train_example(img1, img2, flow)
        record_writer.write(example.SerializeToString())
    record_writer.close()
