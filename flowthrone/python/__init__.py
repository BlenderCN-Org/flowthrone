# Hack to import all .py files as modules.
from os.path import dirname, isfile, basename
import glob

EXCLUDED_FILES = [
    'utils_test.py',
    'tf_utils_test.py',
    'train_tool.py',
    '__init__.py'
]
def is_module(f):
    return isfile(f) and not any([f.endswith(exc) for exc in EXCLUDED_FILES])

modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = [basename(f)[:-3] for f in modules if is_module(f)]
print __all__
del dirname, isfile, basename, glob, is_module, EXCLUDED_FILES
