#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String


class Append:
    def __init__(self):

        rospy.init_node('listener', anonymous=True)

        self.msg1 = rospy.Subscriber('chatter', String, self.callback_1)

        self.msg2 = rospy.Subscriber('chatter_2', String, self.callback_2)

        self.name = String()
        self.initial = String()

        self.rate = rospy.Rate(2)

    def callback_1(self, data):
        self.name = data.data
        #print(self.name)

    def callback_2(self, data):
        self.initial = data.data
        #print(self.name)

    def print_name(self):
        time.sleep(1)
        while not rospy.is_shutdown():
            print(self.name,self.initial)
            self.rate.sleep()


if __name__ == '__main__':
    try:
        x = Append()
        x.print_name()
    except rospy.ROSInterruptException:
        pass
