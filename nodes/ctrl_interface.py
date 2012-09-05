#!/usr/bin/env python
#########TODO?? ####### "# -*- coding: utf-8 -*-"

""" The following code implements an Adaptor Interface Node written in Python for Robot Operating System.
This module is meant to provide communication between any application able to communicate with this node
and any camera device drivers with the appropriate file configuration in the "translation.yaml" file.
"""



###############################################################################
##  *****     *****    Initially needed constants    *****     *****
###############################################################################
 # Constants
globals()["PACKAGE_NAME"] = 'my_adaptor'
###############################################################################












###############################################################################
##  *****     *****    CONFIGURATION PARAMETERS    *****     *****
###############################################################################
 ## Keys
globals()["KEY_CONFIG_FILENAME"] = "property_config_file"
globals()["KEY_CONFIG_TEST_FILENAME"] = "property_test_file"
globals()["KEY_TOPIC_TIMEOUT"] = "topic_time_out"
globals()["KEY_SERVICE_TIMEOUT"] = "service_time_out"

globals()["KEY_GET_STRING_SERVICE"] = "get_string_service_name"
globals()["KEY_GET_INT_SERVICE"] = "get_int_service_name"
globals()["KEY_GET_FLOAT_SERVICE"] = "get_float_service_name"
globals()["KEY_GET_BOOL_SERVICE"] = "get_bool_service_name"

globals()["KEY_GET_TOPIC_LOCATION"] = "get_topic_location_service_name"
globals()["KEY_GET_IMAGE"] = "get_image_service_name"
globals()["KEY_GET_DISP_IMAGE"] = "get_disp_image_service_name"

globals()["KEY_SET_STRING_SERVICE"] = "set_string_service_name"
globals()["KEY_SET_INT_SERVICE"] = "set_int_service_name"
globals()["KEY_SET_FLOAT_SERVICE"] = "set_float_service_name"
globals()["KEY_SET_BOOL_SERVICE"] = "set_bool_service_name"

globals()["KEY_SET_TOPIC_LOCATION"] = "set_topic_location_service_name"
globals()["KEY_PUB_IMAGE"] = "pub_image_service_name"
globals()["KEY_PUB_DISP_IMAGE"] = "pub_disp_image_service_name"


 ## Defaults
globals()["DEFAULT_CONFIG_FILENAME"] = "propertyConfigFile.yaml"
globals()["DEFAULT_CONFIG_TEST_FILENAME"] = "propertyTestFile.yaml"
globals()["DEFAULT_TOPIC_TIMEOUT"] = 3
globals()["DEFAULT_SERVICE_TIMEOUT"] = 3

globals()["DEFAULT_GET_STRING_SERVICE"] = "get/StringProperty"
globals()["DEFAULT_GET_INT_SERVICE"] = "get/IntProperty"
globals()["DEFAULT_GET_FLOAT_SERVICE"] = "get/FloatProperty"
globals()["DEFAULT_GET_BOOL_SERVICE"] = "get/BoolProperty"

globals()["DEFAULT_GET_DISP_IMAGE"] = "get/DispImage"
globals()["DEFAULT_GET_IMAGE"] = "get/Image"
globals()["DEFAULT_GET_TOPIC_LOCATION"] = "get/TopicLocation"

globals()["DEFAULT_SET_STRING_SERVICE"] = "set/StrProperty"
globals()["DEFAULT_SET_INT_SERVICE"] = "set/IntProperty"
globals()["DEFAULT_SET_FLOAT_SERVICE"] = "set/FloatProperty"
globals()["DEFAULT_SET_BOOL_SERVICE"] = "set/BoolProperty"

globals()["DEFAULT_SET_TOPIC_LOCATION"] = "set/TopicLocation"
globals()["DEFAULT_PUB_IMAGE"] = "publishImages"
globals()["DEFAULT_PUB_DISP_IMAGE"] = "publishDispImages"


# Global values
globals()["propertyConfigFile"] = globals()["DEFAULT_CONFIG_FILENAME"]
globals()["propertyTestFile"] = globals()["DEFAULT_CONFIG_TEST_FILENAME"]
globals()["topicTimeOut"] = globals()["DEFAULT_TOPIC_TIMEOUT"]
globals()["serviceTimeOut"] = globals()["DEFAULT_SERVICE_TIMEOUT"]

globals()["getStrSrv"] = globals()["DEFAULT_GET_STRING_SERVICE"]
globals()["getIntSrv"] = globals()["DEFAULT_GET_INT_SERVICE"]
globals()["getFloatSrv"] = globals()["DEFAULT_GET_FLOAT_SERVICE"]
globals()["getBoolSrv"] = globals()["DEFAULT_GET_BOOL_SERVICE"]

globals()["getLocationSrv"] = globals()["DEFAULT_GET_TOPIC_LOCATION"]
globals()["getImgSrv"] = globals()["DEFAULT_GET_IMAGE"]
globals()["getDispImgSrv"] = globals()["DEFAULT_GET_DISP_IMAGE"]

globals()["setStrSrv"] = globals()["DEFAULT_SET_STRING_SERVICE"]
globals()["setIntSrv"] = globals()["DEFAULT_SET_INT_SERVICE"]
globals()["setFloatSrv"] = globals()["DEFAULT_SET_FLOAT_SERVICE"]
globals()["setBoolSrv"] = globals()["DEFAULT_SET_BOOL_SERVICE"]

globals()["setLocationSrv"] = globals()["DEFAULT_SET_TOPIC_LOCATION"]
globals()["pubImgSrv"] = globals()["DEFAULT_PUB_IMAGE"]
globals()["pubDispImgSrv"] = globals()["DEFAULT_PUB_DISP_IMAGE"]

###############################################################################










###############################################################################
##  *****     *****    External modules to import    *****     *****
###############################################################################
# ****   Standard Python Utility Modules
#==============================================================================
import roslib; roslib.load_manifest(PACKAGE_NAME)
import rospy
import sys
# March19 - YAML library for configuration file.
import yaml
# April17 - Command line calls for launching nodes
import subprocess
import shlex



###############################################################################
# ****   ROS-specific objects and definitions to import
#==============================================================================

#from dynamic_reconfigure.encoding import Config as dynReconfConfig
# January23 - Including services
from my_adaptor.srv import *
# January 24 - Including ALL the standard types
#(I think they'll all be necessary at some point)
from std_msgs.msg import *
# January31 - Dynamic Reconfigure
from dynamic_reconfigure.client import Client as DynamicReconfigureClient
from dynamic_reconfigure.server import Server as DynamicReconfigureServer
from my_adaptor.cfg import PropertiesConfig
# February14
from stereo_msgs.msg import *
from sensor_msgs.msg import *
###############################################################################












