#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
one_per_line.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import re
import sys
import os
import time

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./first_for_loop"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.01)
out = output_buffer_read.read()

loop_limit = randint(10, 50)

cproc.stdin.write(str(loop_limit) + "\n")
time.sleep(0.01)
out = output_buffer_read.read()

parsed_output = re.split("\n", out)

expected_numbers = True;

if len(parsed_output) >= loop_limit :
    for count in range(1,loop_limit+1) :
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
    print "FAILED - Numbers on each line did not match expected numbers."
    sys.exit(1)
elif unexpected_output :
    print "FAILED - More output than expected."
    sys.exit(1)
else :
    print "PASSED - Each number outputted on a separate line."
    sys.exit(0)
