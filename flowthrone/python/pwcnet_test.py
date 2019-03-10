import tensorflow as tf
import os
import unittest
import numpy as np
from pwcnet import (FeaturePyramidExtractor, FeaturePyramidExtractorOptions, 
                    OpticalFlowEstimator, OpticalFlowEstimatorOptions,
                    ContextEstimator, ContextEstimatorOptions, 
                    PWCNet, PWCNetOptions, PWCNetTrainer)


def make_random_input(dim, channels):
    return tf.convert_to_tensor(
        np.random.uniform(0, 1, [1, dim, dim, channels]).astype(np.float32))


def make_random_uint8_input(dim, channels):
    return tf.convert_to_tensor(
        np.random.uniform(0, 255, [1, dim, dim, channels]).astype(np.uint8))


class FeaturePyramidExtractorTest(unittest.TestCase):
    image = None
    tolerance = 1e-3

    def setUp(self):
        tf.reset_default_graph()

    def test_weights_are_shared(self):
        """
        Tries to verify that weights are shared across different
        FeaturePyramidExtractor instances.
        """
        image1 = make_random_input(512, 3)
        image2 = make_random_input(512, 3)

        fpe1 = FeaturePyramidExtractor(image1)
        fpe2 = FeaturePyramidExtractor(image2)

        session = tf.Session()
        with session.as_default():
            names = [x.name for x in tf.global_variables()]

            # Print some helpful information.
            print "Variable names are: "
            for i, name in enumerate(names):
                print i, name
            print "Layers are: "
            for i, name in enumerate(fpe1.layers):
                print i, name
            # Note: need to subtract 1, since we added the original input to 'layers'.
            self.assertEqual(len(names), (len(fpe1.layers) - 1) * 2)
        session.close()

    def test_expected_dimensions(self):
        """
        Verifies that network levels dimensions are what they should be
        according to the paper.
        """
        opts = FeaturePyramidExtractorOptions()
        opts.NUM_FILTERS = [16, 32, 64, 96, 128, 192]

        net = FeaturePyramidExtractor(make_random_input(512, 3), opts)
        EXPECTED_SHAPES = [
            [1, 512, 512, 3],
            [1, 256, 256, 16],
            [1, 128, 128, 32],
            [1, 64, 64, 64],
            [1, 32, 32, 96],
            [1, 16, 16, 128],
            [1, 8, 8, 192],
        ]
        for i, EXPECTED_SHAPE in enumerate(EXPECTED_SHAPES):
            level_shape = net.get_level(i).shape.as_list()
            self.assertEqual(EXPECTED_SHAPE, level_shape)

    def test_with_batch_norm(self):
        """ At least verify that syntax doesnt break. """
        opts = FeaturePyramidExtractorOptions()
        opts.is_training = tf.Variable(True, dtype=tf.bool)

        net = FeaturePyramidExtractor(make_random_input(128, 3), opts)


class OpticalFlowEstimatorTest(unittest.TestCase):
     def setUp(self):
         tf.reset_default_graph()
 
     def test_expected_dimensions(self):
         """ Verify that dimensions of the layers match expectations. """
         DIM = 32
         x1 = make_random_input(DIM, channels=3)
         x2 = make_random_input(DIM, channels=3)
         uv = make_random_input(DIM / 2, channels=2)
         occ = make_random_input(DIM / 2, channels=1)
 
         estimator = OpticalFlowEstimator(x1, x2, uv, occ)
 
         self.assertEqual([DIM, DIM, 3],
                          estimator.get_x2_warped().shape.as_list()[1:])
         self.assertEqual([DIM, DIM, 2],
                          estimator.get_flow().shape.as_list()[1:])
         for layer in estimator.layers:
             self.assertEqual([DIM, DIM], layer.shape.as_list()[1:3])
 
     def test_runs_successfully(self):
         """
         Verifies that we can evaluate the network successfully, and that
         flow values do not get rectified out.
         """
         DIM = 32
         x1 = make_random_input(DIM, channels=3)
         x2 = make_random_input(DIM, channels=3)
         uv = make_random_input(DIM / 2, channels=2)
         occ = make_random_input(DIM / 2, channels=1)
 
         estimator = OpticalFlowEstimator(x1, x2, uv, occ)
         flow = estimator.get_flow()
         penultimate = estimator.get_penultimate_layer()
         session = tf.Session()
         with session.as_default():
             session.run(tf.global_variables_initializer())
             flow_vals = session.run([flow])
 
             nnz_frac = np.count_nonzero(flow_vals) / float(np.size(flow_vals))
             print 'Fraction of nonzero elements {}'.format(nnz_frac)
             # Zero values do appear here sometimes.
             self.assertGreater(nnz_frac, 0.01, \
                 msg='Expected nnz to be high, due to lack of ReLU: {}'.format(nnz_frac))
         session.close()
 
     def test_with_batch_norm(self):
         """ At least verify that syntax doesnt break. """
         opts = OpticalFlowEstimatorOptions()
         opts.is_training = tf.Variable(True, tf.bool)
 
         DIM = 64
         estimator = OpticalFlowEstimator(
             make_random_input(
                 DIM, channels=3),
             make_random_input(
                 DIM, channels=3),
             make_random_input(
                 DIM / 2, channels=2),
             make_random_input(
                 DIM / 2, channels=1))
 
 
