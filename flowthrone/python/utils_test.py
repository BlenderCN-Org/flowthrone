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
        self.assertLessEqual(
            np.sum(abs(flow - flow_from_file)), self.tolerance)


class TestColorMap(unittest.TestCase):
    gtimage = np.zeros([0, 0, 0])
    # per-pixel error
    tolerance = 1e-2

    def setUp(self):
        image_filename = '../testdata/gtflow.jpg'
        assert os.path.exists(image_filename)
        self.gtimage = cv2.imread(image_filename) / 255.0

    def test_color_map(self):
        """ Verify that the colormap is correct """
        v = np.linspace(0.5, 99.5, 100)
        xx, yy = np.meshgrid(v, v)
        flow = np.zeros([100, 100, 2])
        flow[:, :, 0] = xx - 50
        flow[:, :, 1] = yy - 50

        image = utils.compute_flow_color(
            u=flow[:, :, 0], v=flow[:, :, 1]) / 255.

        # Make sure that error between the correct colormap and ours is small.
        err = np.sum(abs(image - self.gtimage)) / np.prod(image.shape)
        self.assertLessEqual(err, self.tolerance)


class TestWarpWithFlow(unittest.TestCase):
    image = None
    tolerance = 1e-3

    def setUp(self):
        self.image = np.random.uniform(0.0, 1.0, [50, 100])

    def test_identity(self):
        """ Verify that uv=0 does not change the image. """
        uv = np.zeros(list(self.image.shape) + [2])
        image_warped = utils.warp_with_flow(self.image, uv)
        err = np.linalg.norm(image_warped - self.image)
        self.assertLessEqual(err, self.tolerance)

    def test_simple_shift(self):
        """ Verify that a simple shift works correctly. """
        uv = np.zeros(list(self.image.shape) + [2])
        uv[:, :, 0] = 1
        image_warped_gt = np.zeros(self.image.shape)
        image_warped_gt[:, 0:-1] = np.copy(self.image[:, 1:])
        image_warped_gt[:, -1] = 0

        image_warped = utils.warp_with_flow(self.image, uv)
        err = np.linalg.norm(image_warped - image_warped_gt)
        self.assertLessEqual(err, self.tolerance)


class TestComputeResidual(unittest.TestCase):
    def test_simple(self):
        """ Create a simple scenario where a rectangle is moving to the right.
          Given perfect flow, residual should be nonzero only in the occluded
          region. """
        uv_fwd = np.zeros([9, 9, 2])
        uv_fwd[3:6, 3:6, 0] = 1
        i0 = np.zeros([9, 9])
        i1 = np.zeros([9, 9])
        i0[3:6, 3:6] = 255
        i1[3:6, 4:7] = 255
        err = utils.compute_residual(i0, i1, uv_fwd)
        # Verify that in the occluded region residual is large.
        self.assertGreater(np.linalg.norm(err[3:6, 6]), 0.0)
        # Verify that outside residual is zero.
        err_fixed_occ = np.copy(err)
        err_fixed_occ[3:6, 6] = 0
        self.assertEqual(np.linalg.norm(err_fixed_occ), 0.0)


class TestResampleFlow(unittest.TestCase):
    def test_simple(self):
        """ Create a simple scenario where a rectangle is moving to the right.
          Given perfect flow, residual should be nonzero only in the occluded
          region. """
        uv = np.ones([10, 20, 2])
        uv[:, :, 0] = -5
        uv[:, :, 1] = +10

        uv_out = utils.resample_flow(uv, [10, 10])
        uv_expected = np.concatenate(
            [np.ones([10, 10, 1]) * (-2.5),
             np.ones([10, 10, 1]) * (+10)],
            axis=2)
        # Verify that in the occluded region residual is large.
        self.assertGreater(np.linalg.norm(uv_expected - uv_out), 0.0)

class TestLoadPfm(unittest.TestCase):
    def test_simple(self):
        fn = '/home/vasiliy/data/ChairsSDHom/data/train/flow/04190.pfm'
        image = utils.read_pfm(fn)

        cv2.imshow("iamge", utils.compute_flow_color(image))
        cv2.waitKey(0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
