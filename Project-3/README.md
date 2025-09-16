## Turtle Hexagon Path Follower <br>

## Overview<br>
The Turtle Hexagon Path Follower is a ROS2 project built using the `turtlesim` simulator.<br>  
This makes the turtle draw a **hexagon shape repeatedly** until stopped externally.  <br>

It demonstrates how to:<br>
- Publish velocity commands to a simulator<br>
- Use loops and geometry to create complex motion<br>
- Automate robot path-following in ROS2<br>

This is the third project in the Level-1 Practices Repository.<br>

---

## Package Structure<br>

turtle_hexagon/<br>
│── package.xml # Package metadata (name, version, dependencies)<br>
│── setup.py # Installation and entry points<br>
│── resource/ # Resource index<br>
│── turtle_hexagon/ # Python source code (nodes)<br>
│── launch/ # (Optional) launch files<br>


---

## Requirements<br>
Before running this project, ensure you have:<br>
- ROS2 Humble (or later) installed  <br>
- A working ROS2 workspace (`ros2_ws`)  <br>
- `turtlesim` package installed:  <br>

  sudo apt install ros-humble-turtlesim<br>

How to Run<br>
1️⃣ Navigate to your workspace<br>
  cd ~/ros2_ws<br>
2️⃣ Build the package<br>
  colcon build --packages-select turtle_hexagon<br>
3️⃣ Source the workspace<br>
  source install/setup.bash<br>
4️⃣ Start turtlesim node (in a new terminal)<br>
  ros2 run turtlesim turtlesim_node<br>
5️⃣ Run the hexagon controller<br>
  ros2 run turtle_hexagon turtle_hexagon_node<br>


What I Learned<br>

-How to use publisher nodes in ROS2<br>
-How to control a robot’s motion with linear and angular velocities<br>
-Using loops and geometry to generate paths<br>
-Running multiple nodes (turtlesim_node + custom node) together<br>
-Automation of robot movement<br>


Demo:

![Turtle_hexagon](turtle.png)
![Turtle_hexagon](Screenshot 2025-09-16 170619.png)
