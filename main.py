from tkinter import *
from frames import setupFrames
from functions import allFunctions
from icons import addIcon, removeIcon
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

# ROS2 Node
class TablePublisher(Node):
    def __init__(self):
        super().__init__('table_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, '/goal_pose', 10)

    def publish_position(self, x, y, z=0.0, z_orient=0.0, w_orient=1.0):
        pose = PoseStamped()
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.header.frame_id = "map"
        pose.pose.position.x = float(x)
        pose.pose.position.y = float(y)
        pose.pose.position.z = float(z)
        pose.pose.orientation.z = float(z_orient)
        pose.pose.orientation.w = float(w_orient)
        self.publisher_.publish(pose)
        self.get_logger().info(f"Published position: x={x}, y={y}, z={z}, orientation: z={z_orient}, w={w_orient}")

# ROS2 initialization
rclpy.init()

# Initialize ROS2 node
ros_node = TablePublisher()

# Main view
myView = Tk()
myView.title("Restaurant")
myView.attributes("-fullscreen", True)

# Button and table frames
buttonFrame, tableFrame = setupFrames(myView)

# Call icons
add = addIcon()
remove = removeIcon()

# Call allFunctions to set up buttons and functions
allFunctions(myView, buttonFrame, tableFrame, add, remove, ros_node)

# Bind the Escape key to exit fullscreen
myView.bind("<Escape>", lambda event: myView.attributes("-fullscreen", False))

# Start ROS2 spinning in a separate thread
import threading
ros_thread = threading.Thread(target=rclpy.spin, args=(ros_node,))
ros_thread.start()

myView.mainloop()

# Shutdown ROS2 when the application exits
rclpy.shutdown()
ros_thread.join()

