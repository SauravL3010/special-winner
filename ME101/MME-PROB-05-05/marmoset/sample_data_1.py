#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sample_data_1.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

STEP_SIZE = 0.02
TOLERANCE = 1e-6

from approximate_integral import approximate_integral
from subprocess import Popen,PIPE
import os
import time
import re
import sys

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./approximate_integral"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = output_buffer_read.read()

cproc.stdin.write(str(STEP_SIZE)+"\n")
time.sleep(0.1)
out = output_buffer_read.read()

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

expected_value = approximate_integral(STEP_SIZE)
if abs(float(out) - expected_value) > TOLERANCE :
    print "FAILED - step_size: " + str(STEP_SIZE) + "<br>"
    print "expected value: " + str(expected_value)
    sys.exit(1)
else :
    print "PASSED - step_size: " + str(STEP_SIZE)
    sys.exit(0)