###############################################################################
##  *****     *****    This file is divided in three classes:    *****     *****
###############################################################################
# # # - Driver manager (communicate with layer below)
# # # - Interface node (communicate with layer above)
# # # - Property translator




###############################################################################
##  *****     *****    ((Self agreement)):    *****     *****
###############################################################################
# # #  *** ( Not being followed anymore by the moment ) ***
        # "None" values mean that some Error was already reported
        # "False", negative or empty strings (depending on the place) mean that there was an error but still unknown
    #Reasons:
            #In case an error is not really taken into account; "None" will produce a second error that will be noticeable
            #Some structures haven't got any "empty" element to return but in the lowest level is sometimes possible to just
        #check if something is possible; read whatever the return value is (can be external) and answer whatever
            #In the lowest level, it should be possible to ask to check something: "if isThatThingWorking():" and get True
        #or False as the answer: but it's not an error that the answer is False, the error is finding that it shouldn't!





###############################################################################
##  ****     ****    To avoid getting stuck in config updates:    ****     ****
###############################################################################
#avoidSelfReconf = 0
#avoidRemoteReconf = 0
# These vbles are incremented as many times as propagations to avoid. When below 1,
#then there are real callbacks:
 # # avoidSelfReconf ++;
 # # ** UNEXPECTED REAL CALLBACK **
 # # ** real callback call avoided **
 # # update_config(...)
 # # ** second callback updates everything
#==============================================================================



















###############################################################################
##  *****     *****    Beginning of the executable code    *****     *****
###############################################################################
# ****   Assigning values to "constants" (used as literals):
#==============================================================================

## The names of the equivalent data types in python native types and
# ROS basic data types.
remoteType = {str: String, int: UInt16, float: Float64, bool: Bool}
## List of known kinds of properties
# The interface knows how to handle these properties and only these.
kindOfProperty = set(["dynParam", "parameter", "topic", "service", "virtual", "renaming"]) ## "publishedtopic" removed
##ppty = {"reference":0, "type":1, "kind":2}
PPTY_REF = 0# ppty[0]
PPTY_TYPE = 1# ppty[1]
PPTY_KIND = 2# ppty[2]
###############################################################################












###############################################################################
##  *****     *****    img_interface_node Class    *****     *****
###############################################################################

class img_interface_node: ## This is the LISTENER for the layer ABOVE
    """The 'img_interface_node' is the class which communicates to the layer above
    according to this structure. It provides services and dynamic reconfigure server
    and also publishes topics."""



###############################################
##  *****     Static Data Members     *****
###############################################
# ****   Services provided to the above layer
#==================================================
    listOf_services = {}



###############################################
##  *****     Constructor Method     *****
###############################################

    def __init__(self, translator, driverMgr):
        """initialises img_interface_node instances by launching the dynamic reconfigure server
        until it is called to launch services for listening. It doesn't receive or return
        anything.

        @param self - self object for the call.
        @param translator - a reference to the translator object/instance to be used.
        @param driverMgr - a reference to the object/instance of the driver manager to
                            be used (bottom layer)."""
        self.translator = translator
        self.driverMgr = driverMgr
        self.avoidRemoteReconf = 0
        try:
            ## Dynamic Reconfigure
            self.avoidRemoteReconf = self.avoidRemoteReconf + 1
            # Launch self DynamicReconfigure server
            self.dynServer = DynamicReconfigureServer(PropertiesConfig, self.dynServerCallback)
            # Launch request listener services
            self.listenToRequests()
            rospy.loginfo("Interface for requests created.")
        except:
            rospy.logerr("img_interface_node::Error: while trying to initialise dynamic parameter server.")
            raise
        return





###################################################
##  *****     General Purpose Methods     *****
###################################################
# ****   Launch services for receiving requests
#==================================================

    def listenToRequests(self):
        """Main services creator method in order to remain listening for requests.
        It receives nothing and returns true just for future needs.

        @param self - self object for the call.

        @return True if it finishes. Otherwise it would just raise an exception
                as there are no checks."""
        self.listOf_services[getStrSrv] = rospy.Service(getStrSrv, stringValue, self.getStringProperty)
        self.listOf_services[getIntSrv] = rospy.Service(getIntSrv, intValue, self.getIntProperty)
        self.listOf_services[getFloatSrv] = rospy.Service(getFloatSrv, floatValue, self.getFloatProperty)
        self.listOf_services[getBoolSrv] = rospy.Service(getBoolSrv, booleanValue, self.getBoolProperty)

##MICHI: 14Feb2012
        self.listOf_services[getImgSrv] = rospy.Service(getImgSrv, normalImage, self.getImage)
        self.listOf_services[getDispImgSrv] = rospy.Service(getDispImgSrv, disparityImage, self.getDispImage)
##MICHI: 13Mar2012
        self.listOf_services[pubImgSrv] = rospy.Service(pubImgSrv, requestTopic, self.publishImages)
        self.listOf_services[pubDispImgSrv] = rospy.Service(pubDispImgSrv, requestTopic, self.publishDispImages)
##MICHI: 16Apr2012
        self.listOf_services[getLocationSrv] = rospy.Service(getLocationSrv, stringValue, self.getTopicLocation)
        self.listOf_services[setLocationSrv] = rospy.Service(setLocationSrv, setString, self.setTopicLocation)

        self.listOf_services[setStrSrv] = rospy.Service(setStrSrv, setString, self.setStrProperty)
        self.listOf_services[setIntSrv] = rospy.Service(setIntSrv, setInteger, self.setIntProperty)
        self.listOf_services[setFloatSrv] = rospy.Service(setFloatSrv, setFloat, self.setFloatProperty)
        self.listOf_services[setBoolSrv] = rospy.Service(setBoolSrv, setBoolean, self.setBoolProperty)
        rospy.loginfo("Ready to answer service requests.")
        return True



###################################################
# ****   Dynamic Reconfigure related methods
#==================================================

    def dynServerCallback(self, dynConfiguration, levelCode):
        """Handler for the changes in the Dynamic Reconfigure server.
        Must return a configuration in the same format as received.

        @param self - self object for the call.
        @param dynConfiguration - a dictionary of {property:value} with the changes to be done.
                            Precondition: the names of the properties are the LOCAL names.
        @param levelCode - the code generated during the callback as a hint of which group of
                            properties where changed.

        @return The dictionary with the final configuration (as the callback requires to)."""
        if self.avoidRemoteReconf > 0:
            rospy.loginfo("LOCAL configuration was changed by self (levelCode = %s)"%levelCode)
            self.avoidRemoteReconf = self.avoidRemoteReconf - 1
        elif levelCode != 0:
            rospy.loginfo("LOCAL configuration changing.".rjust(80, '_'))
            for elem in dynConfiguration:
                if self.translator.canSet(elem):
                    success = self.setAnyProperty(elem, dynConfiguration[elem])
                    if success == False or success == None:
                        rospy.logerr("dynServerCallback::Error: Changing %s failed with value %s..."%(elem,dynConfiguration[elem]))
                        value = self.getAnyProperty(elem)
                        if value != None:
                            dynConfiguration[elem] = value
                        else:
                            rospy.logerr("dynServerCallback::Error: unable to read '" + elem + "' back.")
                        rospy.logdebug("...%s used"%(dynConfiguration[elem]))
        return dynConfiguration
    
    def updateSelfFromRemote(self, dynConfiguration):
        """It would be necessary to "translate" the local names into remote names if it is needed
        to be used the "updateSelfParameters method.
        

        @param self - self object for the call.
        @param dynConfiguration - a dictionary of {property:value} with the changes to be done.
                            Precondition: the names of the properties are the REMOTE names.

        @return The dictionary with the final configuration just in case there was any changes to it."""
