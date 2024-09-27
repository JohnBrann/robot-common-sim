import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    # Path to the Gazebo world file
    world_path = os.path.join(get_package_share_directory('gazebo_worlds'), 'worlds', 'base_world.world')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_path],
            output='screen'
        ),
    ])
