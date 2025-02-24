import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Get paths to packages and files
    pkg_gazebo_sim = get_package_share_directory('gazebo_sim')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # Declare the launch argument for the world name
    world_arg = DeclareLaunchArgument(
        'world', default_value='4x4m_empty.world',
        description='Name of the Gazebo world to load'
    )

    # Path to the worlds directory
    world_dir = os.path.join(pkg_gazebo_sim, 'worlds')

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

    # Path to the SDF model
    model_path = os.path.expanduser("~/ros2_nav_ws/src/robot-common-sim/gazebo_sim/models/waypoint_marker/model.sdf")

    # Read the SDF file as a string
    if os.path.exists(model_path):
        with open(model_path, "r") as sdf_file:
            sdf_content = sdf_file.read()
    else:
        raise FileNotFoundError(f"Model SDF file not found: {model_path}")

    # Spawn the waypoint marker in Gazebo
    spawn_marker_cmd = ExecuteProcess(
        cmd=[
            "ros2", "service", "call", "/spawn_entity", "gazebo_msgs/srv/SpawnEntity",
            f"{{name: 'waypoint_marker', xml: '{sdf_content}', initial_pose: {{position: {{x: 1.0, y: 2.0, z: 0.0}}}}}}"
        ],
        output="screen"
    )

    # Create the launch description and add actions
    ld = LaunchDescription()
    ld.add_action(world_arg) 
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)
    ld.add_action(spawn_marker_cmd)  

    return ld
