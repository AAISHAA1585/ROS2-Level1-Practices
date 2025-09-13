import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import matplotlib.pyplot as plt

class ServoSubscriber(Node):
    def __init__(self):
        super().__init__('servo_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'servo_angle',
            self.listener_callback,
            10)
        self.history = []

        # Setup matplotlib
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'r-', linewidth=2)
        self.ax.set_ylim(0, 180)
        self.ax.set_xlim(0, 50)
        self.ax.set_xlabel("Steps")
        self.ax.set_ylabel("Servo Angle (°)")

    def listener_callback(self, msg):
        angle = msg.data
        self.history.append(angle)
        self.history = self.history[-50:]  # keep last 50 values

        self.line.set_xdata(range(len(self.history)))
        self.line.set_ydata(self.history)
        self.ax.set_xlim(0, len(self.history))

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

        self.get_logger().info(f'Servo angle: {angle}')

def main(args=None):
    rclpy.init(args=args)
    node = ServoSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
