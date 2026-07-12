# First time to pull the project:
'''
mkdir -p ~/Desktop/ROS2_WS
cd ~/Desktop/ROS2_WS
git clone https://github.com/renfei-Zhou/ROS2.git src
colcon build
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
echo "source ~/Desktop/ROS2_WS/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
'''

# Important parameter name and dir
'''
PACKAGE_NAME     包名          pkg create 的参数；ros2 run 第一个参数
FILE_NAME        文件名        模块文件 FILE_NAME.py
EXEC_NAME        可执行名      entry_points 等号左边；ros2 run 第二个参数
NODE_NAME        ROS节点名     代码里 super().__init__("NODE_NAME")
NODE_CLASS_NAME  Python类名   代码里 class NODE_CLASS_NAME(Node)

make sure in setup.py: 'EXEC_NAME = PACKAGE_NAME.FILE_NAME:main'
'''


# Step1. Create a new package
'''
dir cd = src
ros2 pkg create PACKAGE_NAME --build-type ament_python --dependencies rclpy --node-name FILE_NAME
'''

# Step2. Template for FILE_NAME
'''
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class NODE_CLASS_NAME(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("NODE_NAME") # MODIFY NAME
        self.get_logger().info("This is a template")


def main(args=None):
    rclpy.init(args=args)
    node = NODE_CLASS_NAME() # MODIFY NAME
    rclpy.spin(node)
    rclpy.try_shutdown()


if __name__ == "__main__":
    main()
'''

# (option) Add a new node.py
'''
1. create NEW_FILE.py under the same dir as FILE_NAME.py
2. finish writing NEW_FILE.py e.g. in template
'''

# Step3. Run a node in terminal
'''
in setup.py make sure entry_points in form:
'EXEC_NAME = PACKAGE_NAME.FILE_NAME:main'
'NEW_EXEC_NAME = PACKAGE_NAME.NEW_FILE:main'


dir cd = WS 
colcon build    # option:删除不需要的候选列表 rm -rf build install log && colcon build
source install/setup.bash    # ← 新建包/新建工作空间后必须；已有包改代码则可省
ros2 run PACKAGE_NAME EXEC_NAME   # EXEC_NAME = setup.py 入口点等号左边那个名字
'''

# 