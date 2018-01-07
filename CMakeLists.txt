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
include(cmake/FindEigen.cmake)
include(cmake/FindTensorFlow.cmake)

find_package(Boost REQUIRED COMPONENTS system filesystem)
find_package(OpenCV REQUIRED COMPONENTS opencv_core opencv_highgui opencv_imgproc opencv_video)
find_package(GTest REQUIRED)
find_package(GFlags REQUIRED)
find_package(Glog REQUIRED)
find_package(Protobuf REQUIRED)
find_package(Eigen)
find_package(TensorFlow)

include_directories(
  ${GTEST_INCLUDE_DIRS}
  ${GLOG_INCLUDE_DIRS}
  ${GFLAGS_INCLUDE_DIR}
  ${OpenCV_INCLUDE_DIR}
  ${Eigen_INCLUDE_DIRS}
  ${Protobuf_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
  ${TensorFlow_INCLUDE_DIRS}
  ${CMAKE_CURRENT_BINARY_DIR}
)

link_directories(
  ${Boost_LIBRARY_DIRS}
)

# Build the proto.
protobuf_generate_cpp(PROTO_SRC PROTO_HEADER "flowthrone/proto/flowthrone.proto")
add_library(flowthrone_proto STATIC ${PROTO_SRC} ${PROTO_HEADER})
target_link_libraries(flowthrone_proto ${PROTOBUF_LIBRARY})

###############################################################################
##   _       _____  ____   _____             _____   _____  ______   _____   ##
##  | |     |_   _||  _ \ |  __ \     /\    |  __ \ |_   _||  ____| / ____|  ##
##  | |       | |  | |_) || |__) |   /  \   | |__) |  | |  | |__   | (___    ##
##  | |       | |  |  _ < |  _  /   / /\ \  |  _  /   | |  |  __|   \___ \   ##
##  | |____  _| |_ | |_) || | \ \  / ____ \ | | \ \  _| |_ | |____  ____) |  ##
##  |______||_____||____/ |_|  \_\/_/    \_\|_|  \_\|_____||______||_____/   ##
##                                                                           ##
###############################################################################
# This is the main library that the binaries should be link.
add_library(flowthrone STATIC
  flowthrone/cpp/optical_flow_model.h
  flowthrone/cpp/optical_flow_model.cpp
  flowthrone/cpp/optical_flow_tf_model.cpp
  flowthrone/cpp/optical_flow_tf_model.h
  flowthrone/cpp/io.cpp
  flowthrone/cpp/io.h
  flowthrone/cpp/visualization.cpp
  flowthrone/cpp/visualization.h
  flowthrone/cpp/utils.cpp
  flowthrone/cpp/utils.h
  flowthrone/cpp/tf_utils.cpp
  flowthrone/cpp/tf_utils.h
  flowthrone/cpp/signal_handling.cpp
  flowthrone/cpp/signal_handling.h
)

target_link_libraries(flowthrone
  flowthrone_proto
  ${TensorFlow_LIBRARIES}
  ${GLOG_LIBRARIES}
  ${OpenCV_LIBS}
)

# Library for evaluation/inspection. If you are only interested in running
# optical flow, you do not need this.
add_library(evaluation STATIC
  flowthrone/cpp/evaluation.cpp
  flowthrone/cpp/evaluation.h
)
target_link_libraries(evaluation
  flowthrone_proto
  ${GLOG_LIBRARIES}
  ${OpenCV_LIBS}
)

# Library that should be linked only by tests.
add_library(test_utils STATIC
  flowthrone/cpp/test_utils.cpp
  flowthrone/cpp/test_utils.h
)
target_link_libraries(test_utils
  ${GLOG_LIBRARIES}
  ${OpenCV_LIBS}
)

###############################################################################
##        ____  _____  _   _            _____   _____  ______   _____        ##
##       |  _ \|_   _|| \ | |    /\    |  __ \ |_   _||  ____| / ____|       ##
##       | |_) | | |  |  \| |   /  \   | |__) |  | |  | |__   | (___         ##
##       |  _ <  | |  | . ` |  / /\ \  |  _  /   | |  |  __|   \___ \        ##
##       | |_) |_| |_ | |\  | / ____ \ | | \ \  _| |_ | |____  ____) |       ##
##       |____/|_____||_| \_|/_/    \_\|_|  \_\|_____||______||_____/        ##
##                                                                           ##
###############################################################################
# Tool for running optical flow on a pair of images, or on a video.
add_executable(optical_flow_tool flowthrone/cpp/optical_flow_tool.cpp)
target_link_libraries(optical_flow_tool
  flowthrone
  ${GLOG_LIBRARIES}
  ${GFLAGS_LIBRARIES}
  ${OpenCV_LIBS}
)

# Binary for evaluation.
add_executable(evaluation_tool flowthrone/cpp/evaluation_tool.cpp)
target_link_libraries(evaluation_tool
  flowthrone
  evaluation
  ${Boost_LIBRARIES}
  ${GLOG_LIBRARIES}
  ${GFLAGS_LIBRARIES}
  ${OpenCV_LIBS}
)

###############################################################################
##                _______   ______    _____   _______    ____                ##
##               |__   __| |  ____|  / ____| |__   __|  / ____|              ##
##                  | |    | |__    | (___      | |    | (___                ##
##                  | |    |  __|    \___ \     | |     \___ \               ##
##                  | |    | |____   ____) |    | |     ____) |              ##
##                  |_|    |______| |_____/     |_|    |_____/               ##
##                                                                           ##
###############################################################################
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

add_executable(evaluation_test flowthrone/cpp/evaluation_test.cpp)
target_link_libraries(evaluation_test
  evaluation
  test_utils
  ${GTEST_BOTH_LIBRARIES}
  ${GFLAGS_LIBRARIES}
  ${OpenCV_LIBS}
)

add_executable(utils_test flowthrone/cpp/utils_test.cpp)
target_link_libraries(utils_test
  flowthrone
  ${GTEST_BOTH_LIBRARIES}
  ${GFLAGS_LIBRARIES}
  ${OpenCV_LIBS}
)

add_executable(tf_utils_test flowthrone/cpp/tf_utils_test.cpp)
target_link_libraries(tf_utils_test
  flowthrone
  test_utils
  ${GTEST_BOTH_LIBRARIES}
  ${GFLAGS_LIBRARIES}
)

# List of tests.
enable_testing()
add_test(io_test io_test)
add_test(visualization_test visualization_test)
add_test(evaluation_test evaluation_test)
add_test(utils_test utils_test)
add_test(tf_utils_tets tf_utils_test)
