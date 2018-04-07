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

        return zip(
            *[[self._I1s[i], self._I2s[i], self._flos[i], self._weights[i]]
              for i in idx])

    def _load_all(self):
        self._I1s = []
        self._I2s = []
        self._flos = []
        self._weights = []

        target_size = (self._image_size, self._image_size)
        for f in self._files:
            print "Loading ", f
            I1, I2, flo = self._load_triple(f, normalize=False)
            if len(I1.shape) == 0 or len(I2.shape) == 0:
                print "Encountered invalid triple, skipping: ", f
                continue

            if self._image_size is not I1.shape[0]:
                I1 = cv2.resize(I1, target_size)
                I2 = cv2.resize(I2, target_size)
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

            self._I1s.append(I1)
            self._I2s.append(I2)
            self._flos.append(flo)
            self._weights.append(weights)

    def _load_triple(self, fn_triplet, normalize):
        flo = np.asarray(utils.read_flo(fn_triplet[0]), dtype='float32')
        I1 = np.asarray(cv2.imread(fn_triplet[1]), dtype='float32')
        I2 = np.asarray(cv2.imread(fn_triplet[2]), dtype='float32')
        if normalize:
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
            try:
                Dataset._check_files_exist(flo_fn, i1_fn, i2_fn)
            except:
                pass
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
        utils.resample_flow(triplet[0], sz),
        cv2.resize(triplet[1], sz),
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

    flow = triplet[0][y_offset:y_offset + target_size[0], x_offset:
                      x_offset + target_size[1], :]
    img1 = triplet[1][y_offset:y_offset + target_size[0], x_offset:
                      x_offset + target_size[1], :]
    img2 = triplet[2][y_offset:y_offset + target_size[0], x_offset:
                      x_offset + target_size[1], :]
    return [flow, img1, img2]


def generate_example_triplet_flip(triplet, flip_x=False, flip_y=False):
    """ Flips and returns a given triplet. """
    output = [np.copy(triplet[0]), np.copy(triplet[1]), np.copy(triplet[2])]
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
