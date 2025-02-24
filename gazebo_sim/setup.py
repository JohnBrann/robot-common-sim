from setuptools import find_packages, setup
import glob

package_name = 'gazebo_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob('launch/*.launch.py')),
        ('share/' + package_name + '/worlds', glob.glob('worlds/*.world')), 
        ('share/' + package_name + '/models/waypoint_marker', glob.glob('models/waypoint_marker/*.sdf')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='csrobot',
    maintainer_email='john.brann4315@gmail.com',
    description='Package for custom Gazebo worlds',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
