import os
from glob import glob
from setuptools import setup

package_name = 'px4_map_app'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Alfredo',
    maintainer_email='amamanisai@unsa.edu.pe',
    description='Provides a 3D mapping application for PX4 drones',
    license='GPL-3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
