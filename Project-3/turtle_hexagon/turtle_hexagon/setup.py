from setuptools import setup

package_name = 'project3_hexagon'

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
    maintainer='aishwarya',
    maintainer_email='aishwarya@example.com',
    description='TurtleSim hexagon drawing project',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_hexagon = turtle_hexagon.turtle_hexagon_node:main',
        ],
    },
)

