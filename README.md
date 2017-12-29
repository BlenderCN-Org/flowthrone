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

## antipasto

After installing the prerequisites in the *aperitivo* step you can build the
package:                                                 
                                                                                
    $ mkdir build; cd build                                                     
    $ cmake ..                                                                  
    $ make all                                                                  
    $ make test 


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
