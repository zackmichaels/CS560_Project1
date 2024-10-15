## How to launch Webots Environment using ROS2
	1.	Navigate to the folder containing the simulation.sh file (CS560_Project1)
	2.	Enter ./simulation.sh
	
### Or
		1. Navigate to CS560_Project1 folder and enter the following:
			source /opt/ros/humble/setup.bash
			export WEBOTS_HOME=/mnt/c/Program\ Files/Webots
			colcon build
			source install/setup.bash
			ros2 launch zackmichaels_proj_1 zackmichaels_proj_1_launch.py

## How to manipulate doors and lighting
### Doors
1. First start the Webots application
2. Click on the door you want opened
3. TO OPEN: Go to the doors position property and set its value to -1.50
4. TO CLOSE: Go to the doors position property and set its value to 0
### Lighting
1. First start the Webots application
2. Click on the ceiling light you want to be adjusted
3. Set the pointLightIntensity value to 0 for the light to be off or a positive value for it to be turned on, with increasing numbers increasing the brightness of the light
		
