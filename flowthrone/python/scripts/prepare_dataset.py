import os
import sys
import argparse
# Add parent directory to pythonpath.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from training import dataset_utils
import numpy as np
import tensorflow as tf
import random
import glog as log

def get_input_files(args):
    dataset = dataset_utils.create_dataset(args.dataset_type,
                                           args.dataset_path)
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
    print "Found {} files.".format(len(files))
    target_size = [args.target_size, args.target_size]

    record_writer = tf.python_io.TFRecordWriter(args.output_filename)
    remaining_files = set(range(len(files)))
    verbose = False
    for idx in range(args.num_examples):
        if len(remaining_files) == 0:
            print "Exhausted all files; will reset sampling from beginning."
            remaining_files = set(range(len(files)))
        fn_idx = random.choice(list(remaining_files))
        remaining_files -= {fn_idx}
        if idx % 100 == 0:
            print "Writing example {} to {}".format(idx, args.output_filename)

        triplet = dataset_utils.read_triplet(\
                files[fn_idx][0], files[fn_idx][1], files[fn_idx][2])
        flow, img1, img2 = dataset_utils.generate_example(
            triplet, target_size, scale_range=[0.1, .25])

        img1 = img1.astype(dtype=np.uint8)
        img2 = img2.astype(dtype=np.uint8)
        flow = flow.astype(dtype=np.float32)

        for item in [img1, img2, flow]:
            log.check_eq(args.target_size, item.shape[0])
            log.check_eq(args.target_size, item.shape[1])
       
        if verbose:
            print "Flow range x: {:.2f}, {:.2f}, y: {:.2f}, {:.2f}".format(
                    np.min(flow[:,:,0]), np.max(flow[:,:,0]),
                    np.min(flow[:,:,1]), np.max(flow[:,:,1]))

        example = dataset_utils.as_tf_example(img1, img2, flow)
        record_writer.write(example)
    print "Wrote {} examples to {}".format(args.num_examples,
                                           args.output_filename)


def parse_args():
    parser = argparse.ArgumentParser(description='''
    Script for loading standard datasets and creating files with TFRecords
    for training.
    ''')
    parser.add_argument(
        '--dataset_type',
        choices=dataset_utils.valid_datasets(),
        required=True,
        help='Dataset type.')
    parser.add_argument(
        '--dataset_path',
        default=os.path.join(os.getenv('HOME'), 'data/FlyingChairs_release'),
        help='Path to the dataset.')
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