## TODO: be careful with the PPTY_REF of the parameters; it may be the same path/subParam/paramName
#or the absolute path or just "paramName"...
        ## From REMOTE to LOCAL names:
        newConfig = {}
        for elem, value in [(i, dynConfiguration[i]) for i in dynConfiguration]:
            paramName = self.translator.reverseInterpret(elem)
            if paramName != None and paramName != False and paramName != "":
                newConfig[paramName] = value ## i.e.: { dictionary[parameter] = value }
            else:
                rospy.logdebug("updateSelfParameters::Ignoring unknown REMOTE name while updating self configuration: " + elem)
        
        localConfig = self.updateSelfParameters(newConfig, avoidPropagation=True)
        
        ## From LOCAL to REMOTE names:
        for elem, value in [(i, localConfig[i]) for i in localConfig]:
            name = self.translator.interpret(elem)
            if name != None and name != False and name != "":
                dynConfiguration[name[PPTY_REF]] = value
            else:
                rospy.logdebug("updateSelfParameters::Ignoring unknown LOCAL name while updating self configuration: " + elem)
        ## Send the -already translated- configuration.
        return dynConfiguration


    def updateSelfParameters(self, newConfig, avoidPropagation=False):
        """This method is responsible for changing the node's own dynamic reconfigure parameters
        from its own code ***but avoiding a chain of uncontrolled callbacks!!.

        @param self - self object for the call.
        @param newConfig - a dictionary of {property:value} with the changes to be done.
                            Precondition: the names of the properties are the LOCAL names.
        @param avoidPropagation - boolean to indicate whether if not to prevent the changes to be
                                propagated downwards (in case that they already come from there).

        @return The dictionary with the final configuration just in case there was any changes to it."""
        if avoidPropagation == True:
            self.avoidRemoteReconf = self.avoidRemoteReconf + 1
        return self.dynServer.update_configuration(newConfig)


    def getTopicLocation(self, getStrMsg):
        """Gets the location of an existing topic in the ROS environment.

        @param self - self object for the call.
        @param getStrMsg - a service structure including:
            string topicName - the name of the topic which location is to be returned.
            ***************
            string topicValue for storing the return value.

        @return A string answering weather if the relocation was successful
                or not and describing the possible error."""
        return self.getStringProperty(getStrMsg)


    def setTopicLocation(self, setStrMsg):
        """Sets a new location in the ROS environment for an existing topic.

        @param self - self object for the call.
        @param setStrMsg - a service structure including:
            string topicName - the name of the topic to be relocated
            string newValue - the new path or name of the topic after relocation
            ***************
            string setAnswer for storing the return value

        @return A string answering weather if the relocation was successful
                or not and describing the possible error."""
        rospy.loginfo (str("Received call to set/TopicLocation " + setStrMsg.topicName + " " + setStrMsg.newValue))
        translation = self.translator.interpret(setStrMsg.topicName)
        if translation != None and (translation[PPTY_KIND]=="topic"):
            oldAddress = translation[PPTY_REF]
        else:
            oldAddress = setStrMsg.topicName
        try:
            rospy.loginfo (str("...relocating " + oldAddress + " as " + setStrMsg.newValue + "..."))
            success = self.driverMgr.relocateTopic(oldAddress, setStrMsg.newValue)
            ## If it was a name; the value needs to be updated in the translator
            if success == True and translation != None:
                self.translator.updatePptyRef(setStrMsg.topicName, setStrMsg.newValue)
            else:
                print "Translator not updated"
        except Exception as e:
            rospy.logerr("Exception while relocating: %s"%(e))
            return str("Exception while relocating: %s"%(e))
        return "Success!"


###################################################
# ****   Generic handlers for getting and setting parameters
#==================================================

    def setAnyProperty(self, propertyName, newValue):
        """Generic setter in order to redirect to the type-specific setter method.
        Received the LOCALLY KNOWN name of a property and sets the associated remote value.

        @param self - self object for the call.
        @param propertyName - the LOCAL name of the property to be set.
        @param newValue - the new value to be set for the property.

        @return True if success and False otherwise."""
        propertyData = self.translator.interpret(propertyName)
        if propertyData == None:
            rospy.logdebug("setAnyProperty::called with an unknown property name.")
            return None
        #else:
        if (propertyData[PPTY_TYPE].lower()).find("string") >= 0:
#            if type(newValue) != str:
#                print "Error: value '%s' seems to be %s instead of '%s' which is needed"%(newValue, type(newValue), propertyData[PPTY_TYPE])
#                return None
            valueType = str
        elif (propertyData[PPTY_TYPE].lower()).find("int") >= 0:
            valueType = int
        elif (propertyData[PPTY_TYPE].lower()).find("double") >= 0 or (propertyData[PPTY_TYPE].lower()).find("float") >= 0:
            valueType = float
        elif (propertyData[PPTY_TYPE].lower()).find("bool") >= 0:
            valueType = bool
        else:
            rospy.logerr("setAnyProperty::Error: non registered value type.")
            return None
        return self.setFixedTypeProperty(propertyName, newValue, valueType)


	####################################
	# Specific fixed type property setters
	#===================================
    ## The next methods are the callbacks for the setter services
    ##all of them are supposed to return the resulting values to
    ##inform in case the set event failed.
    ## In case there's an error; the error message is sent no
    ##matter the returning type is
    def setStrProperty(self, setterMessage):
        return self.setFixedTypeProperty(setterMessage.topicName, setterMessage.newValue, str)
    def setIntProperty(self, setterMessage):
        return self.setFixedTypeProperty(setterMessage.topicName, setterMessage.newValue, int)
    def setFloatProperty(self, setterMessage):
        return self.setFixedTypeProperty(setterMessage.topicName, setterMessage.newValue, float)
    def setBoolProperty(self, setterMessage):
        return self.setFixedTypeProperty(setterMessage.topicName, setterMessage.newValue, bool)

    def setFixedTypeProperty(self, localPropName, newValue, valueType):
        """Main property setter receiving the property name, the value to assign and its type
        and returning the response from the "setRemoteValue" method from the low level driver.
        
        Precondition: the localPropName must be a known local name and the change is supposed to
        be remote. Not meant to be used for local changes in this layer.

        @param self - self object for the call.
        @param localPropName - the LOCAL name of the property to be set.
        @param newValue - the new value to be set for the property.
        @param valueType - the expected data type of the value to be set.

        @return True if success and False otherwise."""
