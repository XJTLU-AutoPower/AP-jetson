#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped

class PoseTransformer(Node):
	def __init__(self):
		super().__init__('pose_converter')
		self.subscription = self.create_subscription(
		PoseWithCovarianceStamped,
		'amcl_pose',
		self.pose_callback,
		10)
		self.publisher_ = self.create_publisher(PoseStamped, '/pf/viz/inferred_pose', 			10)

	def pose_callback(self, msg):
		pose_stamped = PoseStamped()
		pose_stamped.header = msg.header
		pose_stamped.pose = msg.pose.pose
		self.publisher_.publish(pose_stamped)
		self.get_logger().info('Publishing: "%s"' % pose_stamped)

def main(args=None):
	rclpy.init(args=args)
	pose_transformer = PoseTransformer()
	rclpy.spin(pose_transformer)
	
	pose_converter.destroy_node()	
	rclpy.shutdown()

if __name__ == '__main__':
	main()
