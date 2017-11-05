""" Script used to generate a collection of groundtruth examples for optical
    flow. This is a programmatic way to generate a toy dataset for 
    optical flow.
    Since it relies on Blender, we can (in principle) extend it to generate
    more complex scenes.
    USAGE:
      python generate_groundtruth_examples.py --output_path /tmp/
    will write 100 examples to /tmp/.
    Each example is a tuple:
      - img1.jpg (image at t0)
      - img2.jpg (image at t1)
      - flow1.flo (the 'forward' flow)
      - flow2.flo (the 'backward' flow)

    Blender provides a depth map from which we could estimate the occlusion
    masks, but currently this is not done.
"""

import argparse
import cv2
import hashlib
import numpy as np
import os
import sys
from blender_utils import generate_example

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import write_flo, compute_flow_color, warp_with_flow

def main():
  parser = argparse.ArgumentParser(description='Generates a toy flow dataset.')
  parser.add_argument('--num_examples', default=100, type=int,
                      help='Number of examples to generate')
  parser.add_argument('--output_path', default='/tmp/', help='Output path')
  parser.add_argument('--image_size', default=64, type=int, help='Image size')
  parser.add_argument('--max_displacement', default=2.0, type=float)
  parser.add_argument('--box_aspect_range', default=2.0, type=float)
  parser.add_argument('--in_plane_motion', action='store_true', default=False,
                      help='Whether motion should be limited to be in-plane.')
  parser.add_argument('--visualize', action='store_true')


  args = parser.parse_args()
  generate_groundtruth_examples(args)


def generate_groundtruth_examples(args):
  """ 
  Generates n (img1, img2, uv1, uv2) tuples and writes results to
  output_path / %03d_{0,1}.{flo, jpg}
  """
  if not os.path.exists(args.output_path):
    os.mkdir(args.output_path)

  for i in range(args.num_examples):
    print "Working on example %d/%d" % (i, args.num_examples)
    p1 = np.asarray([0, 4, 0], dtype='float64')
    d1 = np.random.uniform(-0.5, 0.5, 3)*args.max_displacement
    d2 = np.random.uniform(-0.5, 0.5, 3)*args.max_displacement
    if args.in_plane_motion:
      d1[1] = 0.0
      d2[1] = 0.0
    p1 += d1
    p2 = p1 + d2
    box_scale = np.random.uniform(1.0/args.box_aspect_range, args.box_aspect_range, 2)
    temporary_path = os.path.join('/tmp/', 
            '{:08d}/'.format(np.random.randint(1e8)))
    os.mkdir(temporary_path)
    data = generate_example(p1, p2, box_scale, args.image_size, temporary_path)
    os.removedirs(temporary_path)
    
    img1_fn = os.path.join(args.output_path, '%06d_img1.jpg' % i)
    img2_fn = os.path.join(args.output_path, '%06d_img2.jpg' % i)
    flo1_fn = os.path.join(args.output_path, '%06d_flow1.flo' % i)
    flo2_fn = os.path.join(args.output_path, '%06d_flow2.flo' % i)

    cv2.imwrite(img1_fn, data['image1'])
    cv2.imwrite(img2_fn, data['image2'])
    write_flo(flo1_fn, data['uv_fwd'])
    write_flo(flo2_fn, data['uv_bwd'])
    
    for fn in [img1_fn, img2_fn, flo1_fn, flo2_fn]:
      print "Wrote {}".format(fn)
    if args.visualize:
      images = np.concatenate([data['image1'], data['image2']], axis=1)
      flows  = np.concatenate([compute_flow_color(data['uv_fwd']), 
                               compute_flow_color(data['uv_bwd'])], axis=1)
      depths = np.concatenate([data['depth1'], data['depth2']], axis=1)
      depths = np.asarray(depths / np.max(depths)*255, dtype='uint8')
      depths = np.repeat(
              np.reshape(depths, [depths.shape[0], depths.shape[1], 1]), 3, axis=2)

      cv2.imshow("image and flow", 
              np.concatenate([images, flows, depths], axis=0))
      key = cv2.waitKey(0)
      if key == 27:
        break


if __name__ == "__main__":
  main()
