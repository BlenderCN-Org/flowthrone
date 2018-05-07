import os
import sys
import argparse
# Add parent directory to pythonpath.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import dataset_utils
import numpy as np
import tensorflow as tf


def get_input_files(args):
    flying_chairs_path = os.path.join(args.dataset_path, 'data')
    matchers = ['flow.flo', 'img1.ppm', 'img2.ppm']
    dataset = dataset_utils.Dataset(
        flying_chairs_path, num_splits=10, matchers=matchers)
    if args.kind == 'train':
        return dataset.train_files()
    elif args.kind == 'val':
        return dataset.val_files()
    elif args.kind == 'all':
        return dataset.all_files()
    else:
        raise Exception('did not understand the argument')


def main(args):
    files = get_input_files(args)
    target_size = [args.target_size, args.target_size]

    record_writer = tf.python_io.TFRecordWriter(args.output_filename)
    remaining_files = set(range(len(files)))
    for idx in range(args.num_examples):
        if len(remaining_files) == 0:
            print "Exhausted all files; will reset sampling from beginning."
            remaining_files = set(range(len(files)))
        fn_idx = random.choice(list(remaining_files))
        remaining_files -= {fn_idx}
        print "Writing example {} to {}".format(idx, args.output_filename)

        triplet = dataset_utils.read_triplet(\
                files[fn_idx][0], files[fn_idx][1], files[fn_idx][2])
        flow, img1, img2 = dataset_utils.generate_example(triplet, target_size)

        img1 = img1.astype(dtype=np.uint8)
        img2 = img2.astype(dtype=np.uint8)
        flow = flow.astype(dtype=np.float32)
        example = dataset_utils.as_tf_example(img1, img2, flow)
        record_writer.write(example)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dataset_path',
        default=os.path.join(os.getenv('HOME'), 'data/FlyingChairs_release'),
        help='Path to FlyingChairs dataset.')
    parser.add_argument(
        '--output_filename',
        default='',
        help='Filename where the generated tfrecords file should be saved to.')
    parser.add_argument(
        '--num_examples',
        type=int,
        default=100,
        help='Number of examples to generate.')
    parser.add_argument(
        '--target_size',
        type=int,
        default=128,
        help='Size of the output examples')
    parser.add_argument(
        '--kind',
        action='store',
        default='all',
        choices=['val', 'train', 'all'],
        help='Whether to generate training or validation dataset')
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
