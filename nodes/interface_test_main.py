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


class TEST_img_interface_node (img_interface_node):
    def __init__(self, translator, driverMgr):
        self.translator = translator
        self.driverMgr = driverMgr
        self.avoidRemoteReconf = 0
        return

class TEST_manager3D (manager3D):
    def __init__(self, dynServers): ## , serverList):
        # Dictionary of multiplexors for remembering topic relocations
        self.createdMuxes = {}
        # Dictionary of parameter servers connected
        self.paramServers = {}
        # Self Reconfiguration semaphore begins with a 0
        self.avoidSelfReconf = 0
        return

class TEST_propertyTranslator (propertyTranslator):
    def __init__(self,config_filename):
        try:
            # Storing the filename as it's useful in case there is more than one instance
            self.property_config_file = config_filename
            
            # Defining names to avoid problems:
            self.translations = ([],[])
            self.ReversePropDict = {}
        except:
            rospy.logerr("Error while reading property configuration from file.")
            raise
        return

    def dynamicServers(self):
        return propertyTranslator.dynamicServers(self)
        


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

########################################################################################
########################################################################################
#####################################   TRANSLATOR   ###################################
########################################################################################
########################################################################################
            mainTranslator = TEST_propertyTranslator(privateParam(KEY_CONFIG_FILENAME, DEFAULT_CONFIG_FILENAME))
            
            ## Manual configuration for testing:
            
            try:
                # Loads the YAML Config in a pair of lists of names (drivers) and dictionaries (properties)
                mainTranslator.translations = mainTranslator.readYAMLConfig(mainTranslator.property_config_file)
                # A reverse dictionary is necessary to search for the original property names when needed
                mainTranslator.ReversePropDict = mainTranslator.generateReverseDictionary()

                rospy.loginfo("Property configuration loaded:")
            except:
                rospy.logerr("Error while reading property configuration from file.")
                raise








########################################################################################
########################################################################################
##################################### DRIVER MANAGER ###################################
########################################################################################
########################################################################################
            dynServers = mainTranslator.dynamicServers()
            mainDriverManager = TEST_manager3D(dynServers)
            
            ## Manual configuration for testing:
            
            try:
                ## It's assumed that every dynamic server has always a "set_parameters" service or it's just not running
                rospy.loginfo("Creating Dynamic Reconfigure Client")
                ## A reconfiguration callback will be shooted. The semaphore is incremented in order to take that into account 
                mainDriverManager.avoidSelfReconf = mainDriverManager.avoidSelfReconf + 1
                ## Connecting to all the different servers
                for server in dynServers: ## serverList:
                    rospy.loginfo("...waiting for server in %s."%(rospy.get_namespace() + server))
                    rospy.wait_for_service(server + "/set_parameters")
                    mainDriverManager.paramServers[server] = DynamicReconfigureClient(server, mainDriverManager.dynSrvTimeout, mainDriverManager.dynClientCallback)
                rospy.loginfo("Driver manager initialised.")
            except:
                rospy.logerr("Error while trying to connect to remote parameter server.")
                raise









########################################################################################
########################################################################################
#####################################   INTERFACE   ####################################
########################################################################################
########################################################################################
            
            
            globals()["ifcNode"] = TEST_img_interface_node(translator = mainTranslator, driverMgr = mainDriverManager)
                        
            ## Manual configuration for testing:
            
            try:
                ## Dynamic Reconfigure
                ifcNode.avoidRemoteReconf = ifcNode.avoidRemoteReconf + 1
                # Launch self DynamicReconfigure server
                ifcNode.dynServer = DynamicReconfigureServer(PropertiesConfig, ifcNode.dynServerCallback)
                # Launch request listener services
                ifcNode.listenToRequests()
                rospy.loginfo("Interface for requests created.")
            except:
                rospy.logerr("Error while trying to initialise dynamic parameter server.")
                raise
                
            rospy.loginfo("Waiting before cleaning renamings.")
            rospy.sleep(5)
            mainTranslator.cleanRenamings(mainDriverManager)
                
                
                
                
                
                
                
                
