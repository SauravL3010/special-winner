#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
no_loops.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import time
import os
import sys
import re
from remove_comments import remove_comments

remove_comments("binary_conversion.cpp", "no_comments.cpp")
file_binary_conversion = open("no_comments.cpp")

if re.search("\swhile\s*\(", file_binary_conversion.read(), re.MULTILINE) :
    print "failed - Found a while loop in the code."
    print "The customer doesn't understand while loops,"
    print "and asks you not to use them."
    exit(1)
elif re.search("\sfor\s*\(", file_binary_conversion.read(), re.MULTILINE) :
    print "failed - Found a for loop in the code."
    print "The customer doesn't understand for loops,"
    print "and asks you not to use them."
    exit(1)
elif re.search("\sdo\s*{", file_binary_conversion.read(), re.MULTILINE) :
    print "failed - Found a do-while loop in the code."
    print "The customer doesn't understand do-while loops,"
    print "and asks you not to use them."
    exit(1)
else :
    print "passed"
    exit(0)
