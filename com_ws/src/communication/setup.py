from setuptools import setup

package_name = 'communication'

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
    maintainer='WyattZhang',
    maintainer_email='Ziye.Zhang23@student.xjtlu.edu.cn',
    description=r"XJTLU-AutoPower's communication between jetson and stm32",
    license='Mozilla',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['communication_node = communication.com:main',
        ],
    },
)
