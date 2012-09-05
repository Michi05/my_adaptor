#!/usr/bin/env python

""" This is the main code for handling the "Control Interface" class."""



###############################################################################
##  *****     *****    Initially needed constants    *****     *****
###############################################################################
 # Constants
globals()["PACKAGE_NAME"] = 'my_adaptor'
###############################################################################








###############################################################################
##  *****     *****    External modules to import    *****     *****
###############################################################################
# ****   Standard Python Utility Modules
#==============================================================================
import roslib; roslib.load_manifest(PACKAGE_NAME)
import rospy
import sys

from ctrl_interface import *




###############################################################################
##  *****     *****    SINGLE UTILITY FUNCTIONS     *****     *****
###############################################################################
#  *****    Get Parameters from Parameter Server    *****
#==============================================================================
        
def searchParam(param_name):
    location = rospy.search_param(param_name)
    if location == None:
        raise Exception("ERROR: Mandatory '%s' parameter not found."%(param_name))
    return rospy.get_param(location)
        
def privateParam(param_name, default_value=None):
    response = rospy.get_param("~" + param_name, default_value)
    if response == None:
        raise Exception("ERROR: Mandatory '%s' parameter not found."%(param_name))
    else:
        rospy.set_param("~" + param_name, response)
    return response






###############################################################################
##  *****     *****    MAIN FUNCTION OF THE CODE     *****     *****
###############################################################################


def mainFunction(basename):
    ## Reading from arguments:
    rospy.loginfo("Initializing node")
    rospy.init_node(basename)

    globals()["propertyConfigFile"] = privateParam(KEY_CONFIG_FILENAME, DEFAULT_CONFIG_FILENAME)
    globals()["propertyTestFile"] = privateParam(KEY_CONFIG_TEST_FILENAME, DEFAULT_CONFIG_TEST_FILENAME)
    ## Update time outs according to parameters
    globals()["topicTimeOut"] = privateParam(KEY_TOPIC_TIMEOUT, DEFAULT_TOPIC_TIMEOUT)
    globals()["serviceTimeOut"] = privateParam(KEY_SERVICE_TIMEOUT, DEFAULT_SERVICE_TIMEOUT)
    
    
    globals()["getStrSrv"] = privateParam(KEY_GET_STRING_SERVICE, DEFAULT_GET_STRING_SERVICE)
    globals()["getIntSrv"] = privateParam(KEY_GET_INT_SERVICE, DEFAULT_GET_INT_SERVICE)
    globals()["getFloatSrv"] = privateParam(KEY_GET_FLOAT_SERVICE, DEFAULT_GET_FLOAT_SERVICE)
    globals()["getBoolSrv"] = privateParam(KEY_GET_BOOL_SERVICE, DEFAULT_GET_BOOL_SERVICE)
    
    globals()["getLocationSrv"] = privateParam(KEY_GET_TOPIC_LOCATION, DEFAULT_GET_TOPIC_LOCATION)
    globals()["getImgSrv"] = privateParam(KEY_GET_IMAGE, DEFAULT_GET_IMAGE)
    globals()["getDispImgSrv"] = privateParam(KEY_GET_DISP_IMAGE, DEFAULT_GET_DISP_IMAGE)
    
    globals()["setStrSrv"] = privateParam(KEY_SET_STRING_SERVICE, DEFAULT_SET_STRING_SERVICE)
    globals()["setIntSrv"] = privateParam(KEY_SET_INT_SERVICE, DEFAULT_SET_INT_SERVICE)
    globals()["setFloatSrv"] = privateParam(KEY_SET_FLOAT_SERVICE, DEFAULT_SET_FLOAT_SERVICE)
    globals()["setBoolSrv"] = privateParam(KEY_SET_BOOL_SERVICE, DEFAULT_SET_BOOL_SERVICE)
    
    globals()["setLocationSrv"] = privateParam(KEY_SET_TOPIC_LOCATION, DEFAULT_SET_TOPIC_LOCATION)
    globals()["pubImgSrv"] = privateParam(KEY_PUB_IMAGE, DEFAULT_PUB_IMAGE)
    globals()["pubDispImgSrv"] = privateParam(KEY_PUB_DISP_IMAGE, DEFAULT_PUB_DISP_IMAGE)



    while not rospy.is_shutdown():
        try:
## Initialising the 3 layers trying to avoid dependency problems
            mainTranslator = propertyTranslator(globals()["propertyConfigFile"])

            mainDriverManager = manager3D(dynServers = mainTranslator.dynamicServers())
            globals()["ifcNode"] = img_interface_node(translator = mainTranslator, driverMgr = mainDriverManager)
            
            rospy.loginfo("Waiting before cleaning renamings.")
            rospy.sleep(5)
            mainTranslator.cleanRenamings(mainDriverManager)
                
            
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
#            print "Unexpected error:", sys.exc_info()[1]
#            raise
            rospy.logerr("Error while trying to Initialise node. Waiting 10s")
            rospy.logerr(("Error: %s."%e).center(80, '*'))
            try:
        ## If there was any error I delete the objects and begin from scratch
        # I could just use a try/except for each initialisation but I don't see real improvement on that
                del mainTranslator
                del mainDriverManager
                del globals()["ifcNode"]
            except:
                pass
            rospy.sleep(10)## TODO: Parametrizar los .sleep??
            rospy.loginfo("Reinitializing Node")
        else:
            ## Everything is initialised and ready. Wait for requests:
            try:
                rospy.loginfo("...Image Adaptor initialized...")
            except KeyboardInterrupt:
                rospy.loginfo("Shutting down node.")
            else:
                rospy.spin()
    return





###############################################################################
##  *****    *****    ENTRY POINT FOR STARTING THE CODE    *****    *****
###############################################################################

if __name__ == '__main__':
    try:
        basename = sys.argv[0].split('/')[-1]
        if basename == "":
            basename = sys.argv[0].split('/')[-2]
        if basename[-3:] == ".py":
            basename = basename[0: -3]
        mainFunction(basename)
    except Exception as e:
        rospy.logerr("WHOLE-SCOPE EXCEPTION - NODE SHUTTING DOWN")
        rospy.logerr(("Error: %s."%e).center(80, '*'))
    finally:
        rospy.signal_shutdown("testing shutdown")

