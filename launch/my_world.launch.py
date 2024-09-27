from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Declare a launch argument for the world file
    world_arg = DeclareLaunchArgument(
        'world_name',
        default_value='empty.world',
        description='Specify the world file to load in Gazebo'
    )

    # Directory for world files
    worlds_dir = get_package_share_directory('gazebo_worlds') + '/worlds/'

    # Execute Gazebo with the dynamically specified world file
    gazebo_command = ExecuteProcess(
        cmd=['gazebo', '--verbose', LaunchConfiguration('world_name')],
        cwd=[worlds_dir],
        output='screen'
    )

    return LaunchDescription([
        # Declare the argument for the world
        world_arg,
        # Launch Gazebo with the specified world
        gazebo_command,
    ])
