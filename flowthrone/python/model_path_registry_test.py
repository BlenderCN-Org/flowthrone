import cv2
import numpy as np
import os
import unittest
from model_path_registry import ModelPathRegistry


class ModelPathRegistryTest(unittest.TestCase):
    def test_model_registry(self):
        """ Verifies that model registry class mostly works okay. """
        registry = ModelPathRegistry()

        msg = 'Should have at least one model.'
        self.assertGreater(len(registry.list()), 0, msg=msg)

        # Monkey-patch a method in ModelPathHandle that otherwise would trigger
        # a download.
        for name in registry._models.keys():
            registry._models[name].load = None

        model_path_handle = registry.get_latest()

        msg = 'Should have provided a local path (possibly nonexistent).'
        self.assertGreater(len(model_path_handle), 0, msg=msg)


if __name__ == '__main__':
    unittest.main(verbosity=2)
