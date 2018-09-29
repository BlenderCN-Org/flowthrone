---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

# Installation

### Overview (C++)

FLOWTHRONE uses CMake as a build system and depends on the following:

* [boost](http://www.boost.org/users/download/)                                 
* [Glog](https://github.com/google/glog) (>=0.3.3)                              
* [GFlags](https://github.com/gflags/gflags)                                    
* [Googletest](https://github.com/google/googletest)                            
* [Google Protocol Buffers](https://github.com/google/protobuf)
* OpenCV (2.4+)                                                                 
* [Eigen](http://eigen.tuxfamily.org/)                                          
* [Tensorflow](https://www.tensorflow.org/)

The tensorflow dependency requires that system-installed versions of Eigen and
Protobuf match the ones listed in tensorflow BUILD files.

### Installation Steps (Dependencies)

* **Boost**, **Glog**, **GFlags** and **GTest**

      $ sudo apt-get install libboost-system libboost-filesystem          
      $ sudo apt-get install libgflags-dev libgoogle-glog-dev libgtest-dev

* **Google Protocol Buffers**:
                                                                                
    Download the version listed in tensorflow's `workspace.bzl` and follow
    installation instructions in the package.

* **Eigen**:
                                                                                
    Install the version listed in tensorflow's `workspace.bzl`

* **OpenCV**:

    In certain cases it might be sufficient to run:

      $ sudo apt-get install libopencv-dev

    To support video decoding/encoding, may need to do:

      $ git clone https://github.com/opencv/opencv.git && cd opencv &&        
      $ git fetch origin 2.4 && git checkout 2.4                              
      $ cd opencv && mkdir build && cd build && cmake ..               \      
         -DBUILD_EXAMPLES=OFF -DBUILD_TESTS=OFF -DBUILD_PERF_TESTS=OFF \      
         && make && sudo make install
 
* **Tensorflow**:

    Clone a recent version of tensorflow. 

    Run `build_and_install_tensorflow.py` in the root of `flowthrone` repo. 
    This script will install the tensorflow shared library on your system 
    and will make it available to cmake:

      $ python build_and_install_tensorflow.py --tf_repo /your-tf-repo/

    
### Installation Steps (Library)

After doing all steps above, you are probably ready to build `flowthrone`.  
This is simple (assuming the steps above worked okay):                      
                                                                                
    $ cd flowthrone && mkdir build && cd build && cmake ..
    $ make -j                                             
    $ make test                                           
                                                                                
This will install the default/latest tensorflow model into `build/model_*` and 
will also install the default configuration for running optical flow into 
`build/config/flowthrone.pbtxt`.


At this stage, if everything went well, you could try running optical flow on
a pair of images:                                                           
                                                                                
    $ ./optical_flow_tool --img1 /path/to/image1.jpg \
                          --img2 /path/to/image2.jpg \
                          --output /tmp/blah.jpg     \
                          --visualize                \
                          --scale 1.0                \

### Overview (Python)

Having OpenCV and tensorflow should be sufficient.
