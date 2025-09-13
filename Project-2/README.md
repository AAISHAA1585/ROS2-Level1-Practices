# Project 2: Sensor Alert System

## Overview
The **Sensor Alert System** is a simple ROS2 project that simulates sensor readings (like temperature or humidity) and raises alerts when values cross predefined thresholds.  
It is the second project in the Level-1 Practice Repository, designed to help beginners understand **publishers, subscribers, and basic alert logic** in ROS2.

---

## Package Structure<bra>

sensor_alert/<bra>
│── package.xml # Package metadata (name, version, dependencies)<bra>
│── setup.py # Installation and entry points for executables<bra>
│── sensor_alert/ # Python source code (nodes)<bra>
│ ├── publisher.py # Publishes sensor values<bra>
│ └── subscriber.py # Subscribes and checks thresholds<bra>



---

# What you need to have<bra>
Before running this project, make sure you have:<bra>  
- ROS2 (Humble or later) installed  <bra>
- A working ROS2 workspace (`ros2_ws`)  <bra>
- Colcon build system  
<bra>
---

## How to Run<bra>

1️] Navigate to your workspace:<bra>
    cd ~/ros2_ws<bra>

2]Build the package:<bra>
  colcon build --packages-select sensor_alert<bra>

3]Source the workspace:<bra>
   source install/setup.bash<bra>

4]Run the Publisher Node:<bra>
  ros2 run sensor_alert sensor_pub<bra>

5]Run the Subscriber Node (in a new terminal):<bra>
 ros2 run sensor_alert sensor_pub<bra>


What I Learn<bra>

How a ROS2 package is structured (package.xml, setup.py, src)<bra>
How to create publishers and subscribers in ROS2<bra>
How to simulate sensor data and implement threshold-based alerts<bra>
How to use ROS2 CLI commands to inspect topics and messages<bra>
