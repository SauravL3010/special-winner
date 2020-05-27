#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
edge_case_0.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import time
import os
import sys
import re

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./binary_conversion"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = output_buffer_read.read()

cproc.stdin.write("0\n")
time.sleep(0.1)
out = output_buffer_read.read()
count_zeroes = len(re.findall("0", out, re.VERBOSE))
count_ones = len(re.findall("1", out, re.VERBOSE))

if (count_zeroes < 1 or count_ones != 0) :
    print "failed - did not find expected binary string in output"
    exit(1)

print "passed"
exit(0)
