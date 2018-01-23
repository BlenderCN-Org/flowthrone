# flowthrone

## aperitivo
Follow the standard installation instructions for the following libraries:      
* [boost](http://www.boost.org/users/download/)
* [Glog](https://github.com/google/glog) (>=0.3.3)                              
* [GFlags](https://github.com/gflags/gflags)                                    
* [Googletest](https://github.com/google/googletest)
* [Google Protocol Buffers](https://github.com/google/protobuf) 
  You should use [this version](http://mirror.bazel.build/github.com/google/protobuf/archive/0b059a3d8a8f8aa40dde7bea55edca4ec5dfea66.tar.gz) due to tensorflow compatibility issues, or at the very least it should be >= 3.4.0
* OpenCV (2.4+)
* [Eigen](http://eigen.tuxfamily.org/)
  You should use [this version](https://bitbucket.org/eigen/eigen/get/429aa5254200.tar.gz) due to tensorflow compatibility issues.
* [Tensorflow](https://www.tensorflow.org/)
  Installing tensorflow is a whole separate meal; the steps are roughly:
  1. Clone [tensorflow](https://github.com/tensorflow/tensorflow/tree/r1.4/)
     repository and checkout `r1.4`.
  2. Run `build_and_install_tensorflow.py` which will install a tensorflow 
     shared library on your system.

## antipasto

After installing the prerequisites in the *aperitivo* step you can build the
package:                                                 
                                                                                
    $ mkdir build; cd build                                                     
    $ cmake ..                                                                  
    $ make all                                                                  
    $ make test 

This step will compile everything that should be compiled, will download the
tensorflow model, and will modify `flowtrhone.pbtxt` options to point to it. 

## primo
To try running/visualizing optical flow:
    
    $ ./optical_flow_tool --helpshort

To evaluate/benchmark optical flow:
  
    $ ./evaluation_tool --helpshort

## dolce (python installation)

    $ python setup.py build

Then if you really need a system-wide install (not sure why):
    
    $ python setup.py install
    
Alternatively, could do:

    >>> sys.path.append(os.path.join(pwd, 'build/lib.linux-x86_64-2.7'))

(or wherever the library was installed) in your python interpreter. Then:

    >>> import flowthrone


## contact

[email](mailto:karasev00@gmail.com)
