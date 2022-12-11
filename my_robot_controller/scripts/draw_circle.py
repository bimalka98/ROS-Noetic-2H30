#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

# bimalka98@LAP-BIMALKA98:~$ rosmsg show geometry_msgs/Twist
# geometry_msgs/Vector3 linear
#   float64 x
#   float64 y
#   float64 z
# geometry_msgs/Vector3 angular
#   float64 x
#   float64 y
#   float64 z

if __name__ == '__main__':
    rospy.init_node('draw_circle')
    rospy.loginfo("Node has been started!")

    # publishing to the turtles existing velocity command topic 
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        
        # publish cmd_vel
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        
        # publish the msg
        pub.publish(msg)

        rate.sleep()

# bimalka98@LAP-BIMALKA98:~$ rostopic info /turtle1/cmd_vel 
# Type: geometry_msgs/Twist

# Publishers: 
#  * /draw_circle (http://LAP-BIMALKA98:46635/)

# Subscribers: 
#  * /turtlesim (http://LAP-BIMALKA98:44519/)
