from setuptools import find_packages, setup

package_name = 'my_robo_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zaid',
    maintainer_email='zaid@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = my_robo_controller.my_first_node:zaid",
            "draw_circle = my_robo_controller.draw_circle:main",
            "pose_subs = my_robo_controller.pose_subscriber:main",
            "turtle_loop = my_robo_controller.turtlesim_loop:main",
            "draw_square = my_robo_controller.draw_square:main"
        ],
    },
)
