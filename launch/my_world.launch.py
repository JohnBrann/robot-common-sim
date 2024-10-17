import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Get paths to packages and files
    gazebo_worlds_dir = get_package_share_directory('gazebo_worlds')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # World file path
    world_path = os.path.join(gazebo_worlds_dir, 'worlds', 'world1.world')

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
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)

    return ld
