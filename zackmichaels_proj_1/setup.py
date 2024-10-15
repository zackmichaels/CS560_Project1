from setuptools import find_packages, setup

package_name = 'zackmichaels_proj_1'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/zackmichaels_proj_1_launch.py']))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/ten_Hoor_Hall.wbt', 
]))
data_files.append(('share/' + package_name, ['package.xml']))
data_files.append(('share/' + package_name + '/resource', [
    'resource/turtlebot_webots.urdf',
    'resource/ros2control.yml',
]))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='Zachary Michaels',
    maintainer_email='zemichaels@crimson.ua.edu',
    description='Ten Hoor Hall Webot Environment',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],    
        'console_scripts': ['zackmichaels_proj_1 = zackmichaels_proj_1.zackmichaels_proj_1:main']
    },

)
