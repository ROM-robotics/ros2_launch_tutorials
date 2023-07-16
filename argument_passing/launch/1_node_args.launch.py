from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node",
        condition=IfCondition(LaunchConfiguration('open_turtlesim'))
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('open_turtlesim', default_value='false', description='Open turtlesim or Not.'),
        turtlesim_node,
    ])