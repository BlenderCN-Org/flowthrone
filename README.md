# flowthrone

## aperitivo
Follow the standard installation instructions for the following libraries:      
* [Glog](https://github.com/google/glog) (>=0.3.3)                              
* [GFlags](https://github.com/gflags/gflags)                                    
* [Googletest](https://github.com/google/googletest)
* OpenCV (2.4+)

## antipasto
Then you can build the package:                                                 
                                                                                
    $ mkdir build; cd build                                                     
    $ cmake ..                                                                  
    $ make all                                                                  
    $ make test 

## primo
To try running/visualizing optical flow:
    
    $ ./optical_flow_main --helpshort
