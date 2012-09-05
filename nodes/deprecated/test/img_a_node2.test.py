#!/usr/bin/env python
PKG = 'image_adaptor'
import roslib; roslib.load_manifest(PKG)

import sys
import unittest

## A sample python unit test
class TestBareBones(unittest.TestCase):
    ## test 1 == 1
    def test_one_equals_one(self):
        self.assertEquals(1, 1, "1!=1")
 
if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'resulting_test', TestBareBones)

## REMINDER: your package will need to depend on 'rostest' in the manifest.xml.


