""" Utilities for optical flow """
import cv2
import numpy as np
import struct

def read_flo(filename):
  """
  Reads binary .flo file into a numpy array (cv::Mat) 
  TODO(vasiliy): this is far slower than it can be.
  """
  fid = open(filename, 'rb')
  tag = fid.read(4)
  width = struct.unpack('i', fid.read(4))[0]
  height = struct.unpack('i', fid.read(4))[0]
  flow = np.zeros([height, width, 2])
  for r in range(height):
    for c in range(width):
      flow[r,c,0] = struct.unpack('f', fid.read(4))[0]
      flow[r,c,1] = struct.unpack('f', fid.read(4))[0]
  return flow

def write_flo(filename, flow):
  """
  Writes binary .flo file given a numpy array (cv::Mat)
  TODO(vasiliy): this is far slower than it can be.
  """
  fid = open(filename, 'wb')
  fid.write(struct.pack('f', 202021.25))
  fid.write(struct.pack('i', flow.shape[1]))
  fid.write(struct.pack('i', flow.shape[0]))
  for r in range(flow.shape[0]):
    for c in range(flow.shape[1]):
      fid.write(struct.pack('f', flow[r,c,0]))
      fid.write(struct.pack('f', flow[r,c,1]))

def make_colorwheel():
  ry = 15
  yg = 6
  gc = 4
  cb = 11
  bm = 13
  mr = 6
  colors = []
  for i in range(ry):
    colors.append([0, int(255.0*i/float(ry)), 255])
  for i in range(yg):
    colors.append([0, 255, 255 - int(255.0*i/float(yg))])
  for i in range(gc):
    colors.append([int(255*i/gc), 255, 0])
  for i in range(cb):
    colors.append([255, 255 - int(255.0*i/float(cb)), 0])
  for i in range(bm):
    colors.append([255, 0, int(255.0 * i / float(bm))])
  for i in range(mr):
    colors.append([255 - int(255.0*i/float(mr)), 0, 255])
  colors = [np.asarray(c) for c in colors]
  return np.asarray(colors)

def compute_flow_color(u, v):
  """ Returns a BGR image colored according to optical flow """
  colorwheel = make_colorwheel()/255.
  num_colors = len(colorwheel)

  mag = np.sqrt(u*u + v*v)
  uv_max_mag = np.max(mag)
  mag_normalized = mag / (uv_max_mag + 1e-10)
  angle = np.arctan2(-v, -u)/np.pi # in [-1, 1]
  angle_normalized = (angle + 1.0)/2.0 # in [0, 1]
  fk = angle_normalized * (num_colors-1)
  k0 = np.floor(fk) % num_colors
  k1 = (k0 + 1) % num_colors
  f = fk - k0 
  k0 = np.asarray(k0, dtype='int')
  k1 = np.asarray(k1, dtype='int')
  color0 = colorwheel[k0]
  color1 = colorwheel[k1]

  image = np.zeros([u.shape[0], u.shape[1], 3])
  for i in range(3):
    c0 = color0[:,:,i]
    c1 = color1[:,:,i]
    color = (1-f)*c0 + f*c1
    image[:,:,i] = 1.0 - mag_normalized * (1-color)
  image = np.asarray(np.minimum(255, np.floor(255*image)), dtype='uint8')
  return image