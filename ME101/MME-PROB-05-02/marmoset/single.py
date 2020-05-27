#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
single.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import re
import time
import sys

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./first_for_loop"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.01)
out = output_buffer_read.read()

loop_limit = 1

cproc.stdin.write(str(loop_limit) + "\n")
time.sleep(0.01)
out = output_buffer_read.read()

missing_number = False;
for check_number in range(1,loop_limit) :
    match_string = "^" + str(check_number) + "\s"
    match = re.match(match_string, out)

    if match :
        out = re.sub(match_string, '', out)
    else :
        print "Did not find " + str(check_number) + "<br>"
        missing_number = True;

if missing_number :
    print "FAILED"
    sys.exit(1)
else :
    print "PASSED - Found all numbers from 1 to " + str(loop_limit) + "."
    sys.exit(0)