## TODO: rewrite this so it returns something else than true/false (or make everything coherent at least)
        propertyData = self.translator.interpret(localPropName)
        if propertyData == None:
            rospy.logerr("setFixedTypeProperty::Error: trying to set not found property.")
            return False
        response = True
        if propertyData[PPTY_KIND] == "dynParam":
            remotePropName = propertyTranslator.get_basic_name(propertyData[PPTY_REF])
            path = self.translator.getServerPath(remotePropName)
            temp = self.driverMgr.setRemoteValue(remotePropName, newValue, path, self)
            if temp==None:
                rospy.logerr("setFixedTypeProperty::ERROR while setting remote property: " + remotePropName)
                response = False
        elif propertyData[PPTY_KIND] == "topic":
            self.driverMgr.sendByTopic(rospy.get_namespace() + propertyData[PPTY_REF], newValue, remoteType[valueType])
        else:
            response = False
            rospy.logerr("setFixedTypeProperty::Error: unable to set local property %s of kind: '%s'"%(localPropName, propertyData[PPTY_KIND]))
        return response


# Getter and getter handlers
    # Generic setter in order to redirect to the appropriate method
    def getAnyProperty(self, propertyName):
        """Generic getter in order to get any property with any kind or type.

        @param self - self object for the call.
        @param propertyName - the LOCAL name of the property to be get.

        @return the read value or None if there was some error."""
        propertyData = self.translator.interpret(propertyName)
        if propertyData == None:
            return None
        #else:
        if propertyData[PPTY_TYPE].find("string") >= 0:
            valueType = str
        elif (propertyData[PPTY_TYPE].lower()).find("int") >= 0:
            valueType = int
        elif (propertyData[PPTY_TYPE].lower()).find("double") >= 0 or (propertyData[PPTY_TYPE].lower()).find("float") >= 0:
            valueType = float
        elif (propertyData[PPTY_TYPE].lower()).find("bool") >= 0:
            valueType = bool
        else:
            rospy.logerr("getAnyProperty::Error: non registered value type")
            return None
        return self.getFixedTypeProperty(propertyName, valueType)

    # Generic getter in order to redirect to the appropriate method
    #Specific fixed type property getters
    def getStringProperty(self, srvMsg):
        return self.getFixedTypeProperty(srvMsg.topicName, str)
    def getIntProperty(self, srvMsg):
        return self.getFixedTypeProperty(srvMsg.topicName, int)
    def getFloatProperty(self, srvMsg):
        return self.getFixedTypeProperty(srvMsg.topicName, float)
    def getBoolProperty(self, srvMsg):
        return self.getFixedTypeProperty(srvMsg.topicName, bool)
    def getImage(self, srvMsg):
        """Handler for getting images when called from a service.

        @param self - self object for the call.
        @param srvMsg - a service structure including:
            int64 nImages - amount of images to retransmit.
            string sourceTopic - original topic from which to get the images.
            string responseTopic - target topic path through which to send them.

        @return the images read from the source."""
        respImages = []
        while len(respImages) < srvMsg.nImages:
            respImages.append(self.getFixedTypeProperty(srvMsg.topicName, None))
        return respImages
    def getDispImage(self, srvMsg):
        """Handler for getting disparity images when called from a service.

        @param self - self object for the call.
        @param srvMsg - a service structure including:
            int64 nImages - amount of images to retransmit.
            string sourceTopic - original topic from which to get the images.
            string responseTopic - target topic path through which to send them.

        @return the images read from the source."""
        respImages = []
        while len(respImages) < srvMsg.nImages:
            respImages.append(self.getFixedTypeProperty(srvMsg.topicName, None))
        for image in respImages:
            self.driverMgr.sendByTopic("testImages", image, DisparityImage)
        return respImages
##AMPLIATION: I could add normalImage.timestamp (time[] timestamp) if needed (including the changes in the "normalImage.srv"
## in that case I would need a normalImage variable and set both fields: images and timestamp

    def getFixedTypeProperty(self, localPropName, valueType):
        """Main property getter receiving the property name and the value type
        and returning the current value from the low level driver.

        @param self - self object for the call.
        @param localPropName - the LOCAL name of the property to be get.
        @param valueType - the expected data type of the value to be get.

        @return the read value or None if there was some error."""
        propertyData = self.translator.interpret(localPropName)
        if propertyData == None:
            return None
        #else:
        if propertyData[PPTY_KIND] == "dynParam":
            remotePropName = propertyTranslator.get_basic_name(propertyData[PPTY_REF])
            response = self.driverMgr.getValue(remotePropName, self.translator.getServerPath(localPropName))
#        elif propertyData[PPTY_KIND] == "publishedTopic":
#            response = self.driverMgr.getTopic(propertyData[PPTY_REF], valueType)
        elif propertyData[PPTY_KIND] == "parameter":
            remotePropName = propertyTranslator.get_basic_name(propertyData[PPTY_REF])
            location = rospy.search_param(remotePropName)
            response = rospy.get_param(location)
        elif propertyData[PPTY_KIND] == "topic":
            if valueType == str:
                response = str(propertyData[PPTY_REF])
            else: ## Special case for reading disparity images
                valueType2 = DisparityImage
                if propertyData[PPTY_TYPE].find("Disparity") < 0:
                    valueType2 = Image
                response = self.driverMgr.getTopic(propertyData[PPTY_REF], valueType2)
        else:
            rospy.logerr("getFixedTypeProperty::Error: unable to get property %s of kind %s"%(localPropName, propertyData[PPTY_TYPE]))
            response = None
        return response


    # Method to request the complete list of properties
    def get_property_list(self):
        """Auxiliary method for receiving the list of properties known by the translator.

        @param self - self object for the call.

        @return complete list of properties from the translator."""
        return self.translator.get_property_list()
    
    # Methods related to requesting topics to publish
    def publishImages(self, srvMsg):
        """Specific purpose method meant to retransmit, when asked via-service, an image topic
        through a topic path receiving the original path, the new path and the amount of messages.

        @param self - self object for the call.
        @param srvMsg - a service structure including:
            int64 nImages - amount of images to retransmit.
            string sourceTopic - original topic from which to get the images.
            string responseTopic - target topic path through which to send them.

        @return string message telling whether if it worked or not."""
        topicPath = self.translator.get_topic_path(srvMsg.sourceTopic)
        self.driverMgr.retransmitTopic(srvMsg.nImages, topicPath, srvMsg.responseTopic, Image)
        "%s images sent from %s topic to %s."%(srvMsg.nImages, srvMsg.sourceTopic, srvMsg.responseTopic)
        return "%s images sent from %s topic to %s."%(srvMsg.nImages, srvMsg.sourceTopic, srvMsg.responseTopic)
    
    def publishDispImages(self, srvMsg):
        """Specific purpose method meant to retransmit, when asked via-service, a DISPARITY image topic
        through a topic path receiving the original path, the new path and the amount of messages.

        @param self - self object for the call.
        @param srvMsg - a service structure including:
            int64 nImages - amount of images to retransmit.
            string sourceTopic - original topic from which to get the images.
            string responseTopic - target topic path through which to send them.

        @return string message telling whether if it worked or not."""
        topicPath = self.translator.get_topic_path(srvMsg.sourceTopic)
        self.driverMgr.retransmitTopic(srvMsg.nImages, topicPath, srvMsg.responseTopic, DisparityImage)
        "%s images sent from %s topic to %s."%(srvMsg.nImages, srvMsg.sourceTopic, srvMsg.responseTopic)
        return "%s images sent from %s topic to %s."%(srvMsg.nImages, srvMsg.sourceTopic, srvMsg.responseTopic)







