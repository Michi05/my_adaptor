#!/usr/bin/env python

# Import required Python code.
import sys
import roslib
roslib.load_manifest('interface_3D_node')
import rospy

#January 16th => Reconfigurable Parameters
import dynamic_reconfigure.client

#January 17th => Temporary GUI for testing
import Tkinter
from Tkinter import *

#January 23rd => Service Client
from interface_3D_node.srv import *

# Import custom message data.
#from kinect_aux/imu.msg import imuDataType
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64
from std_msgs.msg import UInt8

 ## Classes ##

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.command1 = Button(self)
        self.command1["text"] = "show_accel",
        self.command1["command"] = lambda: listener("show_accel")
        self.command1.pack
        self.command1.pack({"side": "bottom"})
        self.command1.pack({"side": "left"})

        self.command2 = Button(self)
        self.command2["text"] = "show_status",
        self.command2["command"] = callService
        self.command2.pack({"side": "bottom"})
        self.command2.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

 ## Single Functions ##

def callService():
    rospy.wait_for_service('/image_adaptor/image_adaptor/getIntValue')
    try:
        remoteFunction = rospy.ServiceProxy('/image_adaptor/image_adaptor/getIntValue', intValue)
        resp1 = remoteFunction("prop_data_skip")
        print resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    return

# Create a callback function for the subscriber.
def callback(data):
    # Simply print out values in our custom message.
    rospy.loginfo(rospy.get_name() + " I heard %s", data.header)
    rospy.loginfo(" With X,Y,Z = %s,%s,%s", data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z)

# This ends up being the main while loop.
def listener(command):
    # Get the ~private namespace parameters from command line or launch file.
#    topic = rospy.get_param('~topic', 'chatter')
## Next structure is a pythonic "select case"
    options = {"show_accel" : ('/imu', Imu),
               "show_tilt" : ('/cur_tilt_angle', Float64),
               "show_status" : ('/cur_tilt_status', UInt8),
               "update_tilt" : ('/tilt_angle', Float64),
               "image_mode" : ('/camera/driver/image_mode', int),
               "depth_mode" : ('~depth_mode', int),
               "depth_registration" : ('~depth_registration', int),
               "data_skip" : ('data_skip', int),
}
    topic, dataType = options[command]
    if command == "update_tilt":
        pub = rospy.Publisher(topic, dataType)
        pub.publish("10")
        rospy.spinOnce();
        return
    if command == "data_skip":
        client = dynamic_reconfigure.client.Client('/camera/driver')
        params = { topic : int(sys.argv[2]) }
        config = client.update_configuration(params)
        return
    timeout = 100
    # Create a subscriber with appropriate topic, custom message and name of callback function.
#    rospy.Subscriber(topic, Imu, callback)
    print "Reading topic %s"%topic
    rcvdMsg = rospy.wait_for_message(topic, dataType, timeout)
    if dataType == Imu:
        callback(rcvdMsg)
    else:
        print rcvdMsg
    # Wait for messages on topic, go to callback function when new messages arrive.
#    rospy.spin()

def usage():
    print "%s <command>"%sys.argv[0]
    print "show_accel"
    print "show_tilt"
    print "update_tilt"

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('pylistener', anonymous = True)

#    root = Tk()
#    app = Application(master=root)
#    app.mainloop()
#    root.destroy()

