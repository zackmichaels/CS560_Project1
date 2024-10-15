#!/bin/bash
source /opt/ros/humble/setup.bash
export WEBOTS_HOME=/mnt/c/Program\ Files/Webots
colcon build
source install/setup.bash
ros2 launch zackmichaels_proj_1 zackmichaels_proj_1_launch.py
