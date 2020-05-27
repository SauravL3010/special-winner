#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
randomize.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

STEP_SIZE = 1e-6
TOLERANCE = 1e-6

from approximate_integral import approximate_integral
from subprocess import Popen,PIPE
from random import randint
import os
import time
import re
import sys

passed_all = True
for run_number in range(0, 3) :

    STEP_SIZE = randint(1,9) * 10 / float(pow(10, randint(1,6)))

    output_buffer_write = open("out_buffer", "wb+")
    output_buffer_read = open("out_buffer", "rU")

    input = ["./approximate_integral"]
    cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
    time.sleep(0.1)
    out = output_buffer_read.read()

    out = cproc.communicate(str(STEP_SIZE)+"\n")
    out = output_buffer_read.read()

    expected_value = approximate_integral(STEP_SIZE)

    output_buffer_write.close()
    output_buffer_read.close()
    os.remove("out_buffer")

    if abs(float(out) - expected_value) > TOLERANCE :
        print "FAILED - step_size: " + str(STEP_SIZE) + "<br>"
        print "expected value: " + str(expected_value) + "<br>"
        passed_all = False
    else :
        print "PASSED - step_size: " + str(STEP_SIZE) + "<br>"

if passed_all :
    sys.exit(0)
else :
    sys.exit(1)
