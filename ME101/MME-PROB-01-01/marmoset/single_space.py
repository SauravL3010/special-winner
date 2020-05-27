#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys

input = ["./hello_world"]
cproc=Popen(input, stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

match_space = re.findall(" ", out)
if len(match_space) == 1 :
    print "passed - one space in output"
    sys.exit(0)
else :
    print "failed - incorrect number of spaces found in output"
    print "number of spaces found: " + str(len(match_space))
    sys.exit(1)
