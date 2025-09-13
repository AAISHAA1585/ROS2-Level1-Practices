# Project 1: Servo Visualizer

Overview<br>

The Servo Visualizer is a simple ROS2 project that demonstrates how to control and visualize a servo motor using ROS2.
It is the first project in the Level-1 Practice Repository, designed to help beginners understand the structure of a ROS2 package, building with colcon, and running nodes.<br>

Package Structure
servo_visualizer/ <br>
│── package.xml        # Package metadata (name, version, dependencies)<br>
│── setup.py           # Installation and entry points for executables<br>
│── resource/          # Resource index<br>
│── srv_visualizer/    # Python source code (nodes)<br>
│── launch/            # Optional: launch files<br>


what you need to have<br>
Before running this project, make sure you have:<br>
ROS2 (Humble or later) installed <br>
A working ROS2 workspace (ros2_ws) <br>
Colcon build system <br>

1]Navigate to your workspace<br>
  cd ~/ros2_ws<br>

2]Build the package<br>
 colcon build --packages-select servo_visualizer<br>

3]Source the workspace<br>
 source install/setup.bash<br>

4]Run the node<br>
 ros2 run servo_visualizer servo_node<br>


What I learn:<br>
-How a ROS2 package is structured (package.xml, setup.py, src).<br>
-How to build packages using colcon.<br>
-How to source and run nodes in ROS2.<br>
-The first step toward controlling actuators (servos, motors) in robotics.<br>

Demo:

