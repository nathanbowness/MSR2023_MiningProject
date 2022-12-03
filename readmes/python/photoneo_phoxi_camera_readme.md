# phoxi_camera

This package enables interfacing Photoneo PhoXi 3D Scanner/Camera from ROS. 

<img src="http://photoneo.com/images/photoneo_scanner.png" width="640">

### Installation
*phoxi_camera* package depends on:
- ROS (we are using Kinetic)
- PhoXiControl version *1.2.x* driver software which you can download on Photoneo website: https://www.photoneo.com/3d-scanning-software/ (* contact support@photoneo.com for testing the release candidate)
#### Installation steps
- Download latest PhoXi Control
- Add rights to execute downloaded file 
```
sudo chmod +x PhotoneoPhoXiControlInstaller-xxxxx.run
```
- Install downloaded file 
```
sudo ./PhotoneoPhoXiControlInstaller-xxxxx.run
```
- clone phoxi_camera repository to your ROS workspace (usually catkin_ws/src)
```
cd catkin_ws/src
git clone https://github.com/photoneo/phoxi_camera
```
- Update rosdep
```
rosdep update
```
- Change working directory to your root ROS workspace folder (usually catkin_ws )
```
cd catkin_ws
```
- Install all dependencies needed by phoxi_camera package
```
rosdep install --from-paths src --ignore-src -r -y
```
#### Parameters

```
~/scanner_id                - Default PhoXi 3D Scannet to connect after startup. Default value: "InstalledExamples-PhoXi-example"
~/frame_id:                 - Frame id to which captured data relies to. Default value: "PhoXi3Dscanner_sensor"
~/latch_topics              - Default value: false
~/topic_queue_size          - Default value: 1
~/init_from_config          - Default value: false # if true all following parameters will be initialized from this config otherwise from PhoXi control application.
~/organized_cloud           - Default value: true  # if true organized point cloud will be published, other otherwise unorganized

## All following parameters are for PhoXi Control and they can override all dynamic_reconfigure parameters in cfg file.
#  This values are set to scanner after successful connection only if init_from_config parameter is true.
~/resolution                - Default value: 1  # 0 = Low, 1 = High
~/scan_multiplier           - Default value: 1
~/confidence                - Default value: 3.0
~/send_confidence_map       - Default value: true
~/send_depth_map            - Default value: true
~/send_normal_map           - Default value: true
~/send_point_cloud          - Default value: true
~/send_texture              - Default value: true
~/shutter_multiplier        - Default value: 1
~/timeout                   - Default value: -3    # in ms, special parameters: 0 = Zero, -1 = Infinity, -2 = Last stored, -3 = Default
~/trigger_mode              - Default value: 1     # 0 = Free run, 1 = Software

## Setting available only for PhoXi Control 1.2 and higher. Also for dynamic reconfigure
~/coordinate_space        - Default value: 1 # 1 = Camera, 2 =  Mounting, 3 = Marker, 4 = Robot, 5 = Custom
~/ambient_light_suppression - Default value: false  # Ambient light suppression samples the scene multiple times during one pattern exposure.
                                  # This multiple samples are then used to suppress the effect of ambient illumination by eliminating most of the shot noise caused by longer exposure of ambient light.
                                  # Enabling the mode will set Shutter multiplier to fixed value of 2.
~/single_pattern_exposure   - Default value: 20       # The time for projection of one pattern. Use only provided values form PhoXi control settings.
~/camera_only_mode          - Default value: false    # With this mode you can use the scanner internal camera to capture only 2D images of the scene. 
```

#### Available ROS services

For input and output parameters of each service please see coresponding service file in srv folder.
```
~/V2/is_acquiring
~/V2/is_connected
~/V2/start_acquisition
~/V2/stop_acquisition
~/connect_camera
~/disconnect_camera
~/get_device_list
~/get_frame
~/get_hardware_indentification
~/get_supported_capturing_modes
~/is_acquiring
~/is_connected
~/save_frame
~/set_parameters
~/start_acquisition
~/stop_acquisition
~/trigger_image
```
Services available only for PhoXi Control API version 1.2 and higher
```
~/V2/save_last_frame
~/V2/set_coordinate_space
~/V2/set_transformation
```

#### Available ROS topics
```
~/confidence_map
~/depth_map
~/normal_map
~/parameter_updates
~/pointcloud
~/rgb_texture
~/texture
```
### Test PhoXi ROS interface 
Rostests are used to test ROS node interfaces. These tests will try to connect 
and check if there are topics, services, and some basic parameters.

In config file **tests/interfaces/config.py** set camera ID. You can set up real scanner or file camera. 
For more information read **tests/README.md**

Launch test for phoxi_camera node interfaces:
```bash
rostest -t phoxi_camera phoxi_camera_interfaces.test 
```


### Test PhoXi ROS interface without real 3D scanner
It is possible to test PhoXi ROS interface without real hardware. 
- Start PhoXiControl application 
- Launch simple test example```roslaunch phoxi_camera phoxi_camera_test.launch```
- Application should connect to the camera and start aquiring example pointclouds
- Notice that pointcloud data are also being published on ROS topics
- Use available ROS services to control the dummy camera.

<img src="http://photoneo.com/images/PhoXiControl_01.jpg" width="640">


### Test PhoXi ROS interface with real device
- Start PhoXiControl application 
- Connect to your device
- Run Interface node ```rosrun phoxi_camera phoxi_camera ```
- Use available ROS services to control your 3D scanner

<img src=http://photoneo.com/images/PhoXiControl_02.jpg width="640">

See phoxi_camera [ROS Wiki page](http://wiki.ros.org/phoxi_camera) for further details. 