###############################################################################
##  *****     *****    propertyTranslator Class    *****     *****
###############################################################################

class propertyTranslator(object):
    """This 'PropertyTranslator' class is the module to change driver names and paths into
the ones offered by the interface and the other way around. It stores two dictionaries (for
both translations) and several methods for translating."""


###############################################
##  *****     Constructor Method     *****
###############################################
    def __init__(self,config_filename):
        """Initialises new instances of the propertyTranslator objects by
        reading the new configuration and creating the dictionary and the
        reverse translation dictionary.
        
        @param self - self object for the call.
        @param config_filename - the name AND PATH to the file from which to read
                            to read the configuration."""
        try:
            # Storing the filename as it's useful in case there is more than one instance
            self.property_config_file = config_filename
            # Loads the YAML Config in a pair of lists of names (drivers) and dictionaries (properties)
            self.translations = self.readYAMLConfig(file_name = config_filename)
            # A reverse dictionary is necessary to search for the original property names when needed
            self.ReversePropDict = self.generateReverseDictionary()
            
            rospy.loginfo("Property configuration loaded:")
        except:
            rospy.logerr("propertyTranslator::Error while reading property configuration from file.")
            raise
        return

###################################################
##  *****     General Purpose Methods     *****
###################################################
# ****   Interpret and Reverse interpret
#==================================================

    def updatePptyRef (self, propertyName, newPath):
        """Changes the REMOTE name or path to a property in the
        translation dictionary.
        
        @param self - self object for the call.
        @param propertyName - the LOCAL name of a property.
        @param newPath - the REMOTE new name to assign to the property.

        @return The new path assigned if the property was found.
                None otherwise."""
        for dictIndex in xrange(len(self.translations[1])):
            if propertyName in self.translations[1][dictIndex]:
                self.translations[1][dictIndex][propertyName][PPTY_REF] = newPath
                return newPath
        return None
        
    def interpret(self, propertyName):
        """Receives a generic name specified in the YAML config
        Returns the associated values for the driver according to:
        [property name, data type, kind of property].
        
        @param self - self object for the call.
        @param propertyName - the LOCAL name of a property.

        @return The REMOTE name of the same property if found.
                None otherwise"""
        for dictionary in self.translations[1]:
            if propertyName in dictionary:
                return dictionary[propertyName]
        rospy.logdebug("Property '%s' not found. Returning None type value.")
        return None

    def reverseInterpret(self, reverseProperty):
        """Reads from the reverse dictionary, the LOCAL name associated with
        the received REMOTE name.

        @param self - self object for the call.
        @param reverseProperty - the REMOTE name of the property.

        @return The LOCAL name of the same property if found. None otherwise"""
        result = None
        if reverseProperty in self.ReversePropDict:
            result = self.ReversePropDict[reverseProperty]
            rospy.logdebug("reverseInterpret::" + reverseProperty + " reversed as " + result)
        else:
            for completeName in [ str(path + "/" + reverseProperty) for path in self.translations[0]]:
                if completeName in self.ReversePropDict:
                    result = self.ReversePropDict[completeName]
        if result == None:
            rospy.logdebug("reverseInterpret::Parameter '%s' not found in the property list."%(reverseProperty))
        return result



###################################################
# ****   Methods for loading property configuration
#==================================================

    def readYAMLConfig(self, file_name):
        """This method receives a file_name in which to read the properties.
        Returned Value MUST be a tuple of two lists with strings and
        dictionaries respectively.

        @param self - self object for the call.
        @param file_name - the name AND PATH to the file from which to read
                            the configuration.

        @return A tuple of two list. The first stores the path to each driver
                and the second the associated dictionary in the same index."""
        newDictionaries = ([],[])
        yamlConfig = ""
        cfgFile = file(file_name, 'r')
        if cfgFile != None:
            try:
                yamlConfig = yaml.safe_load_all(cfgFile)
            except yaml.YAMLError, exc:
                if hasattr(exc, 'problem_mark'):
                    mark = exc.problem_mark
                    raise Exception("readYAMLConfig::exception: in YAML file '%s'::f%s,col%s." % (file_name, mark.line+1, mark.column+1))
                else:
                    raise Exception("readYAMLConfig::exception: Unknown in YAML file '%s'." % (file_name))
        else:
            raise Exception("Unable to open YAML configuration file '%s'." % (file_name))

        ## Once the config is successfully loaded:
        for page in yamlConfig:
            if len(page) < 1:
                rospy.logerr("WRONG CONFIG FORMAT!! Nothing found in this page. Exactly one entry expected.")
            if len(page) > 1:
                rospy.logerr("STRANGE CONFIG FORMAT!! More than one dictionary in a single page. Exactly one entry expected.")
