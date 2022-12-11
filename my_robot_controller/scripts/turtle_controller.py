#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


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


if __name__ == '__main__':
    
    rospy.init_node('turtle_controller')
    rospy.loginfo('Running turtle controller')

    # publisher
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.loginfo('Initialized the publisher')

    # subscriber
    sub = rospy.Subscriber('/turtle1/pose', Pose, callback=pose_callback)
    rospy.loginfo('Initialized the subscriber')

    # passive loop
    rospy.spin()