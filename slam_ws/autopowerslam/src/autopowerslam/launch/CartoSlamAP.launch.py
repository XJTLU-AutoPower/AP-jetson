from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, SetRemap
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():

## ***** Launch arguments *****
# 是否使用仿真时间，真实的机器人我们不需要，设置为False
	use_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value = 'False')

## ***** File paths ******
# 找到cartographer功能包的地址
	pkg_share = FindPackageShare('cartographer_ros').find('cartographer_ros')
## ***** Nodes *****
#=====================声明三个节点，cartographer/occupancy_grid_node/rviz_node=================================
	cartographer_node = Node(
	package = 'cartographer_ros',
	executable = 'cartographer_node',
	parameters = [{'use_sim_time': LaunchConfiguration('use_sim_time')}],
	arguments = [
		      '-configuration_directory', 				  FindPackageShare('cartographer_ros').find('cartographer_ros') + '/configuration_files',
		'-configuration_basename', '/AutoPower_2d.lua'],
	remappings = [
			('scan', 'scan')],
	output = 'screen'
	)

# 可视化节点
	rviz_node = Node(
	package='rviz2',
	namespace='rviz2',
	executable='rviz2',
	name='rviz2',
	output='screen')

	cartographer_occupancy_grid_node = Node(
	package = 'cartographer_ros',
	executable = 'cartographer_occupancy_grid_node',
	parameters = [
	{'use_sim_time': False},
	{'resolution': 0.05}],
	)

	return LaunchDescription([
	use_sim_time_arg,
	# Nodes
	rviz_node ,
	cartographer_node,
	cartographer_occupancy_grid_node,
	])
