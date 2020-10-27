vi_bag_tools
=================
Software for extracting imu measurements and images from bagfile. It is a extract from Kalibr (https://github.com/ethz-asl/kalibr) with small modifications on the output format and to eliminate dependences. It also supports semantic maps.

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
  $ git clone git@github.com:catkin/catkin_simple
  $ git clone git@github.com:ethz-asl/eigen_catkin
  
  # If you don't need Schweizer-Messer package you can donwload only then numpy_eigen package and catkin_boost_python_buildtool
  $ git clone git@github.com:ethz-asl/catkin_boost_python_buildtool
  $ git clone git@github.com:ethz-asl/numpy_eigen.git
  OR
  $git clone git@github.com:ethz-asl/Schweizer-Messer.git
  
  #This package
  $ git clone git@github.com:VIS4ROB-lab/vi_bag_tools.git
  
  $ cd ~/catkin_ws/
  $ catkin build
  $ source devel/setup.bash
```


How to run
-------------------
examples:


``
bagextractor_asl_format --image-topics /cam0/image_raw /cam1/image_raw --imu-topics /imu0  --bag /home/lucas/data/bags/euroc/MH_05_difficult.bag --output-folder /home/lucas/data/output_dir
``

``
bagextractor_asl_format --image-topics /firefly/vrglasses_for_robots_ros/color_map --depth_map_topics /firefly/vrglasses_for_robots_ros/depth_map --semantic-topics /firefly/vrglasses_for_robots_ros/semantic_map --gt_odometry_topics /firefly/vi_sensor/ground_truth/odometry /firefly/vrglasses_for_robots_ros/camera_odometry_out --bag /media/2020-10-27-18-43-43.bag --output-folder /home/lucas/data/output_dir
``


License
-------------------
Copyright (c) 2014, Paul Furgale, Jérôme Maye and Jörn Rehder, Autonomous Systems Lab, 
                    ETH Zurich, Switzerland

Copyright (c) 2014, Thomas Schneider, Skybotix AG, Switzerland

Copyright (c) 2018-2020, Lucas Teixeira, Fabiola Maffra, Vision for Robotics Lab, 
                    ETH Zurich, Switzerland

All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this 
    list of conditions and the following disclaimer.

    Redistributions in binary form must reproduce the above copyright notice, 
    this list of conditions and the following disclaimer in the documentation 
    and/or other materials provided with the distribution.

    All advertising materials mentioning features or use of this software must 
    display the following acknowledgement: This product includes software developed 
    by the Autonomous Systems Lab and Skybotix AG.

    Neither the name of the Autonomous Systems Lab and Skybotix AG nor the names 
    of its contributors may be used to endorse or promote products derived from 
    this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTONOMOUS SYSTEMS LAB AND SKYBOTIX AG ''AS IS'' 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
IN NO EVENT SHALL the AUTONOMOUS SYSTEMS LAB OR SKYBOTIX AG BE LIABLE FOR ANY DIRECT, 
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT 
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR 
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY 
OF SUCH DAMAGE.
