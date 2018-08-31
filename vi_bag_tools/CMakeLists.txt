cmake_minimum_required(VERSION 2.8.3)
project(vi_bag_tools)

find_package(catkin_simple REQUIRED)

catkin_simple()

cs_install()

cs_install_scripts(python/bagextractor_asl_format)

cs_export()

catkin_python_setup()
