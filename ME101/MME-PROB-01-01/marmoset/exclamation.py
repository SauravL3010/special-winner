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

match_exclamation = re.search("!\Z", out.rstrip())

if (match_exclamation) :
    print "passed - exclamation point at end of string"
    sys.exit(0)
else :
    print "failed - no exclamation point found at the end of the string"
    sys.exit(1)
