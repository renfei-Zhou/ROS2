#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class NODE_CLASS_NAME(Node): # MODIFY NAME
    def __init__(self):
        self.counter1_ = 0
        self.counter2_ = 0
        super().__init__("NODE_NAME") # MODIFY NAME
        self.publisher_1_ = self.create_publisher(String, "temp_topic", 10)
        self.timer1_ = self.create_timer(0.5, self.callbackFun)
        self.timer2_ = self.create_timer(1.0, self.callbackFun2)

        self.get_logger().info("This is a template")

    def callbackFun(self):
        self.counter1_ += 1
        msg = String()
        msg.data = f"temperaly message ({self.counter1_}s)"
        self.publisher_1_.publish(msg)

    def callbackFun2(self):
        self.counter2_ += 1
        msg = String()
        msg.data = f"temperaly message from callback2 ({self.counter2_}s)"
        self.publisher_1_.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node = NODE_CLASS_NAME() # MODIFY NAME
    rclpy.spin(node)
    rclpy.try_shutdown()


if __name__ == "__main__":
    main()