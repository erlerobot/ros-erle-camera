cmake_minimum_required(VERSION 2.8.3)
project(ros_erle_camera)
include(FindPkgConfig)
## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
    roscpp
    image_transport
)

find_package(OpenCV REQUIRED)

catkin_package()

include_directories(include ${catkin_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS} )

add_executable(usb_cam src/camera_opencv.cpp)
target_link_libraries(usb_cam ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
add_dependencies(usb_cam beginner_camera)

install(
	TARGETS usb_cam
	ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
	LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
	RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