# There is supposed to be only 1 dictionary but it
#can be useful for the future making it with a loop
            for driverName in page:
                ## Store the properties in the second list...
                newDictionaries[1].append(page[driverName])
                ##...and the driver path without the last '/'
                if len(driverName) > 0 and driverName[-1] == '/':
                    newDictionaries[0].append(driverName[:-1])
                else:
                    newDictionaries[0].append(driverName)
        
        print " Translation Configuration read from YAML file:"
        for driver, dictionary in zip(newDictionaries[0], newDictionaries[1]): ## enumerate() if index numbers needed
            print "\r\n\r\nDictionary %s:"%driver
            for elem in dictionary:
                print elem, "\t:\t", dictionary[elem]
        return newDictionaries
    

    def cleanRenamings(self, driverManager):
        """Launches a multiplexor node that relocates a topic to a new address.
        
        NOTE: Right now it checks if the topic exists... That may be avoidable if
        the multiplexor can be working anyway for future topics.
        The method is supposed to be launched from the outside when loading; the
        later the better.

        @param self - self object for the call.
        @param driverManager - the reference to the driverManager object to be
                                used for the relocations.
        PRECONDITION: the driverManager must be already initialised
        and the topics must be already published (at least by now)."""
        dictionaryList = self.translations[1]
        for dictionary in dictionaryList:
            for renaming in [prop for prop in dictionary if dictionary[prop][PPTY_KIND]=="renaming"]:
## TODO: document this with care; only topics can be renamed and the "renaming" keyword should be configurable
## the type of topic is being obviously ignored; which can have secondary effects maybe?
                rospy.loginfo("Automatically renaming from " + dictionary[renaming][PPTY_REF] + " to " + renaming)
                translation = self.interpret(dictionary[renaming][PPTY_REF])
                if translation != None and (translation[PPTY_KIND]=="topic"):
                    oldAddress = translation[PPTY_REF]
                    rospy.loginfo("...the " + dictionary[renaming][PPTY_REF] + " property is mapped as " + oldAddress)
                else:
                    oldAddress = dictionary[renaming][PPTY_REF]
                    
                try:
                    rospy.loginfo("Remaping from " + oldAddress + " to " + renaming)
                    driverManager.relocateTopic(oldAddress, renaming)
                    ## If it was a name; the value needs to be updated in the translator
                    if translation!= None and oldAddress == translation[PPTY_REF]:
                        self.translator.updatePptyRef(dictionary[renaming][PPTY_REF], renaming)
                except Exception as e:
                    rospy.logerr("Exception during initial relocation: %s"%(e))
                    return
                else: ## In case there was no exception
                    del dictionary[renaming]
        return
    
    
    def generateReverseDictionary(self):
        """Generates a dictionary for the translator using the driver-side name as
        key and the name inside of the interface as value as the correlation is
        needed in both directions.

        @param self - self object for the call.

        @return The reversed dictionary of properties indexed by the REMOTE names
                both with and without the paths."""
        reversePropDict = {}
        rospy.loginfo("Storing the reverse dictionary")
        for dictionary in self.translations[1]:
            for elem in dictionary:
                reversePropDict[dictionary[elem][PPTY_REF]] = elem
                reversePropDict[self.get_basic_name(dictionary[elem][PPTY_REF])] = elem
        return reversePropDict


    def dynamicServers(self, checkDynamic=True):
        """Generates a list with the relative or absolute paths of the different
        dynamic reconfigure servers according to the YAML property configuration file.
            In the current version checkDynamic forces the method to ignore the path if
        there are no dynamic parameters in its list.

        @param self - self object for the call.
        @param checkDynamic - decides weather if checking or not that there actually are
                            dynamic properties for each dynamic server.

        @return The list of paths to the available servers."""
        driverServers = []
        for elem, index in [(elem, index) for elem, index in zip(self.translations[0], xrange(len(self.translations[0]))) if elem != "" and elem != "~"]:
            # If check is off, any non-empty string different from '~' is added
            if (checkDynamic == False):
                driverServers.append(elem)
                break
            #else: # The existence of dynamic parameters is checked
            for prop in [prop for prop in self.translations[1][index] if self.translations[1][index][prop][PPTY_KIND] == "dynParam"]:
                driverServers.append(elem)
                break
        return driverServers

###################################################
# ****   Properties Utility Methods
#==================================================

    def prop_exists(self, propertyName):
        """Receives the name of a property and checks if it exists in the dictionary
        (meaning the same as if it is known by the translator).

        @param self - self object for the call.
        @param propertyName - the local name of the property to be checked.

        @return True if the property was found in the dictionary. False otherwise."""
# return (self.interpret(propertyName) != None) ## This line would look less efficient but more maintainable
        for dictionary in self.translations[1]:
            if propertyName in dictionary:
                return True
        return False;
        
    def canSet(self, propertyName):
        """Receives the name of a property and decides whether if it can be Setted or not.

        @param self - self object for the call.
        @param propertyName - the local name of the property to be checked.

        @return True if the property was found and it can be get. False otherwise."""
        kindsToSet = set (["dynParam", "topic"])
        prop_data = self.interpret(propertyName)
        if prop_data != None:
            return (prop_data[PPTY_KIND] in kindsToSet)
        return False
    def canGet(self, propertyName):
        """Receives the name of a property and decides weather if it can be Getted or not.

        @param self - self object for the call.
        @param propertyName - the local name of the property to be checked.

        @return True if the property was found and it can be get. False otherwise."""
        kindsToGet = set (["dynParam", "parameter", "topic"])
        prop_data = self.interpret(propertyName)
        if prop_data != None:
            return (prop_data[PPTY_KIND] in kindsToGet)
        return False

    def getServerPath(self, propName):
        """Receives a property name.
        If the property exists, the driver's path is returned
        Otherwise, the response is None

        @param propName - the known complete name of a property (which may
                        include a relative path to diferentiate from others).

        @return the LAST 'part' of the name without the relative path."""
        for dictIndex in xrange(len(self.translations[1])):
            if propName in self.translations[1][dictIndex]:
                return (self.translations[0][dictIndex])
        return None

## TODO: the following explanation is not clear at all.
    @staticmethod
    def get_basic_name(propName):
        """Static method that receives a string with any name or path
        and returns the name after the last slash. That is:
        propName = /rootDir/secondary/package/whatever/propName = propName/

        @param propName - the known complete name of a property (which may
                        include a relative path to diferentiate from others).

        @return the LAST 'part' of the name without the relative path or an
            empty string if the first was not possible."""
        if len(propName) < 1:
            return ""
        if len(propName.split("/")[-1]) > 0:
            propName = propName.split("/")[-1]
        else:
            propName = propName.split("/")[-2]
        # Cleaning '~' in private names
        propName = propName[propName.find('~')+1:]
        return propName
    
    def get_topic_path(self, topicName):
        """Method to get the path to a certain topic.
        If the given name exists as a topic; the name is returned,
        otherwise, the name is translated with the dictionary.

        @param self - self object for the call.
        @param topicName - the property name of the topic to be found.

        @return the complete path to the topic associated with the received name."""
        prop_data = self.interpret(topicName)
        # If no interpretation found, the name is assumed to be a path itself
        if prop_data == None:
            rospy.logdebug(topicName + " -- doesn't exist as a property. Assuming that it is a path.")
            return topicName
        return prop_data[PPTY_REF]

    def get_property_list(self):
        """Method that returns the complete list of properties.

        @param self - self object for the call.

        @return the complete list with the known properties."""
        propList = {}
        for dictionary in self.translations[1]:
            for elem in dictionary:
                propList[elem] = dictionary[elem]
        return propList






