import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import can
import math

class DriveToCanNode(Node):
    def __init__(self):
        super().__init__('drive_to_can')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.callback,
            10
        )


    def callback(self, msg):
        global east
        global west
        global eastnorth
        global westnorth
        global north
        global oriental
        global speed
        oriental=1499;speed=1499
        west=0; eastnorth=0; westnorth=0; north=0; east=0
        angle_start = msg.angle_min
        angle_end = msg.angle_max
        angle_step = msg.angle_increment
        range_min = msg.range_min
        range_max = msg.range_max
        ranges = list(msg.ranges)

        east_index = int(0.78 / angle_step)
        west_index = int(3.92 / angle_step)
        eastnorth_index = int(1.9 / angle_step)
        westnorth_index = int(2.8 / angle_step)
        north_index = int(angle_start / angle_step)

        east = min(ranges[east_index-10:east_index+10])
        west = min(ranges[west_index-10:west_index+10])
        eastnorth = min(ranges[eastnorth_index-50:eastnorth_index+10])
        north = min(ranges[north_index-10:north_index+10])
        westnorth = min(ranges[westnorth_index-50:westnorth_index+10])

        dic = {'east':east,
               'west':west,
               'eastnorth':eastnorth,
               'north':north,
               'westnorth':westnorth}
        if dic['north'] < 0.2:
                speed = 1499
                oriental = 1469
        elif dic['east'] < 0.5 or dic['eastnorth'] < 0.5:
                print(3)
                speed = 1700
                oriental = 1499 - 750
        elif dic['west'] < 0.5 or dic['westnorth'] < 0.5:
                print(3)
                speed = 1700
                oriental = 1499 + 750
        elif dic['east'] < 0.7 or dic['eastnorth'] < 0.7:
            	print(3)
            	speed = 1700
            	oriental = 1499 - 750
        elif dic['west'] < 0.7 or dic['westnorth'] < 0.7:
            	print(3)
            	speed = 1700
            	oriental = 1499 + 750
        elif dic['north'] <= 0.9 and dic['north'] >= 0.2:
            	print(7)
            	speed = 1700
            	oriental = 1499 - 750
        else:
            	speed = 1900
            	oriental = 1469


        a, b = self.transfer(speed)
        c, d = self.transfer(oriental)


        # Candlelight firmware on Linux
        bus = can.interface.Bus(interface='socketcan', channel='can0', bitrate=1000000)

	# Stock slcan firmware on Linux
		# bus = can.interface.Bus(interface='slcan', channel='/dev/ttyACM0', bitrate=1000000)
        try:
                msg = can.Message(arbitration_id=0x112, data=[c, d, a, b, 0, 0, 0, 0],
		                  is_extended_id=False)
        except can.CanError:
                self.get_logger().info("Message NOT sent")

        try:
            bus.send(msg)
            print("Message sent on {}".format(bus.channel_info))
        except can.CanError:
            print("Message NOT sent")


    def transfer(self, value):
        b = hex(value)
        end_part = b[len(b) - 2:len(b)]
        front_part = b[:len(b) - 2]
        front_part = front_part.replace('0x', '')
        end_part = int(end_part, 16)
        front_part = int(front_part, 16)

        return front_part, end_part

def main(args=None):
    rclpy.init(args=args)
    node = DriveToCanNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
