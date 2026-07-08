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

# Create a new package
'''
ros2 pkg create PACKAGE_NAME --build-type ament_python --dependencies rclpy --node-name NODE_NAME
'''

# Run a node in terminal
'''
ros2 run PACKAGE_NAME NODE_NAME
'''