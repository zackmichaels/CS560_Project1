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
## How to switch between indoor and outdoor environments
1. Navigate to zackmichaels_proj_1/launch/zackmichaels_project_1_launch.py
2. At line 107, set the default value to the world that you want to be run (World options listed at line 103)


## How to manipulate doors and lighting for indoor environment
### Doors
1. First start the Webots application
2. Click on the door you want opened
3. TO OPEN: Go to the doors position property and set its value to -1.50
4. TO CLOSE: Go to the doors position property and set its value to 0
### Lighting
1. First start the Webots application
2. Click on the ceiling light you want to be adjusted
3. Set the pointLightIntensity value to 0 for the light to be off or a positive value for it to be turned on, with increasing numbers increasing the brightness of the light

## How to manipulate lighting and stoplights for outdoor environment
### Lighting
1. Start Webot world
2. Navigate to the TexturedBackgroundLight object in the object list on the left
3. Set the luminosity value to 1 for day and 0 for night lighting
### Edit stoplight settings
1. Select your desired stoplight
2. Select the controller parameter
3. Click the 'edit' button
4. Adjust controller settings in the code editor for desired settings
		
