#！/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("robot_news_station") # MODIFY NAME
        self.get_logger().info("This is my first publisher")
        self.publisher_ = self.create_publisher(String, "robot_news", 10)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.try_shutdown()


if __name__ == "__main__":
    main()
