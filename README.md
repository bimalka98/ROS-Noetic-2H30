# ROS-Noetic-2H30
ROS Tutorial (ROS1) - ROS Noetic 2H30 [Crash Course on YouTube](https://youtu.be/wfDJAYTMTdk)

## Directory structure of the catkin workspace

This repository resides inside the `src` directory of the catkin workspace named as `yt_ros_ws`.

```shell
user@host:~/ros/yt_ros_ws
└── src
    ├── figures
    │   ├── course-end.png
    │   ├── rosgraph-closedloop-pub-sub.png
    │   ├── rosgraph-publisher.png
    │   └── rosgraph-subscriber.png
    ├── my_robot_controller         # package name
    │   ├── CMakeLists.txt
    │   ├── package.xml
    │   ├── scripts                 # directory containing the python scripts (nodes)
    │   │   ├── draw_circle.py
    │   │   ├── my_first_node.py
    │   │   ├── pose_subscriber.py
    │   │   └── turtle_controller.py
    │   └── src
    └── README.md
```

## Running a Node

**Note** :  ROS version must be sourced before anything `source /opt/ros/noetic/setup.bash`

1. Give execution permission to the python script `$ chmod +x script.py`
2. Change directory to the catkin workspace and do `$ catkin build`
3. source the setup basch script in `devel` directory `$ source ~/ros/yt_ros_ws/devel/setup.bash`
4. Initialize ros master `$ roscore`
5. Run the node `$ rosrun <package name> <script.py>`

## Realizing Publisher-Subscriber Architecture

### Subsciber Program

In this program the custom node will subscribe to an existing `turtlesim/Pose` topic and prints the pose (x, y) coordinates.

![](figures/rosgraph-subscriber.png)

```
bimalka98@LAP-BIMALKA98:~$ rostopic info /turtle1/pose 
Type: turtlesim/Pose

Publishers: 
 * /turtlesim (http://LAP-BIMALKA98:36309/)

Subscribers: 
 * /turtle_pose_subscriber (http://LAP-BIMALKA98:43567/)
```

### Publisher Program

In this program the custom node will publish to an existing `/turtle1/cmd_vel` topic, to draw a circle.

![](figures/rosgraph-publisher.png)

```
bimalka98@LAP-BIMALKA98:~$ rostopic info /turtle1/cmd_vel 
Type: geometry_msgs/Twist

Publishers: 
 * /draw_circle (http://LAP-BIMALKA98:46635/)

Subscribers: 
 * /turtlesim (http://LAP-BIMALKA98:44519/)
```

### Pub-Sub Closed Loop Program

This program combines above two pub-sub mechanisms to control the turtle bot intelligently.

![](figures/rosgraph-closedloop-pub-sub.png)