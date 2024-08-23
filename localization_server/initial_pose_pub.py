import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped, PointStamped

# PoseWithCovarianceStamped
# -------------------------
# user:~$ ros2 interface show geometry_msgs/msg/PoseWithCovarianceStamped
# # This expresses an estimated pose with a reference coordinate frame and timestamp

# std_msgs/Header header
#         builtin_interfaces/Time stamp
#                 int32 sec
#                 uint32 nanosec
#         string frame_id
# PoseWithCovariance pose
#         Pose pose
#                 Point position
#                         float64 x
#                         float64 y
#                         float64 z
#                 Quaternion orientation
#                         float64 x 0
#                         float64 y 0
#                         float64 z 0
#                         float64 w 1
#         float64[36] covariance

# PointStamped
# ------------
# user:~$ ros2 interface show geometry_msgs/msg/PointStamped
# # This represents a Point with reference coordinate frame and timestamp

# std_msgs/Header header
#         builtin_interfaces/Time stamp
#                 int32 sec
#                 uint32 nanosec
#         string frame_id
# Point point
#         float64 x
#         float64 y
#         float64 z

class InitialPosePublisher(Node):
    def __init__(self):
        super().__init__("initial_pose_pub")
        self.publisher = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)
        self.subscription = self.create_subscription(PointStamped, '/clicked_point', self.init_pose_cb, 10)
        self.subscription # prevent unused var warning

    def init_pose_cb(self, msg):
        self.get_logger().info('Heard on /clicked_point: "%s"' % msg)
        initial = PoseWithCovarianceStamped()
        initial.header.stamp = msg.header.stamp
        # initial.header.stamp.secs = msg.header.stamp.secs
        # initial.header.stamp.nanosec = msg.header.stamp.nanosec
        initial.header.frame_id = msg.header.frame_id
        initial.pose.pose.position.x = msg.point.x
        initial.pose.pose.position.y = msg.point.y
        initial.pose.pose.orientation.w = 1.0
        self.get_logger().info('Publishing to /initialpose: "%s"' % initial)
        self.publisher.publish(initial)
        
def main(args=None):
    rclpy.init(args=args)
    node = InitialPosePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
