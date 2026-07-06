'''
mkdir -p ~/Desktop/ROS2_WS
cd ~/Desktop/ROS2_WS
git clone https://github.com/renfei-Zhou/ROS2.git src
colcon build
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
echo "source ~/Desktop/ROS2_WS/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
'''