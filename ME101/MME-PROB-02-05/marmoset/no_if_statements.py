#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
no_if_statements.py
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

if re.search("\sif\s*\(", file_binary_conversion.read(), re.MULTILINE) :
    print "failed - Found an if statement in the code."
    print "The customer doesn't understand if statements,"
    print "and asks you not to use them."
    exit(1)
else :
    print "passed"
    exit(0)
