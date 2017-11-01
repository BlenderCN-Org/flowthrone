cmake_minimum_required(VERSION 2.8)
project(flowthrone)

# If you have a relatively old (like: pre 5.2 version of gcc, you probably
# have to change this to std=c++11.
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -fPIC")

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2 -fopenmp")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DNDEBUG")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DEIGEN_NO_DEBUG")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
# Eigen3 master uses std::binder2nd which is deprecated.
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-deprecated-declarations")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS}")

set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "${CMAKE_COMMAND} -E time")

# Cmake dependencies
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake)
include(cmake/FindGlog.cmake)
include(cmake/FindGFlags.cmake)

find_package(OpenCV REQUIRED COMPONENTS opencv_core opencv_highgui opencv_imgproc opencv_video)
find_package(GTest REQUIRED)
find_package(GFlags REQUIRED)
find_package(Glog REQUIRED)

include_directories(
  ${GTEST_INCLUDE_DIRS}
  ${GLOG_INCLUDE_DIRS}
  ${GFLAGS_INCLUDE_DIR}
  ${OpenCV_INCLUDE_DIR}
  ${CMAKE_CURRENT_BINARY_DIR}
)

# Libraries begin here.
add_library(flowthrone STATIC
  flowthrone/cpp/io.cpp
  flowthrone/cpp/io.h
  flowthrone/cpp/visualization.cpp
  flowthrone/cpp/visualization.h
)
target_link_libraries(flowthrone
  ${GLOG_LIBRARIES}
  ${OpenCV_LIBS}
)


add_library(test_utils STATIC
  flowthrone/cpp/test_utils.cpp
  flowthrone/cpp/test_utils.h
)
target_link_libraries(test_utils
  ${GLOG_LIBRARIES}
  ${OpenCV_LIBS}
)

# Test definitions.
add_executable(io_test flowthrone/cpp/io_test.cpp)
target_link_libraries(io_test
  test_utils
  flowthrone
  ${GTEST_BOTH_LIBRARIES}
  ${OpenCV_LIBS}
)

add_executable(visualization_test flowthrone/cpp/visualization_test.cpp)
target_link_libraries(visualization_test
  flowthrone
  ${GTEST_BOTH_LIBRARIES}
  ${GFLAGS_LIBRARIES}
  ${OpenCV_LIBS}
)

# List of tests.
enable_testing()
add_test(io_test io_test)
add_test(visualization_test visualization_test)
