#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
numbers.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys
import os

cproc=Popen("./first_while_loop", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

missing_number = False;
for check_number in range(1,26) :
    match_string = "^" + str(check_number) + "\s"
    match = re.match(match_string, out)

    if match :
        out = re.sub(match_string, '', out)
    else :
        print "Did not find " + str(check_number) + "<br>"
        missing_number = True;

if missing_number :
    print "failed"
    sys.exit(1)
else :
    print "passed - Found all numbers from 1 to 25."
    sys.exit(0)