########################################################################################
########################################################################################
##################################### ACTUAL TESTING ###################################
########################################################################################
########################################################################################
            
            
            rospy.loginfo("Checking list of known properties:")
            try:
                amount_of_properties = 37
                propertyList = mainTranslator.get_property_list()
                assert (len(propertyList) == amount_of_properties)
                print "PASSED!"
            except:
                print "Error found: The property list has " + str(len(propertyList)) + " objects instead of the expected (" + str(amount_of_properties) + ")"

            
            rospy.loginfo("Showing the list of known dynamic servers:")
            try:
                amount_of_dynamicServers = 0
                serverList = mainTranslator.dynamicServers()
                print "PASSED!"
            except:
                print "Error found: The server list has " + str(len(serverList)) + " objects instead of the expected (" + str(amount_of_dynamicServers) + ")"

            ## Testing the path base name getter
            rospy.loginfo("Testing the path base name getter:")
            errors_found = 0
            for (example, result) in [("../strangespath//base1", "base1"),
                                    ("relativePath/base2/", "base2"),
                                    ("ilegalPath/base3//", ""), ## Right now this is correct according to the specification; maybe I should code something more intelligent
                                    ("/absolutePath/base4", "base4"),
                                    ("/absolutePath//base5/", "base5"),
                                    ("base6", "base6"),
                                    ("", "")]:
                try:
                    assert (TEST_propertyTranslator.get_basic_name(example) == result)
                    rospy.logdebug(TEST_propertyTranslator.get_basic_name(example) + " == " + result)
                except:
                    errors_found += 1
                    print "Error found: '" + TEST_propertyTranslator.get_basic_name(example) + "' != '" + result + "'"
            if errors_found < 1:
                print "NO errors were found while checking the get_basic_name method."

            ## DUMMY existence test:
            rospy.loginfo("DUMMY existence auto test:")
            success = True
            for prop in mainTranslator.get_property_list():
                try:
                    assert (mainTranslator.prop_exists(prop) == True)
                    rospy.logdebug("Property " + prop + " existence correctly checked.")
                except:
                    print "Error: '" + prop + "' should exist."
                    success = False
            if success:
                print "All the properties were checked and exist."

            ## Testing interpret and reverseInterpret:
            success = True
            rospy.loginfo("Testing interpret and reverseInterpret:")
            for prop in mainTranslator.get_property_list():
                try:
                    translation = mainTranslator.interpret(prop)[PPTY_REF]
#TODO: warn about ambiguities!!! Error with "freq" and "resol" are caused by that
#base = TEST_propertyTranslator.get_basic_name(translation)
                    reverted = mainTranslator.reverseInterpret(translation)
                    rospy.logdebug(str(prop) + " >> " + str(translation) + " >> " + str(reverted))
                    assert (reverted == prop)
                    rospy.logdebug("Property " + prop + " successfully interpreted and reversed.")
                except:
                    print "Error: Failed while trying to interpret or reverse the property: '" + prop + "' with reference: '" + mainTranslator.interpret(prop)[PPTY_REF] + "'."
                    success = False
            if success:
                print "All the properties have been interpreted correctly." 
                    
            ## Testing INexistence:
            success = True
            rospy.loginfo("INexistence test:")
            for prop_name, value, existence in [
                        ("fotograms", 13, False),
                        ("", -1, False)]:
                try:
                    assert(mainTranslator.updatePptyRef(prop_name, value)==None)
                    assert(mainTranslator.prop_exists(prop_name) == False)
                except:
                    print "Error: Inexistent property should return None or False."                    
                    success = False
            if success:
                print "All the INEXISTENT properties have been detected." 
            
