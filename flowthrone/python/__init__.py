# Hack to import all .py files as modules.
from os.path import dirname, isfile, basename
import glob

modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = [
    basename(f)[:-3] for f in modules
    if isfile(f) and not f.endswith('__init__.py')
]

del dirname, isfile, basename, glob
