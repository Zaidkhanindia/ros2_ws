# ROS2 Beginner Projects using Python and Turtlesim

This repository contains my beginner-level ROS2 projects developed using Python and the Turtlesim package.  
The purpose of this repository is to build a strong foundation in ROS2 concepts such as:

- Nodes
- Publishers
- Subscribers
- Services and Clients
- Topic Communication
- Motion Control Logic

These projects were created while learning the ROS2 workflow and understanding communication between different nodes.

---

# 🚀 Technologies Used

- ROS2
- Python
- Turtlesim
- rclpy

---

# 📂 Project Files

## 1. My First Node
**File:** `my_first_node.py`

A simple ROS2 node created using Python.  
This node prints `"Hello"` on the terminal every 1 second using a timer callback.

### Concepts Learned
- ROS2 Node Creation
- Timer Callback
- Python ROS2 Structure

---

## 2. Circle Publisher Node
**File:** `Circle_Publisher_Node.py`

A publisher node that continuously publishes linear and angular velocity commands to the turtle.

The turtle moves in a circular path by publishing velocity values on the `/turtle1/cmd_vel` topic.

### Concepts Learned
- Publisher Nodes
- Topic Communication
- Geometry Messages
- Velocity Control

---

## 3. Position Subscriber Node
**File:** `Position_Subscriber_Node.py`

A subscriber node that subscribes to the turtle position topic and continuously reads the current:

- X position
- Y position
- Orientation

### Concepts Learned
- Subscriber Nodes
- Topic Subscription
- Reading Real-Time Data

---

## 4. Loop Node with Service/Client
**File:** `Loop_Node.py`

This node combines both publishing and subscribing functionality.

The turtle continuously moves inside the screen and changes direction whenever it approaches the screen boundaries.

Additionally, a ROS2 service/client mechanism is implemented to change the turtle pen color whenever the turtle crosses the middle of the screen (`x = 5.4`).

### Features
- Autonomous turtle movement
- Boundary detection
- Direction control
- Pen color change using ROS2 service/client

### Concepts Learned
- Combining Publisher + Subscriber
- Service and Client Communication
- Decision Making Logic
- Coordinate-Based Control

---

# ▶️ How to Run

## Launch Turtlesim
```bash
ros2 run turtlesim turtlesim_node
