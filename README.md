# Table-Position-Publisher-ROS

## Overview

The **Table-Position-Publisher-ROS** application is a ROS2-based project designed to publish table positions and orientations to the ROS environment, enabling robots to navigate to these predefined locations using the Nav2 stack. Through a user-friendly graphical interface built with Tkinter, the application allows users to easily define, manage, and remove table positions. Once a position is set, the application publishes the data to a ROS2 topic, which is then utilized by the robot to move to the specified location. 

## Features
- Add tables with user-defined positions and orientations.
- Publish table positions and orientations to a ROS2 topic.
- Graphical user interface for easy management.
- Toggle remove mode for deleting tables.

## System Requirements
- **Host System:** Windows 11
- **Development Environment:** Ubuntu 22.04.4 LTS running via WSL (Windows Subsystem for Linux)
- **ROS2 Distribution:** Humble
- **Simulation Tools:** 
  - Gazebo for simulation
  - RViz for visualization

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/HalaGholeh/TableManager-Tkinter-ROS.git
   cd TableManager-Tkinter-ROS
