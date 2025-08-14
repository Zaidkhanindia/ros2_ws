#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtlesimLoopNode(Node):

    def __init__(self):
        super().__init__("turtle_loop")
        self.turtle_publisher = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10
        )
        self.turtle_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10)
        
    def pose_callback(self, position: Pose):
        msg = Twist()
        if (position.x or position.y) > 8.0 or (position.x or position.y) < 3.0:
            msg.angular.z = 1.3
            msg.linear.x = 1.4
        else:
            msg.linear.x = 4.0
            msg.angular.z = 0.0

        self.turtle_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtlesimLoopNode()
    rclpy.spin(node)
    rclpy.shutdown()