###############################################################################
##  *****     *****    manager3D Class    *****     *****
###############################################################################

class manager3D:
    """Communication module class for handling the low-level driver. That
    is the manager for the layer below, so all the requests should use this module in
    order to observe the structure."""


###############################################
##  *****     Static Data Members     *****
###############################################
    dynSrvTimeout = globals()["serviceTimeOut"]


###############################################
##  *****     Constructor Method     *****
###############################################
    def __init__(self, dynServers):
        '''Initialises new instances of manager3D objects by initialising the attributes
        for the objects and trying to create the objects with connections to the different
        remote dynamic param servers.

        @param self - self object for the call.
        @param dynServers - the list of paths to the remote servers to connect
                            with.

        @return Nothing. Raises an exception if there's an unexpected error.'''
        # Dictionary of multiplexors for remembering topic relocations
        self.createdMuxes = {}
        # Dictionary of parameter servers connected
        self.paramServers = {}
        # Self Reconfiguration semaphore begins with a 0
        self.avoidSelfReconf = 0
        try:
            ## It's assumed that every dynamic server has always a "set_parameters" service or it's just not running
            rospy.loginfo("Creating Dynamic Reconfigure Client;")
            ## A reconfiguration callback will be shooted. The semaphore is incremented in order to take that into account 
            self.avoidSelfReconf = self.avoidSelfReconf + 1
            ## Connecting to all the different servers
            for server in dynServers: ## serverList:
                rospy.loginfo("...waiting for server in %s."%(rospy.get_namespace() + server))
                rospy.wait_for_service(server + "/set_parameters")
                self.paramServers[server] = DynamicReconfigureClient(server, self.dynSrvTimeout, self.dynClientCallback)
            rospy.loginfo("Driver manager initialised.")
        except:
            rospy.logerr("manager3D::Error: while trying to connect to remote parameter server.")
            raise
        return



###################################################
##  *****     Getter and Setter Methods     *****
###################################################
# ****   Parameter getters and setters for any type
#==================================================
    def getValue(self, propName, dynServerPath):
        '''Receives the REMOTE name of a property in the TARGET server
        (that is: already translated except for... local changes?).
        Returns the current value or the.

        @param self - self object for the call.
        @param propName - name of the property to be read.
        @param dynServerPath - path of the server in which to set the property.

        @return The obtained value if possible or None otherwise.'''
        if dynServerPath in self.paramServers:
            remoteServer = self.paramServers[dynServerPath]
            currentConfig = remoteServer.get_configuration(self.dynSrvTimeout)
            if propName in currentConfig:
                rospy.logdebug(str("Read parameter %s=%s from %s"%(propName, currentConfig[propName], dynServerPath)))
                return currentConfig[propName]
        return None

    def setRemoteValue(self, rPropName, newValue, dynServerPath, ifcNodeInstance):
        '''Receives a value and the REMOTE name of a property in the TARGET server
        (that is: already translated except for... local changes?).
        Returns the new configuration or a None type if the change wasn't possible.

        @param self - self object for the call.
        @param rPropName - REMOTE name of the property to be set.
        @param newValue - value to be set for the property.
        @param dynServerPath - path of the remote server in which to set the property.
        @param ifcNodeInstance - the "img_interface_node" object that allows to change
                                the properties in the local sserver.

        @return The obtained value if possible or None otherwise.'''
        if dynServerPath in self.paramServers:
            remoteServer = self.paramServers[dynServerPath]
            newConfig = {rPropName:newValue}
            self.avoidSelfReconf = self.avoidSelfReconf + 1
            try:
                requestResult = remoteServer.update_configuration(newConfig)
            except Exception as e:
                rospy.logerr("setRemoteValue::Exception: while setting parameter in remote dynamic server: " + str(e))
            else:
                if requestResult[rPropName] != newValue:
                    rospy.logerr("setRemoteValue::Error: while setting parameter in dynamic server; falling down to actual configuration.")
                    response = ifcNodeInstance.updateSelfFromRemote(requestResult, True)
                    # Should I return the "response" value (self configuration) or the requestResult (remote configuration) ??
                    if response == None:
                        rospy.logerr("setRemoteValue::Error: while updating self parameters in self dynamic reconfiguration.")
                # The whole configuration is returned in order to check possible side changes
                return requestResult
        return None


###################################################
# ****   Topic getter for different types
#==================================================
    def getTopic(self, topicName, data_type = str):
        """Read value from topic with given name.

        @param self - self object for the call.
        @param topicName - topic name in which to listen to the value.
        @param data_type - the type of the message in order to handle the topic.

        @return the obtained value (without checking or validating it)."""
        rospy.loginfo("Requesting %s with type %s"%(topicName, data_type))
        rcvdMsg = rospy.wait_for_message(topicName, data_type, globals()["topicTimeOut"])
        return rcvdMsg

    def sendByTopic(self, topic, value, data_type = UInt16):
        """ Publishes a given value just once and then exits.
        #If no connections listening, the method waits up to a second before publishing
        #and then publishes in either case.

        @param self - self object for the call.
        @param topic - topic name in which to publish the value.
        @param value - value to be published.
        @param data_type - the type of the message in order to handle the topic.

        @return the resulting configuration returned after the update attempt."""
        attemptedTimes = 0
        pub = rospy.Publisher(topic, data_type)
        while pub.get_num_connections() < 1 and attemptedTimes < 10:
            rospy.Rate(10).sleep() # Sleep 10 times/sec (10Hz)
            attemptedTimes = attemptedTimes + 1 
        pub.publish(value)
        return True

    def retransmitTopic(self, times, source_topic, output_topic, data_type = UInt16):
        """Method meant to be executed in a different thread in order
        to repeat a number of messages received from a topic to another one.

        @param self - self object for the call.
        @param times - how many times to repeat the action. I.e. how many messages to retransmit.
        @param source_topic - original topic from which to read the messages.
        @param output_topic - target topic name in which to publish the messages.
        @param data_type - the type of the messages in order to handle the topics.

        @return False if the topic doesn't seem to be published. True if success. Otherwise an exception is raised"""
        if topic_is_published(source_topic) == False:
            rospy.logwarn("Unable to find %s topic in order to retransmit it"%(source_topic))
            return False
        rospy.loginfo("Trying to retransmit %s in %s."%(source_topic, output_topic))
        publisher_topic = rospy.Publisher(output_topic, data_type)
        try:
            for i in xrange(0, times):
                publisher_topic.publish(rospy.wait_for_message(source_topic, data_type, globals()["topicTimeOut"]))
        except exception as e:
            rospy.logerr("Failed while trying to retransmit %s topic in %s.")
        return True



