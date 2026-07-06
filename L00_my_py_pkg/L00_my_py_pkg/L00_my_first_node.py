#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import time

class MyNode(Node):

    def __init__(self):
        # give a new variable for self, which means self can use everything from Node AND a new variable: count
        self.counter_ = 5

        super().__init__("py_test")
        self.get_logger().info("Hello world")
        self.timer_ = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(f"Counting down {self.counter_}")
        self.counter_ -= 1

        if self.counter_ <= 0: # counter=0 -> exit
            self.timer_.cancel()
            time.sleep(0.5)
            rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    
    # node = Node("py_test")
    # node.get_logger().info("Hello world")
    node = MyNode()
    
    rclpy.spin(node)

    rclpy.try_shutdown()

if __name__ == "__main__":
    main()