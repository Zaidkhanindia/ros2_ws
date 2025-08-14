#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class DrawRectangleNode(Node):

    def __init__(self):
        super().__init__("draw_rectangle")
        self.get_logger().info("code executed")

        self.sq_pub = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10
        )

        '''self.timer_ = self.create_timer(0.5, self.draw_circ_callback)'''
        
        self.sq_sub = self.create_subscription(
            Pose, "/turtle1/pose", self.draw_circ_callback, 10
        )

    def draw_circ_callback(self, position: Pose):
        msg = Twist()
        if 9 > position.x > 5:
            msg.linear.x = 1.0
            msg.angular.z = 0.0
        if position.x == 8.0:
            msg.linear.y = 1.0
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        
        self.sq_pub.publish(msg)

        self.get_logger().info("[ " + str(position.x) + " ], [" + str(position.y) + " ]")


def main(args=None):
    rclpy.init(args=args)
    node = DrawRectangleNode()
    rclpy.spin(node)
    rclpy.shutdown()