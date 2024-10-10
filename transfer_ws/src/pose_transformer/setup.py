#!/usr/bin/env python3

from setuptools import setup

package_name = 'pose_transformer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ZiyeZhang',
    maintainer_email='ziyezhang@xjtlu.cn',
    description='',
    license='1',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pose_transformer_node = pose_transformer.pose_transformer_node:main',
        ],
    },
)
