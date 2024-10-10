from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([
		Node(
		package='nav2_bringup',
		executable='bringup_launch.py',
		name='bringup',
		output='screen',
		parameters=[
		'src/amcl_params.yaml',
		{'use_sim_time': False}
		]),
		
		Node(
		package='nav2_amcl',
		executable='amcl',
		name='amcl',
		output='screen',
	parameters=['src/amcl_params.yaml'],
	remappings=[
		('/scan', '/scan'),
		('/map', '/map'),
		]),

		Node(
		package='pose_transformer',
		executable='pose_converter_node',
		name='pose_converter',
		output='screen'
		)])
