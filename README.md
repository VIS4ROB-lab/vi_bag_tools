vi_bag_tools
=================
subset of bagfiles tools from Kalibr (https://github.com/ethz-asl/kalibr)
This package cannot be in the same catkin workspace than Kalibr

installation
-------------------
* Initialize catkin workspace:
```sh
  $ mkdir -p ~/catkin_ws/src
  $ cd ~/catkin_ws
  $ catkin config --cmake-args -DCMAKE_BUILD_TYPE=Release
  $ catkin init  # initialize your catkin workspace
```
* Get the tool set and dependencies
```sh
  $ cd ~/catkin_ws/src
  $ sudo apt-get install liblapacke-dev
  $ git clone git@github.com:catkin/catkin_simple
  $ git clone git@github.com:ethz-asl/eigen_catkin
  $ git clone git@github.com:ethz-asl/Schweizer-Messer.git
  
  $ git clone git@github.com:VIS4ROB-lab/vi_bag_tools.git
  
  $ cd ~/catkin_ws/
  $ catkin build
  $ source devel/setup.bash
```
  

How to run
-------------------
example:

``
bagextractor_asl_format --image-topics /cam0/image_raw /cam1/image_raw --imu-topics /imu0  --bag /home/lucas/data/bags/uzh/2016-06-22-17-10-05.bag --output-folder /home/lucas/data/bags/outputdir4
``
