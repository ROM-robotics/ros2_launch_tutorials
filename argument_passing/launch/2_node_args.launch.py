#!/usr/bin/env python3
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    use_turtlesim = LaunchConfiguration('open_turtlesim')

    my_turtle = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('argument_passing'), 'launch', '1_node_args.launch.py')]),
        launch_arguments={
            'open_turtlesim': use_turtlesim
        }.items()
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('open_turtlesim', default_value='false',description='Run turtlesim or Not'),
        my_turtle,
    ])