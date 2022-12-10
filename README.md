# ROS-Noetic-2H30
ROS Tutorial (ROS1) - ROS Noetic 2H30 [Crash Course on YouTube](https://youtu.be/wfDJAYTMTdk)

## Directory structure of the catkin workspace ``

```shell
user@host:~/ros/yt_ros_ws
└── src
    └── my_robot_controller       # package name
        ├── CMakeLists.txt
        ├── package.xml
        ├── scripts               # directory containing the python scripts (nodes)
        │   └── my_first_node.py  # sample python script
        └── src
```

## Running a Node

**Note** :  ROS version must be sourced before anything `source /opt/ros/noetic/setup.bash`

1. Give execution permission to the python script `$ chmod +x script.py`
2. Change directory to the catkin workspace and do `$ catkin build`
3. source the setup basch script in `devel` directory `$ source ~/ros/yt_ros_ws/devel/setup.bash`
4. Initialize ros master `$ roscore`
5. Run the node `$ rosrun <package name> <script.py>`


