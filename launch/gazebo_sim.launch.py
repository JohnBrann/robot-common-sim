import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    # Get paths to packages and files
    pkg_robot_common_sim = get_package_share_directory('robot-common-sim')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # Declare the launch argument for the world name
    world_arg = DeclareLaunchArgument(
        'world', default_value='4x4m_empty.world',
        description='Name of the Gazebo world to load'
    )

    # Path to the worlds directory
    world_dir = os.path.join(pkg_robot_common_sim, 'worlds')

    # Gazebo server
    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': [world_dir + '/', LaunchConfiguration('world')]}.items()
    )

    # Gazebo client
    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        ),
        launch_arguments={'world': [world_dir + '/', LaunchConfiguration('world')]}.items()
    )

    # Create the launch description and add actions
    ld = LaunchDescription()
    ld.add_action(world_arg) 
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)

    return ld
