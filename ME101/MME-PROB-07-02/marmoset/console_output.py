#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
console_output.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import sys

cproc=Popen("./coordinates_file_read", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

if len(out) < 2 :
    print "FAILED - No console output detected."
    sys.exit(1)
else :
    print "PASSED - Console output detected."
    sys.exit(0)
