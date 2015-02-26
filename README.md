# ros-erle-camera
###Compile the code 

Add this folder to `catkin_ws/src` and the compile the code:

```
>> cd <your catkin_worspace>
>> catkin_make
```

Maybe you need to load the script:

```
>> source <your catkin_worspace>/devel/setup.bash
```

#USB camera

To run the server execute.

```
>>rosrun ros-erle-camera usb_cam
```
This component create several `topics`. To show all the topics, you can execute:

```
>>rostopic list
```

#Show the image

To visualize the image to need to run:

```
>>rosrun image_view image_view image:=/image_raw
```
