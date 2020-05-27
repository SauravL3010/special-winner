#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
same_height.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

ELEVATION_CHANGE = 0
TOLERANCE = 1e-3

numeric_const_pattern = r"""
    \s*
    [-+]? # optional sign
    (?:
        (?: \d* \. \d+ ) # .1 .12 .123 etc 9.1 etc 98.1 etc
        |
        (?: \d+ \.? ) # 1. 12. 123. etc 1 12 123 etc
    )
    # followed by optional exponent part if desired
    (?: [Ee] [+-]? \d+ ) ?
    """

from time_of_flight import get_times
from subprocess import Popen,PIPE
from random import randint
import time
import os
import sys
import re

LAUNCH_VELOCITY = randint(100, 100000)/1000.0
LAUNCH_ANGLE = randint(1, 90)

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./time_of_flight"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = output_buffer_read.read()

cproc.stdin.write(str(LAUNCH_VELOCITY) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

cproc.stdin.write(str(LAUNCH_ANGLE) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

cproc.stdin.write(str(ELEVATION_CHANGE) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

find_numbers = re.findall(numeric_const_pattern, out, re.VERBOSE)
find_numbers = [float(number) for number in find_numbers]
find_numbers.sort()

EXPECTED_TIMES = get_times(LAUNCH_VELOCITY, LAUNCH_ANGLE, ELEVATION_CHANGE)

print "Launch velocity: " + str(LAUNCH_VELOCITY) + "<br>"
print "Launch angle: " + str(LAUNCH_ANGLE) + "<br>"

all_match = True
for number_output,number_expected in zip(find_numbers, EXPECTED_TIMES) :
    if abs(number_output - number_expected) > TOLERANCE :
        print "FAILED - output time does not match expected value <br>"
        print "expected value: " + str(number_expected)
        all_match = False

if all_match :
    print "PASSED - Elevation change zero.<br>"
    sys.exit(0)
else :
    sys.exit(1)
