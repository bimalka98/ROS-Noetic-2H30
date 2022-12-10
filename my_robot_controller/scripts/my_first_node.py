#!/usr/bin/env python3
import rospy 

if __name__ == '__main__':
    rospy.init_node("test_node")
    rospy.loginfo("Test node started")
    

    rate = rospy.Rate(10) # 10 Hz

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep() # running the node in the given frequency