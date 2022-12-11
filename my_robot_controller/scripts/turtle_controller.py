#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

previous_x = 0

def call_set_pen_service(r, g, b, width, off):
    try:
        # arg1-name of srv: rosservice list, 
        # arg2-type of srv: rosservice info /turtle1/set_pen-> Type: turtlesim/SetPen
        set_pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)
        
        # Args: r g b width off
        response = set_pen(r, g, b, width, off)
        # rospy.loginfo("SetPen response: ", response)

    except rospy.ServiceException as e:
        rospy.logwarn(e)


def pose_callback(pose: Pose):

    cmd = Twist()

    # implemet the logic to avoid collision with the walls
    if pose.x > 9 or pose.x < 2 or pose.y > 9 or pose.y < 2 :
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
    
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0

    pub.publish(cmd)

    # change color of the pen depending on the region
    global previous_x

    if pose.x >=5.5 and previous_x <5.5:
        
        rospy.loginfo("Set color to red")
        call_set_pen_service(255, 0, 0, 4, 0)

    elif pose.x < 5.5 and previous_x >=5.5:
        
        call_set_pen_service(0, 255, 0, 4, 0)
        rospy.loginfo("Set color to green")
    
    previous_x = pose.x

if __name__ == '__main__':
    
    rospy.init_node('turtle_controller')
    rospy.loginfo('Running turtle controller')

    # wait for a service to start
    # use: rosservice list to get the list of services for a given node
    rospy.wait_for_service("/turtle1/set_pen")

    # publisher
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.loginfo('Initialized the publisher')

    # subscriber
    sub = rospy.Subscriber('/turtle1/pose', Pose, callback=pose_callback)
    rospy.loginfo('Initialized the subscriber')

    # passive loop
    rospy.spin()


#      bimalka98@LAP-BIMALKA98:~/ros/yt_ros_ws$ rosservice list 
#     /clear
#     /kill
#     /reset
#     /rosout/get_loggers
#     /rosout/set_logger_level
#     /spawn
#     /turtle1/set_pen
#     /turtle1/teleport_absolute
#     /turtle1/teleport_relative
#     /turtlesim/get_loggers
#     /turtlesim/set_logger_level

#     bimalka98@LAP-BIMALKA98:~/ros/yt_ros_ws$ rosservice info /turtle1/set_pen 
#     Node: /turtlesim
#     URI: rosrpc://LAP-BIMALKA98:44757
#     Type: turtlesim/SetPen
#     Args: r g b width off
    
#     bimalka98@LAP-BIMALKA98:~/ros/yt_ros_ws$ rossrv show turtlesim/SetPen
#     uint8 r
#     uint8 g
#     uint8 b
#     uint8 width
#     uint8 off
#     ---

#     bimalka98@LAP-BIMALKA98:~/ros/yt_ros_ws$ 