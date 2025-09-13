from setuptools import find_packages, setup

package_name = 'servo_visualizer'

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
    maintainer='aishwarya',
    maintainer_email='aishwaryasuryawanshi2021@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'servo_pub = servo_visualizer.servo_publisher:main',
        'servo_sub = servo_visualizer.servo_subscriber:main',
    ],
},

)