###################################################
##  *****     General Purpose Methods     *****
###################################################
# ****   Callback for Dynamic Reconfigure Client
#==================================================
    def dynClientCallback(self, dynConfiguration):
        '''This callback is the one to be called when there's a change in a remote dynamic
        reconf. server, that is: with remote names in the the "dynConfiguration" variable.
        
        If the change was initially done by this node, "avoidSelfReconf" is different from 0
        and no action is taken.
        Otherwise the changes are sent to the updateSelfFromRemote method to update the values
        in the local dyn. reconf. server.

        @param self - self object for the call.
        @param dynConfiguration - a dictionary with the configuration according to which the
                                server should be updated.

        @return the resulting configuration returned after the update attempt.'''
        if self.avoidSelfReconf > 0:
            self.avoidSelfReconf = self.avoidSelfReconf - 1
        else:
            rospy.loginfo("Remote configuration changed. Updating self.".rjust(80, '-'))
            dynConfiguration = globals()["ifcNode"].updateSelfFromRemote(dynConfiguration, avoidPropagation=False, remoteNames=True)
        return dynConfiguration

    def relocateTopic(self, oldAddress, newAddress):
        '''This very important method is meant to change the topics from one name (or address) to another in runtime.
        Since that not possible in a literal way; "mux" tool is used to repeat them under the new name/address.
        
        PRECONDITION: the oldAddress is in fact an address, not a name, since it hasn't got any sense to have names at this level
        
        ### Here's a next step when they complete their development >>> callService("rosspawn/start", "")

        @param self - self object for the call.
        @param oldAddress - the already-existing topic that is to be changed.
        @param newAddress - the new address in which to publish the topic after relocation.

        @return False if the first character is NOT a letter. True on success.
        Otherwise the error is unknown and exception is launched.'''
        #TODO: The above is not true, the exception is still raised when the name is not valid.
        for word in newAddress.split('/'):
            if len(word) > 0 and word[0].isalpha() == False:
                raise Exception("Impossible to relocate to a topic with first character", word[0], "in", word + ". Valid characters are a-z, A-Z.")
        myNamespace = '/'.join(rospy.get_namespace().split('/')[:-2])
        newIndex = len(self.createdMuxes)+1
        
        if not oldAddress in self.createdMuxes:
            ## In case that the oldAddress is a new address, the new "addressSub0" is the original one
            for addressSub0 in [j for j in self.createdMuxes if self.createdMuxes[j][1]==oldAddress]:
                oldAddress=addressSub0
                
        if oldAddress in self.createdMuxes:
            ## In case the oldAddress is already relocated, the first node is killed
            newIndex = self.createdMuxes[oldAddress][0]
            rospy.logdebug(str("I will execute: rosnode kill " + myNamespace + '/mux' + str(newIndex)))
            subprocess.Popen(shlex.split('rosnode kill ' + myNamespace + '/mux' + str(newIndex)), close_fds=True)
        ## Postcondition: the index is up to date and the previous mux node is supposed to be already killed
        self.createdMuxes[oldAddress] = (newIndex, newAddress) ## Maybe the address should be checked first
        rospy.logdebug("Relocating from " + oldAddress + " to " + newAddress)
        rospy.logdebug('I will execute: roslaunch ' + globals()["PACKAGE_NAME"] + ' runMultiplexers.launch namespace:="' + myNamespace + '" node_id:="mux' + str(newIndex) + '" args:="' + newAddress + ' ' + oldAddress + '"')
        subprocess.Popen(shlex.split('roslaunch my_adaptor runMultiplexers.launch namespace:="' + myNamespace + '" node_id:="mux' + str(newIndex) + '" args:="' + newAddress + ' ' + oldAddress + '"'), close_fds=True)
##        subprocess.Popen(shlex.split('rosrun topic_tools mux ...
        return True


###################################################
# ****   Service Callers
#==================================================
    def callService(service, arguments, valueType = stringValue):
        '''Calls services in a generic way as it was an interface to call any of them.
        NOTE: It is not being used right now for the moment but it may be useful in the future.

        @param service - the name of the service to be called.
        @param arguments - the arguments which are to be passed when calling the service.
        @param valueType - the data type of the request/response messages of the service, according to the .srv files.

        @return true on success'''
        try:
            rospy.wait_for_service(service, timeout = globals()["serviceTimeOut"])
            remoteFunction = rospy.ServiceProxy(service, valueType)
            response = remoteFunction(arguments)
            rospy.loginfo("Service call response is %s"%response)
        except rospy.ServiceException as service_exception:
            response = None
            rospy.logerr("Service call failed: %s"%(service_exception))
        except Exception as e:
            response = None
            rospy.logerr("Exception while calling service: %s"%(e))
        return response
    


###################################################
# ****   Static utility methods
#==================================================
    @staticmethod
    def topic_is_published(topicName):
        '''Checks if the passed topic is currently published in the environment.

        @param topicName - the name of the topic which will be checked for existence.

        @return true on success'''
        if topicName[0] == "/":
            for topic in [name[0] for name in rospy.get_published_topics('/')]:
                if topicName == topic:
                    return True
        else:
            for topic in [name[0] for name in rospy.get_published_topics('/')]:
                if topic.find(topicName) >= 0:
                    return True
        rospy.logdebug(topicName + " topic not published")
        return False







###############################################################################
##  *****     *****    SINGLE UTILITY FUNCTIONS     *****     *****
###############################################################################
#  *****    Get Parameters from Parameter Server    *****
#==============================================================================
        
def searchParam(param_name):
    '''Looks for a parameter in the ROS parameter server and returns the value.
    It uses the "rospy.search_param" method which looks first in the private
    space and then outside.
    
    @param topicName - the name of the topic which will be checked for existence.

    @return the value of the parameter (otherwise it raises an exception).'''
    location = rospy.search_param(param_name)
    if location == None:
        raise Exception("searchParam::ERROR: Mandatory '%s' parameter not found."%(param_name))
    return rospy.get_param(location)
        
def privateParam(param_name, default_value=None):
    '''Tries to read a parameter only in the private space and returns either its
    value or the default value passed (None by default).
    
    @param param_name - the name of the topic which will be checked for existence.
    @param default_value - the default value in case that the value is not found.s

    @return the value of the parameter (otherwise it raises an exception).'''
    response = rospy.get_param("~" + param_name, default_value)
    if response == None:
        raise Exception("privateParam::ERROR: Mandatory '%s' parameter not found."%(param_name))
    else:
        rospy.set_param("~" + param_name, response)
    return response

