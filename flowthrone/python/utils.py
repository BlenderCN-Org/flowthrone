""" Utilities for optical flow """
import cv2
import numpy as np
import struct

def read_flo(filename):
  """
  Reads binary .flo file into a numpy array (cv::Mat) 
  """
  fid = open(filename, 'rb')
  tag = fid.read(4)
  width = struct.unpack('i', fid.read(4))[0]
  height = struct.unpack('i', fid.read(4))[0]
  n = width * height * 2 
  data = struct.unpack('f'*n, fid.read(4*n))
  return np.reshape(data, [height, width, 2])

def write_flo(filename, flow):
  """
  Writes binary .flo file given a numpy array (cv::Mat)
  """
  fid = open(filename, 'wb')
  fid.write(struct.pack('f', 202021.25))
  fid.write(struct.pack('i', flow.shape[1]))
  fid.write(struct.pack('i', flow.shape[0]))
  n = np.prod(flow.shape)
  fid.write(struct.pack('f'*n, *np.reshape(flow, n)))

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

def compute_flow_color(uv=None, u=None, v=None):
  """ Returns a BGR image colored according to optical flow. You can either
      pass two components (horizontal and vertical displacements) separately,
      or pack them into one argument. """
  # TODO(vasiliy): should force named arguments.
  assert uv is not None or (u is not None and v is not None)
  if uv is not None:
    u = uv[:,:,0]
    v = uv[:,:,1]

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


def warp_with_flow(image, uv):
  X, Y = np.meshgrid(range(image.shape[1]), range(image.shape[0]))
  x_warp = np.asarray(uv[:,:,0] + X, dtype='float32')
  y_warp = np.asarray(uv[:,:,1] + Y, dtype='float32')
  return cv2.remap(image, x_warp, y_warp, cv2.INTER_LINEAR)


def compute_residual(image0, image1, uv):
  return image0 - warp_with_flow(image1, uv)

""" Rescales flow field. """
def resample_flow(uv, out_shape):
    assert uv.shape[2] == 2, "Flow field must have two channels!"
    assert len(out_shape) == 2 or len(out_shape) == 3

    scale_x = out_shape[0] / float(uv.shape[0])
    scale_y = out_shape[1] / float(uv.shape[1])
    uv_out = cv2.resize(uv, (out_shape[0], out_shape[1]))
    uv_out[:,:,0] *= scale_x
    uv_out[:,:,1] *= scale_y
    return uv_out
