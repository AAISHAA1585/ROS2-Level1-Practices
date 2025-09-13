import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class ServoPublisher(Node):
    def __init__(self):
        super().__init__('servo_publisher')
        self.publisher_ = self.create_publisher(Int32, 'servo_angle', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # every 1 sec
        self.get_logger().info("Servo Publisher started")

    def timer_callback(self):
        angle = random.randint(0, 180)  # random angle
        msg = Int32()
        msg.data = angle
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing angle: {angle}')

def main(args=None):
    rclpy.init(args=args)
    node = ServoPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