###### Testing the utilities for properties ######
            ## Testing the property existence manually
            success = True
            rospy.loginfo("DUMMY existence manual test:")
            for prop_name, value, existence in [
                        ("fotograms", 13, False),
                        ("", -1, False)]:
                try:
                    assert(mainTranslator.prop_exists(prop_name) == existence)
                except:
                    print "Error while checking existence manually..."
                    success = False
            if success:
                print "Property existence testing succeed." 

            ## Testing the canGet canSet values
            success = True
            rospy.loginfo("Test the canGet/canSet methods:")
            for prop_name, can_get, can_set in [("fotograms", False, False),
                                     ("", False, False),
                                     ("depth_disparity", True, True), ## Topic
                                     ("depth", True, True),
                                     ("device_id", True, False), ## readOnly Parameter
                                     ("z_offset_mm", True, False),
                                     ("data_skip", True, True), ## dynParam
                                     ("depth_mode", True, True)]:
                
                mainTranslator.canGet(prop_name)
                try:
                    assert(mainTranslator.canGet(prop_name) == can_get)
                    assert(mainTranslator.canSet(prop_name) == can_set)
                except:
                    print "Error: canSet or canGet methods don't agree..."
                    print "The " + prop_name + " property canGet/canSet values are "
                    print str(mainTranslator.canGet(prop_name)) +  "/" + str(mainTranslator.canSet(prop_name))
                    print "...while they should be " + str(can_get) +  "/" + str(can_set)
                    success = False
            if success:
                print "canGet/canSet methods tested with success." 

            ## Testing the getServerPath
            success = True
            rospy.loginfo("Test the getServerPath method:")
            for dictIndex in xrange(len(mainTranslator.translations[1])):
                path = mainTranslator.translations[0][dictIndex]
                for prop in mainTranslator.translations[1][dictIndex]:
                    try:
                        assert(mainTranslator.getServerPath(prop) == path)
                    except:
                        print "There's a problem with getServerPath method"
                        print mainTranslator.getServerPath(prop), "different from", path
                        success = False
            if success:
                print "getServerPath method tested successfully." 


            destructiveTest = False
            if destructiveTest:
                ## Testing the updatePptyRef and get_topic_path methods ((DESTRUCTIVE; LAST ONE!!))
                success = True
                rospy.loginfo("Test the updatePptyRef and get_topic_path methods:")
                for dict in mainTranslator.translations[1]:
                    for prop in dict:
                        try:
                            newPath = "/not/a/real/path"
                            result = mainTranslator.updatePptyRef(prop, newPath)
                            ppty_data=mainTranslator.get_topic_path(prop)
                            assert(ppty_data == newPath)
                            assert(mainTranslator.get_property_list()[prop][PPTY_REF] == newPath)
                        except:
                            print "Unable to set the", prop, "property."
                            print mainTranslator.interpret(prop)[PPTY_REF], "!=", newPath
                            success = False
                if success:
                    print "updatePptyRef and get_topic_path methods tested successfully." 
                    print mainTranslator.get_property_list()
                return












    ## Testing the manager3D
            ## Testing the getServerPath
            success = True
            topicList = [("/rosout",True),
                         ("rosout",True),
                         ("/rosout_agg",True),
                         ("rosout_agg",True),
                         ("nonExistingStuff",False),
                         ("//thisShouldnt/exist",False)]
            rospy.loginfo("Test the topic_is_published method:")
            for topic, value in topicList:
                try:
                    assert(manager3D.topic_is_published(topic) == value)
                except:
                    print topic, "existence should be", str(value)
                    success = False
            if success:
                print "topic_is_published method tested successfully." 

                

            ## Testing the relocateTopic
            if destructiveTest:
                success = True
                topicList = [("/rosout","relative_slash_rosout",True),
                             ("rosout","/absolute_rosout",True),
                             ("/rosout_agg","relative_slash_ragg",True),
                             ("rosout_agg","/absolute_ragg",True),
                             ("nonExistingStuff","falseRelocationDone",True),
                             ("//thisShouldnt/exist","/doesntMatter/AsShould/Fail",True)]
                ## TODO: document: the environment just ignores empty subnames
                ##as in //thisShouldnt... which becomes /thisShoudlnt
                rospy.loginfo("Test the relocateTopic method:")
                for oldTopic, newTopic, value in topicList:
                    try:
                        response = mainDriverManager.relocateTopic(oldTopic, newTopic)
                        assert (response == value)
                    except:
                        print oldTopic, "should be redirected as", newTopic
                        success = False
                if success:
                    print "relocateTopic method tested successfully." 

                
                
                
                
                
                
                
                
                
                
                
                
                

    ## Testing the ctrl_interface
            ## Testing the setTopicLocation
            testRelocation = False
            if testRelocation:
                success = True
                topicList = [("depth_disparity","_slash_rosout",False),
                             ("depth","/aa_rosout",True),
                             ("depth_raw","aa_slash_ragg",True),
                             ("depth_rect","/_ragg",False),
                             ("depth_rect_raw","elocationDone",True),
                             ("depth_points","/AsShould/Fail",True)]
                rospy.loginfo("Test the setTopicLocation method:")
                for name, newTopic, value in topicList:
                    try:
                        param = setString()
                        param.topicName = name
                        param.newValue = newTopic
                        response = ifcNode.setTopicLocation(param)
                        
                        print response, "answer received while setting", name, " to ", value
                        print "Result is: " + ifcNode.get_property_list()[name][PPTY_REF]
                    except Exception as e:
                        if value == True:
                            print ifcNode.get_property_list()[name][PPTY_REF], "failed as it was suppossed to."
                        print "ERROR while trying to relocate ", name, "to", newTopic
                        print "ERROR = '" + e + "'."
                        success = False
                if success:
                    print "relocateTopic method tested successfully."
                    
                    
                rospy.sleep(10) 

                
            ## Testing the get_property_list
            rospy.loginfo("Test the get_property_list method:")
            print "This is the current property list according to get_property_list method:"
            print ifcNode.get_property_list()
                
            ## Testing the updateSelfParameters
            rospy.loginfo("Test the updateSelfParameters method:")
            success = True
            prop_list = [("image_mode",1),
                         ("image_mode",0), # There's no zero; it MUST fail
                         ("data_skip",5),
                         ("data_skip",0),
                         ("data_skip",9)]
            combinations = []
            for i in prop_list:
                combinations.append([i])
            for propagate in [True, False]:
                for pList in combinations:
                    newConfig = {}
                    for name, value in pList:
                        newConfig[name] = value
                        print newConfig
                    try:
                        response = ifcNode.updateSelfParameters(newConfig)
                        if response[name]==value:
                            print name, "was changed to", value
                        else:
                            print name, "was NOT changed to", value
                    except Exception as e:
                        rospy.logerr("ERROR while trying to set.")
                        rospy.logerr("** The current ERROR is: '" + str(e) + "'.")
                        success = False
            if success:
                print "updateSelfParameters method tested successfully." 
                
                
                
                
                
                
                
                
                
            
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
            rospy.sleep(10)
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

