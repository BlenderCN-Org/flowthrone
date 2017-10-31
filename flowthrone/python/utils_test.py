import cv2
import numpy as np
import os
import unittest
import utils

class TestReadWriteFlo(unittest.TestCase):
  test_filename = 'test_filename.flo'
  tolerance = 1e-3
  
  def tearDown(self):
    if os.path.exists(self.test_filename):
      os.remove(self.test_filename)

  def test_read_write_flo(self):
    """ Verifies that reading/writing .flo files works okay """
    width = 50
    height = 100

    flow = np.random.uniform(-5, +5, [height, width, 2])
    utils.write_flo(self.test_filename, flow)
    flow_from_file = utils.read_flo(self.test_filename)
    
    # Verify that the size is correct:
    self.assertEqual(flow_from_file.shape[0], height)
    self.assertEqual(flow_from_file.shape[1], width)
    self.assertEqual(flow_from_file.shape[2], 2)
    # Verify that flow contents match.   
    self.assertLessEqual(np.sum(abs(flow - flow_from_file)), self.tolerance)

class TestColorMap(unittest.TestCase):
  gtimage = np.zeros([0,0,0])
  # per-pixel error
  tolerance = 1e-2
  
  def setUp(self):
    image_filename = '../testdata/gtflow.jpg'
    assert os.path.exists(image_filename)
    self.gtimage = cv2.imread(image_filename)/255.0
  
  def test_color_map(self):
    """ Verify that the colormap is correct """
    v = np.linspace(0.5, 99.5, 100)
    xx, yy = np.meshgrid(v, v)
    flow = np.zeros([100, 100, 2])
    flow[:,:,0] = xx - 50
    flow[:,:,1] = yy - 50
    
    image = utils.compute_flow_color(flow[:,:,0], flow[:,:,1])/255.

    # Make sure that error between the correct colormap and ours is small.
    err = np.sum(abs(image - self.gtimage))/np.prod(image.shape)
    self.assertLessEqual(err, self.tolerance)

if __name__ == '__main__':
  unittest.main(verbosity=2)

