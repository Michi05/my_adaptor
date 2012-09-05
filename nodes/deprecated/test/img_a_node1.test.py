#!/usr/bin/env python
PKG = 'image_adaptor'
import roslib; roslib.load_manifest(PKG)

import sys
import unittest

# Import the code to test
import img_a_node

## A sample python unit test
class TestBareBones(unittest.TestCase):
    def instanceTranslations(self):
        mainTranslator = propertyTranslator(getParam(PROP_CONFIG_FILENAME))

    def instance3DMgr(dynServers):
        mainDriverManager = manager3D(dynServers = [dynParamServerPath])

    def instanceInterface(translator, driverMgr):
        img_interface_node(translator = mainTranslator, driverMgr = mainDriverManager)

######################################################################################
######################################################################################

    ## test 1 == 1
    def test_one_equals_one(self):
        self.assertEquals(1, 1, "1!=1")

##    def test_choice(self):
##        element = random.choice(self.seq)
##        self.assertTrue(element in self.seq)

 
if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'resulting_test', TestBareBones)

## REMINDER: your package will need to depend on 'rosunit' in the manifest.xml.

