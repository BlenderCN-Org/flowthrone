---
layout: default
---

# Contents

### Table of Contents
* [Overview](#overview)
* [Models](#models)
* [flowthrone/cpp](#flowthrone-cpp)
  * [Library](#lib-cpp)
  * [Tools](#tools-cpp)
* [flowthrone/python](#flowthrone-python)



### Overview <a name="overview"></a>
FLOWTHRONE is a library for modern dense optical flow. Since most recent
approaches for solving the problem leverage deep learning, so does flowthrone,
using tensorflow for network inference. Network training is done in python,
most inference, evaluation, and additional features are in C++. Thus, the source
is split into two parts `flowthrone/python` contains training code, while
`flowthrone/cpp` is the rest.

### Models <a name="models"></a>
Current models are based on [Flownet](https://arxiv.org/abs/1504.06852) and
on [PWC-Net](https://arxiv.org/abs/1709.02371), but the implementations do not
precisely follow versions described in the above papers.

### FLOWTHRONE-C++ <a name="flowthrone-cpp"></a>

### Library <a name="lib-cpp"></a>

* `optical_flow_model.h` \\
Interface implemented by classes that perform optical flow estimation.

* `io.h` \\
File input/output, including input/output of FLO files.

* `visualization.h` \\
Utilities for canonical optical flow visualization.

* `evaluation.h` \\
Utilities for calculating endpoint/angular error, consistent with
[Sintel](http://sintel.is.tue.mpg.de/results) evaluation criteria.

* `flow_smoothing` \\
Cross-bilateral filtering applied for refining/post-processing flow fields.

### Tools <a name="tools-cpp"></a>
* `optical_flow_tool.cpp` \\
Binary for running optical flow on a pair of frames, or a video.

* `evaluation_tool.cpp` \\
Binary for evaluating a model on a standard dataset.


### FLOWTHRONE-python <a name="flowthrone-python"></a>

* `flownet.py` \\
Implementation of [Flownet](https://arxiv.org/abs/1504.06852)\\
(*"FlowNet: Learning Optical Flow with Convolutional Networks"*
Philipp Fischer, Alexey Dosovitskiy, Eddy Ilg, Philip Häusser, Caner Hazırbaş, Vladimir Golkov, Patrick van der Smagt, Daniel Cremers, Thomas Brox, ICCV 2015)

* `pwcnet.py` \\
Implementation of [PWC-Net](https://arxiv.org/abs/1709.02371)\\
(*"PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume"* by Deqing Sun, Xiaodong Yang, Ming-Yu Liu, Jan Kautz, CVPR 2018)

* `blender/*` \\
Tools for creating synthetic scenes and generating groundtruth flow using Blender.
