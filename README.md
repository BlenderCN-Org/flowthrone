# flowthrone

## aperitivo
Follow the standard installation instructions for the following libraries:      
* [Glog](https://github.com/google/glog) (>=0.3.3)                              
* [GFlags](https://github.com/gflags/gflags)                                    
* [Googletest](https://github.com/google/googletest)
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
    
    $ ./optical_flow_main --helpshort


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
