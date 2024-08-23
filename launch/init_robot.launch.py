import launch
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        Node(
            package='localization_server',  # Replace with your package name
            executable='initial_pose_pub',  # Replace with your node's executable name
            name='initial_pose_pub',  # Optionally, give the node a name
            output='screen',  # Output logs to the screen
            # Add any additional arguments or parameters as needed
            # arguments=['--your_arg', 'value'],
            # parameters=[{'param_name': 'param_value'}],
        ),
    ])