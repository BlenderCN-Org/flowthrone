# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='flowthrone',
    description='Dense optical flow',
    url='https://github.com/vasiliykarasev/flowthrone',
    author='vasiliykarasev',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'paramiko',
        'cv2',
    ],
)