class ContextEstimatorTest(unittest.TestCase):
    def setUp(self):
        tf.reset_default_graph()

    def test_expected_dimensions(self):
        """ Verifies that network dimensions are what they should be. """
        DIM = 64
        x = make_random_input(dim=DIM, channels=32)
        uv = make_random_input(dim=DIM, channels=2)
        occ = make_random_input(dim=DIM, channels=1)
        net = ContextEstimator(x, uv, occ)
        self.assertEqual([DIM, DIM, 2], net.get_flow().shape.as_list()[1:4])
        self.assertEqual([DIM, DIM, 1], net.get_occlusion().shape.as_list()[1:4])
        self.assertEqual([DIM, DIM, 3], net.layers[-1].shape.as_list()[1:4])

 
class PWCNetTest(unittest.TestCase):
    def setUp(self):
        tf.reset_default_graph()

    def test_expected_dimensions(self):
        DIM = 64
        x1 = make_random_uint8_input(dim=DIM, channels=3)
        x2 = make_random_uint8_input(dim=DIM, channels=3)
        
        opt = PWCNetOptions()
        opt.pyramid_opt.NUM_FILTERS = [16, 32, 64, 96, 128]
        opt.estimator_opt = {}
        for lvl in [5, 4, 3, 2, 1]:
          opt.estimator_opt[lvl] = OpticalFlowEstimatorOptions()

        net = PWCNet(x1, x2, options=opt)
        flow = net.get_output_flow()

        self.assertEqual([DIM, DIM, 2], flow.shape.as_list()[1:4])
        self.assertEqual(5, len(net.estimator_net))
        for lvl in range(5):
            flow = net.get_raw_flow(lvl)
            dim = pow(2, 1 + lvl)
            self.assertEqual([dim, dim, 2], flow.shape.as_list()[1:4])
 
 
class PWCNetTrainerTest(unittest.TestCase):
    def setUp(self):
        tf.reset_default_graph()

    def test_one_step_of_training(self):
        """ 
        Sets up the object used for training and runs one gradient descent
        step, while doing basic sanity checks.
        """
        DIM = 32
        BS = 4
        x1 = tf.placeholder(tf.uint8, [None, DIM, DIM, 3])
        x2 = tf.placeholder(tf.uint8, [None, DIM, DIM, 3])
        y = tf.placeholder(tf.float32, [None, DIM, DIM, 2])

        trainer = PWCNetTrainer(x1, x2, y)
        loss = trainer.get_loss()
        output_flow = trainer.get_output_flow()

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            x1_batch = np.random.uniform(0, 255,
                                         [BS, DIM, DIM, 3]).astype(np.uint8)
            x2_batch = np.random.uniform(0, 255,
                                         [BS, DIM, DIM, 3]).astype(np.uint8)
            y_batch = np.random.uniform(0, 255,
                                        [BS, DIM, DIM, 2]).astype(np.float32)

            optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
            loss_val, output_flow_val, _ = sess.run(
                [loss, output_flow, optimizer],
                feed_dict={x1: x1_batch,
                           x2: x2_batch,
                           y: y_batch})

            self.assertNotEqual(0.0, loss_val, 'Zero loss is surprising!')
            frac_nnz = np.count_nonzero(output_flow_val) / float(output_flow_val.size)
            self.assertLess(0.8, frac_nnz, \
                    'Should not have many zeros in output.')


if __name__ == '__main__':
    # There is absolutely no reason to use GPU for these tests, and this
    # appears to be the most reliable way to disable GPU usage in tensorflow.
    os.environ['CUDA_VISIBLE_DEVICES'] = ''
    unittest.main(verbosity=2)
