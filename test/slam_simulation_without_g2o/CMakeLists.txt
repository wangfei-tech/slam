CMAKE_MINIMUM_REQUIRED( VERSION 3.21.1 )

ADD_DEFINITIONS( -std=c++14 )

SET( EXECUTABLE_OUTPUT_PATH "${PROJECT_BINARY_DIR}/bin" )

#find required eigen
FIND_PACKAGE( Eigen3 )

#directory of eigen headers
INCLUDE_DIRECTORIES( ${EIGEN3_INCLUDE_DIR} )

#find required opencv
FIND_PACKAGE( OpenCV REQUIRED )

#directory of opencv headers
INCLUDE_DIRECTORIES(${OpenCV_INCLUDE_DIRS})

SET( EXECUTABLE_OUTPUT_PATH "${PROJECT_BINARY_DIR}/bin" )
MESSAGE( STATUS "executable files path: " ${PROJECT_BINARY_DIR}/bin )
AUX_SOURCE_DIRECTORY( ${PROJECT_SOURCE_DIR}/slam_simulation_without_g2o/ test_src )

INCLUDE_DIRECTORIES( "${PROJECT_SOURCE_DIR}/../include" )

LINK_DIRECTORIES( "${PROJECT_SOURCE_DIR}/../build/lib/" )

#directory of opencv link libs
LINK_DIRECTORIES(${OpenCV_LIBRARY_DIRS})

ADD_EXECUTABLE( slamSimulationWithoutG2O ${test_src} )

TARGET_LINK_LIBRARIES( slamSimulationWithoutG2O slam.a )

TARGET_LINK_LIBRARIES( slamSimulationWithoutG2O ${OpenCV_LIBS} )
