#!/usr/bin/env python
import roslib; roslib.load_manifest('threedee')
import rospy

import sys
import cv

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

 # # # This file will be divided in two parts;
  # # # - 3D Data interface node
  # # # - Opencv image visor


#####################################################
#####################################################
PARAMETERS
 * /rosdistro
 * /camera/driver/rgb_frame_id
 * /camera/driver/rgb_camera_info_url
 * /camera/depth_registered/rectify_depth/interpolation
 * /camera/driver/depth_frame_id
 * /camera/depth/rectify_depth/interpolation
 * /rosversion
 * /camera/driver/device_id
 * /camera/driver/depth_camera_info_url
#####################################################
#####################################################


class args_getter_node:
    def __init__(self):
        return


# List of generic get interface methods

#	~kinect_depth_frame (string, default: "/kinect_depth")
#	the name of the Depth camera frame
    def get_kinect_depth_frame:
        parameter = "/kinect_depth"
        if rospy.has_param('~kinect_depth_frame'):
            parameter = rospy.get_param('~kinect_depth_frame', "/kinect_depth")
        return parameter

class main_node:
    def __init__(self):
        rospy.init_node('main_node')

        self.cv_window_name = "OpenCV Image"

        cv.NamedWindow(self.cv_window_name, 1)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_color",\
        Image, self.callback)

    def callback(self, data):
        try:
          cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
        except CvBridgeError, e:
          print e

        cv.ShowImage(self.cv_window_name, cv_image)
        cv.WaitKey(3)

    def printData(self, data):
        try:
          print data
        except Exception, e:
          print e

        cv.ShowImage(self.cv_window_name, cv_image)
        cv.WaitKey(3)

def callback(data):
    rospy.loginfo(rospy.get_name()+"I heard %s",data.data)

if __name__ == '__main__':
      vn = main_node()
      try:
        rospy.spin()
      except KeyboardInterrupt:
        print "Shutting node."
        cv.DestroyAllWindows()


