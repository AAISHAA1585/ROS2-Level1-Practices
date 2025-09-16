    def draw_hexagon(self):
        twist = Twist()
        side_length = 2.0     # distance forward per side
        speed = 1.0           # linear speed
        turn_angle = math.radians(60)  # 60° for hexagon
        turn_speed = 1.0      # angular speed

        while rclpy.ok():  # keep looping until stopped
            for i in range(6):
                # Move forward
                twist.linear.x = speed
                twist.angular.z = 0.0
                self.publisher_.publish(twist)
                time.sleep(side_length / speed)

                # Stop briefly
                twist.linear.x = 0.0
                self.publisher_.publish(twist)
                time.sleep(0.5)

                # Turn 60 degrees
                twist.angular.z = turn_speed
                self.publisher_.publish(twist)
                time.sleep(turn_angle / turn_speed)

                # Stop briefly
                twist.angular.z = 0.0
                self.publisher_.publish(twist)
                time.sleep(0.5)

            self.get_logger().info("One hexagon complete, starting again...")

