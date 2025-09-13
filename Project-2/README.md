# Project 2: Sensor Alert System

## Overview
The **Sensor Alert System** is a simple ROS2 project that simulates sensor readings (like temperature or humidity) and raises alerts when values cross predefined thresholds.  
It is the second project in the Level-1 Practice Repository, designed to help beginners understand **publishers, subscribers, and basic alert logic** in ROS2.

---

## Package Structure<br>

sensor_alert/<bra>
│── package.xml # Package metadata (name, version, dependencies)<br>
│── setup.py # Installation and entry points for executables<br>
│── sensor_alert/ # Python source code (nodes)<br>
│ ├── publisher.py # Publishes sensor values<br>
│ └── subscriber.py # Subscribes and checks thresholds<br>



---

# What you need to have<br>
Before running this project, make sure you have:<br> 
- ROS2 (Humble or later) installed  <br>
- A working ROS2 workspace (`ros2_ws`)  <br>
- Colcon build system  <br>
---

## How to Run<br>

1️] Navigate to your workspace:<br>
    cd ~/ros2_ws<br>

2]Build the package:<br>
  colcon build --packages-select sensor_alert<br>

3]Source the workspace:<br>
   source install/setup.bash<br>

4]Run the Publisher Node:<br>
  ros2 run sensor_alert sensor_pub<br>

5]Run the Subscriber Node (in a new terminal):<br>
 ros2 run sensor_alert sensor_pub<br>


What I Learn<br>

How a ROS2 package is structured (package.xml, setup.py, src)<br>
How to create publishers and subscribers in ROS2<br>
How to simulate sensor data and implement threshold-based alerts<br>
How to use ROS2 CLI commands to inspect topics and messages<br>
