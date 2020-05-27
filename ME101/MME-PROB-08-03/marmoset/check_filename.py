#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

import os
import sys

expected_file_name = "factorial.cpp"

# print os.listdir(".")
if os.path.isfile(expected_file_name) :
    print "PASSED - correct file name used: " + expected_file_name
    sys.exit(0)
else :
    print "FAILED - incorrect file name submitted<br>"
    print "expected file name is " + expected_file_name
    sys.exit(1)
