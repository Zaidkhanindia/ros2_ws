#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class DrawRectangleNode(Node):

    def __init__(self):
        super().__init__("draw_rectangle")
        self.get_logger().info("code executed")

        self.rectangle_pub = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10
        )
        
        self.rectangle_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self.rectangle_callback, 10
        )
    
    def rectangle_callback(self, pose: Pose):
        self.get_logger().info("[ " + str(pose.x) + " ], " + "[ " + str(pose.y) + " ]")
        vel = Twist()
        vel.linear.x = 2.0
        vel.angular.z = 0.0
        self.rectangle_pub.publish(vel)
        if pose.x == 8.0:
            vel.angular.z = 1.0
            vel.linear.x = 0.0
            self.rectangle_pub.publish(vel)



def main(args=None):
    rclpy.init(args=args)
    node = DrawRectangleNode()
    rclpy.spin(node)
    rclpy.shutdown()