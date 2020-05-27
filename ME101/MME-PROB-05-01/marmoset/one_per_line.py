#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
one_per_line.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys
import os

cproc=Popen("./first_while_loop", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

parsed_output = re.split("\n", out)

expected_numbers = True;

if len(parsed_output) >= 25 :
    for count in range(1,26) :
        if len(parsed_output[0]) > 0 and int(parsed_output[0]) == count :
            del parsed_output[0]
        else :
            expected_numbers = False;
else :
    expected_numbers = False;

while len(parsed_output) > 0 and parsed_output[0] == '' :
    del parsed_output[0]

unexpected_output = False;
if len(parsed_output) > 0 :
    unexpected_output = True;

if not expected_numbers :
    print "failed - Numbers on each line did not match expected numbers."
    sys.exit(1)
elif unexpected_output :
    print "failed - More output than expected."
    sys.exit(1)
else :
    print "passed - Outputted numbers from 1 to 25."
    sys.exit(0)
