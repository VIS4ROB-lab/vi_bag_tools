cmake_minimum_required(VERSION 2.8.3)
project(aslam_cv_python)

find_package(catkin_simple REQUIRED)
catkin_simple()

add_definitions( -fPIC -Wextra -Winit-self -Woverloaded-virtual -Wnon-virtual-dtor -Wsign-promo -Wno-long-long -std=c++0x)

if(APPLE)
  add_definitions( -ftemplate-depth-1024)
endif()

add_python_export_library(${PROJECT_NAME} python/aslam_cv
  src/module.cpp
  src/Time.cpp
)

find_package(Boost REQUIRED COMPONENTS serialization) 
target_link_libraries(${PROJECT_NAME} ${Boost_LIBRARIES})
cs_install()
cs_export()
