"""
Example of using optical flow in python.
This is just a demo used to illustrate how the model can be loaded / run.
"""
from __future__ import print_function
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
from input_feeder import VideoFeeder, ImageFeeder


def guess_network_size(width, height):
    import math
    # Generally this should be '0', unless for some reason you want to create
    # a network with a smaller input resolution. This could be because:
    #   - you don't have enough GPU memory
    #   - you are in a hurry and just want to see results FAST
    #   - you feel that the (large) network is not behaving well and believe
    #     that a smaller network will do better (for example your video
    #     sequence has very large deformations that the model is not able to
    #     capture).
    extra_smalling_factor = 0
    ratio = width / float(height)
    # This is a hack: we basically need to make sure that input dimensions are
    # evenly divisible by n-th power of two (here n=6).
    pow_2_6 = pow(2, 7 + extra_smalling_factor)
    net_height = int(math.ceil(height / float(pow_2_6)) * pow_2_6)
    size = [int(math.ceil(ratio * net_height / pow_2_6)) * pow_2_6, net_height]
    size = [
        size[0] / pow(2, extra_smalling_factor),
        size[1] / pow(2, extra_smalling_factor)
    ]
    print("Guessed an okay input size to be: {}".format(size))
    return size


def main():
    args = parse_args()
    # Load a pair of images or video.
    if args.video is not None:
        feeder = VideoFeeder(args.video, scale=args.input_scale)
    else:
        feeder = ImageFeeder(
            [args.image1, args.image2], scale=args.input_scale)

    # Peek at the first image (this is not necessary, but useful to figure out
    # the size.
    image1 = feeder.next()
    log.check(image1 is not None,
              "Could not get any images from specified input!")

    # Normally one can/should create a network without trying to infer the size
    # using image dimensions.
    if args.size is None:
        args.size = guess_network_size(
            width=image1.shape[1], height=image1.shape[0])

    session_config = tf.ConfigProto()
    session_config.gpu_options.allow_growth = True
    sess = tf.Session(config=session_config)

    if args.model_path is not None:
        model_filename = args.model_path
    else:
        model_handle = model_config.MODELS[args.model]
        # Downloads the model if necessary.
        model_handle.load_if_needed()
        model_filename = model_handle.path
    print("Loading a model from {}".format(model_filename))
    # Expensive: usually should do only once for the entire video sequence, or
    # for a collection of images.
    flow_solver = OpticalFlowModel(
        session=sess, size=args.size, model_path=model_filename)

    while not feeder.done():
        image2 = feeder.next()

        t1 = time.time()
        flow = flow_solver.run(image1, image2)
        t2 = time.time()
        print("Elapsed {} secs".format(t2 - t1))

        uv = compute_flow_color(u=flow[:, :, 0], v=flow[:, :, 1])
        if args.visualize:
            cv2.imshow("images", np.concatenate([image1, image2], axis=1))
            cv2.imshow("image", uv)
            key = cv2.waitKey(args.wait_time)
            if key == 27:  # escape to exit right away.
                exit(1)

        if args.output_filename is not None:
            cv2.imwrite(args.output_filename, uv)
            print("Wrote output to {}".format(args.output_filename))

        image1 = image2


def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--model', choices=model_config.MODELS.keys(),
        default=None)  #sorted(model_config.MODELS.keys())[::-1][0])
    group.add_argument(
        '--model_path', default=None, help='Path to the model checkpoint')
    parser.add_argument(
        '--size', action='append', nargs=2, help='network size')
    parser.add_argument(
        '--image1', default=None, help='path to the first image')
    parser.add_argument(
        '--image2', default=None, help='path to the second image')
    parser.add_argument('--video', default=None, help='path to input video')
    parser.add_argument(
        '--wait_time',
        type=int,
        default=0,
        help='cv::waitKey wait time in milliseconds')
    parser.add_argument(
        '--visualize',
        default=False,
        action='store_true',
        help='visualize results?')
    parser.add_argument(
        '--input_scale',
        default=1.0,
        type=float,
        help='Scale factor by which to resize input before feeding it to the network'
    )
    parser.add_argument(
        '--output_filename', default=None, help='output filename')
    args = parser.parse_args()

    if args.size is not None:
        args.size = tuple(map(int, args.size[0]))

    if args.video is None:
        if (args.image1 is None or args.image2 is None):
            parser.print_help()
            print("Must specify --image1 and --image2 inputs -- else can "
                  "specify --video.")
            exit(1)

    if args.video is not None:
        if args.image1 is not None or args.image2 is not None:
            parser.print_help()
            print("Do not specify --image1/--image2 if you are using --video "
                  "as input.")
            exit(1)

    if args.video is not None and args.output_filename is not None:
        parser.print_help()
        print("Please do not specify --output_filename if you also specified "
              "--video. There is currently no support for writing output "
              "video sequences, and until there is, --output_filename will "
              "be meaningless.")
        exit(1)

    return args


if __name__ == "__main__":
    main()
