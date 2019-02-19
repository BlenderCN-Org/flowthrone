"""
Example of using optical flow in python.
This is just a demo used to illustrate how the model can be loaded / run.
"""
import argparse
import cv2
import glog as log
import numpy as np
import os
import tensorflow as tf
import time
import utils
from optical_flow_model import OpticalFlowModel
from utils import compute_flow_color
import model_config


def guess_network_size(width, height):
    import math
    ratio = width / float(height)
    # This is a hack: we basically need to make sure that input dimensions are
    # evenly divisible by n-th power of two (here n=6).
    pow_2_6 = pow(2, 6)
    size = [int(math.ceil(ratio * 256 / pow_2_6)) * pow_2_6, 256]
    print "Guessed an okay input size to be: {}".format(size)
    return size


def main():
    args = parse_args()
    # Load a pair of images.
    image1 = cv2.imread(args.image1)
    image2 = cv2.imread(args.image2)

    # Normally one can/should create a network without trying to infer the size
    # using image dimensions.
    if args.size is None:
        args.size = guess_network_size(
            width=image1.shape[1], height=image1.shape[0])

    session_config = tf.ConfigProto()
    session_config.gpu_options.allow_growth = True
    sess = tf.Session(config=session_config)

    model_handle = model_config.MODELS[args.model]
    # Downloads the model if necessary.
    model_handle.load_if_needed()
    print "Loading a model from {}".format(model_handle.path)
    # Expensive: usually should do only once for the entire video sequence, or
    # for a collection of images.
    flow_solver = OpticalFlowModel(
        session=sess,
        size=args.size,
        model_path=model_handle.path)

    # Compute flow.
    t1 = time.time()
    flow = flow_solver.run(image1, image2)
    t2 = time.time()
    print "Elapsed {} secs".format(t2-t1)
    
    uv = compute_flow_color(u=flow[:, :, 0], v=flow[:, :, 1])
    if args.visualize:
        cv2.imshow("images", np.concatenate([image1, image2], axis=1))
        cv2.imshow("image", uv)
        cv2.waitKey(0)
    if args.output_filename is not None:
        cv2.imwrite(args.output_filename, uv)
        print "Wrote output to {}".format(args.output_filename)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model',
        choices=model_config.MODELS.keys(),
        default=sorted(model_config.MODELS.keys())[::-1][0])
    parser.add_argument(
        '--size', action='append', nargs=2, help='network size')
    parser.add_argument(
        '--image1',
        default=None,
        help='path to the first image',
        required=True)
    parser.add_argument(
        '--image2',
        default=None,
        help='path to the second image',
        required=True)
    parser.add_argument(
        '--visualize',
        default=False,
        action='store_true',
        help='visualize results?')
    parser.add_argument(
        '--output_filename', default=None, help='output filename')
    args = parser.parse_args()
    if args.size is not None:
        args.size = tuple(map(int, args.size[0]))
    return args


if __name__ == "__main__":
    main()
