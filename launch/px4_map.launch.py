import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    param_file = os.path.join(
        get_package_share_directory('px4_pose'),
        'params',
        'drone_pose.yaml'
    )
    with open(param_file, 'r') as file:
        params = yaml.safe_load(file)

    use_sim_time_param = {'use_sim_time': True}
    iris_description_dir = get_package_share_directory('iris_description')
    urdf_file = os.path.join(iris_description_dir, 'urdf', 'iris.urdf')
    rviz_config_path = os.path.join(get_package_share_directory('px4_map_app'), 'rviz', 'iris_map.rviz')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open(urdf_file, 'r').read()}]
    	),
        Node(
            package='px4_pose',
            executable='px4_tf_pub',
            name='px4_pose_node',
            output='screen',
            parameters=[params, use_sim_time_param],
        ),
        Node(
            package='pointcloud_to_laserscan',
            executable='laserscan_to_pointcloud_node',
            name='laserscan_to_pointcloud',
            remappings=[('scan_in', '/laser/scan'),  
                        ('cloud', '/cloud')],       
            parameters=[{'target_frame': 'rplidar_link', 'transform_tolerance': 0.01}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path]
    	)
    ])
