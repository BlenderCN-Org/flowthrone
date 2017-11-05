""" Utilities for generating a simple scene using Blender and extracting
    image data and optical flow. """
import cv2
import numpy as np
import os
import struct
import sys
import array
import Imath
import OpenEXR
import subprocess

class ExrDataReader:
  _image_size = None
  _data = None
  _pt = Imath.PixelType(Imath.PixelType.FLOAT)

  def __init__(self, fn):
    self._data = OpenEXR.InputFile(fn)
    box = self._data.header()['dataWindow']
    self._image_size = [box.max.y - box.min.y + 1, box.max.x - box.min.x + 1]
  
  def backward_flow(self):
    x = +np.asarray(array.array('f', 
        self._data.channel('RenderLayer.Vector.X', self._pt)))
    y = -np.asarray(array.array('f', 
        self._data.channel('RenderLayer.Vector.Y', self._pt)))
    uv = np.zeros([self._image_size[0], self._image_size[1], 2])
    uv[:,:,0] = np.reshape(x, self._image_size) 
    uv[:,:,1] = np.reshape(y, self._image_size) 
    return uv

  def forward_flow(self):
    x = -np.asarray(array.array('f', 
        self._data.channel('RenderLayer.Vector.Z', self._pt)))
    y = +np.asarray(array.array('f', 
        self._data.channel('RenderLayer.Vector.W', self._pt)))
    uv = np.zeros([self._image_size[0], self._image_size[1], 2])
    uv[:,:,0] = np.reshape(x, self._image_size) 
    uv[:,:,1] = np.reshape(y, self._image_size) 
    return uv

  def depth_buffer(self):
    z = np.asarray(array.array('f', 
        self._data.channel('RenderLayer.Depth.Z', self._pt)))
    return np.reshape(z, self._image_size)


def get_blender_command(output_path, p1, p2, scale, image_size):
  """ Returns a blender command that generates a pair of images and flows. """
  formatter = lambda x : '{:6f}'.format(x)
  return ['blender', '--background', '--factory-startup', \
          '--python', 'blendbox.py', '--',
          '--filepath', output_path] + \
          (['--pose1'] + map(formatter, p1) + \
           ['--pose2'] + map(formatter, p2)) + \
          ['--image_size', str(image_size)] + \
          (['--scale'] + map(formatter, scale))


def generate_example(p1, p2, scale, imsize, temporary_output_path='/tmp/'):
  """ Runs blender and returns a dictionary with a pair of images, optical
      flow and depth buffers, for a simple scene. """
  cmd = get_blender_command(temporary_output_path, p1, p2, scale, imsize)
  subprocess.check_call(cmd)
 
  exr1_fn = os.path.join(temporary_output_path, '0000.exr')
  exr2_fn = os.path.join(temporary_output_path, '0001.exr')
  img1_fn = os.path.join(temporary_output_path, '0000.jpg') 
  img2_fn = os.path.join(temporary_output_path, '0001.jpg')
  
  exr1_accessor = ExrDataReader(exr1_fn)
  exr2_accessor = ExrDataReader(exr2_fn)
  uv_fwd = exr1_accessor.forward_flow()
  uv_bwd = exr2_accessor.backward_flow()
  depth1 = exr1_accessor.depth_buffer()
  depth2 = exr2_accessor.depth_buffer()

  img1 = cv2.imread(img1_fn)
  img2 = cv2.imread(img2_fn)
  os.remove(exr1_fn)
  os.remove(exr2_fn)
  os.remove(img1_fn)
  os.remove(img2_fn)
   
  return {'image1': img1, 'image2': img2, \
          'uv_fwd': uv_fwd, 'uv_bwd': uv_bwd, \
          'depth1': depth1, 'depth2': depth2}
