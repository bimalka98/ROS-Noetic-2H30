#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

# bimalka98@LAP-BIMALKA98:~$ rostopic info /turtle1/pose 
# Type: turtlesim/Pose

# Publishers: 
#  * /turtlesim (http://LAP-BIMALKA98:36309/)

# Subscribers: 
#  * /turtle_pose_subscriber (http://LAP-BIMALKA98:43567/)


def pose_callback(msg: Pose):
    rospy.loginfo("Turtle position = ({:.2f}, {:.2f})".format(msg.x, msg.y))

if __name__ == '__main__':
    
    rospy.init_node("turtle_pose_subscriber")

    sub = rospy.Subscriber('/turtle1/pose', Pose, callback=pose_callback)

    rospy.loginfo("Node has been started")

    # make a passive loop
    rospy.spin()