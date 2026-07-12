#！/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node): # MODIFY NAME
    def __init__(self):
        self.counter_ = 0
        super().__init__("robot_news_station") # MODIFY NAME
        self.get_logger().info("This is my first publisher")
        self.robot_name_ = "C3PO"
        self.publisher_ = self.create_publisher(String, "robot_news", 10) # topic = "robot_news"
        self.timer_ = self.create_timer(1.0, self.publish_news) # callback fun = publish_news
        self.get_logger().info("Robot news station has been started.")

    def publish_news(self): # is called every 1.0 second
        self.counter_ += 1
        # step1. message type
        msg = String() 
        # step2. message content
        msg.data = f"Hi, this is {self.robot_name_} from the robot news station ({self.counter_}s)"
        # step3. message published
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.try_shutdown()


if __name__ == "__main__":
    main()

# 1. run "ros2 run L01_first_publisher robot_news_station" to start the node:"robot_news_station"
# 2. run "ros2 topic echo /robot_news" to check content published in topic:"robot_news"
# option: check node/topic: ros2 node list / ros2 topic list