#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
float_radius.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

TOL_RELATIVE = 0.001

from sphere_calculations import sphere_calculations
from subprocess import Popen,PIPE
from random import randint
import time
import os
import sys
import re

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./sphere_calculations"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = output_buffer_read.read()

radius_1 = randint(1000,100000)/1000.0
cproc.stdin.write(str(radius_1) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

radius_2 = randint(1000, 100000)/1000.0
cproc.stdin.write(str(radius_2) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

out = filter(None, re.split("\n", out))
del out[0]
out = [re.split(":", out_element) for out_element in out]
for out_element in out :
    del out_element[0]
out = [filter(None, re.split("\s+", out_element[0])) for out_element in out]
out = [[float(out_element_element) for out_element_element in out_element] for out_element in out]
solutions_1 = sphere_calculations(radius_1)
solutions_2 = sphere_calculations(radius_2)

all_solutions_match = True
for index in range(3) :
    if abs(out[index][0] - solutions_1[index])/solutions_1[index] > TOL_RELATIVE :
        all_solutions_match = False
    if abs(out[index][1] - solutions_2[index])/solutions_2[index] > TOL_RELATIVE :
        all_solutions_match = False

if all_solutions_match :
    print "PASSED - floating-point inputs; calculated values match expected."
    sys.exit(0)
else :
    print "FAILED - calculated values did not match expected.<br>"
    print "input 1: " + str(radius_1) + "<br>"
    print "solutions 1: " + str(solutions_1) + "<br>"
    print "input 2: " + str(radius_2) + "<br>"
    print "solutions 2: " + str(solutions_2) + "<br>"
    sys.exit(1)
