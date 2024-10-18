import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    # Get paths to packages and files
    robot_common_sim_dir = get_package_share_directory('robot-common-sim')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # Declare launch argument for the world name
    world_arg = DeclareLaunchArgument(
        'world_name',
        default_value=os.path.join(robot_common_sim_dir, 'worlds', 'world4.world'),
        description='Specify the world file to load in Gazebo'
    )

    # World file path from the argument
    world_path = LaunchConfiguration('world_name')

    # Launch configurations
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # Gazebo server
    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world_path}.items()
    )

    # Gazebo client
    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    # Create the launch description and add actions
    ld = LaunchDescription()
    ld.add_action(world_arg)  # Add the world argument
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)

    return ld
