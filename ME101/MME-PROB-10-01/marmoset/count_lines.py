#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
count_lines.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import os
import time
import re
import sys

EXPECTED_OUTPUT_LINES = 11;

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./2D_print"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = output_buffer_read.read()

split_lines = re.split("\n",out)
found_empty_line = True;
while found_empty_line :
    found_empty_line = False;
    for line in split_lines :
        if len(line) < 1 :
            split_lines.remove(line)
            found_empty_line = True;

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

if len(split_lines) != EXPECTED_OUTPUT_LINES :
    print "FAILED - Number of (non-empty) lines expected: " + str(EXPECTED_OUTPUT_LINES) + "<br>"
    print "Number of (non-empty) lines detected: " + str(len(split_lines))
    sys.exit(1)
else :
    print "PASSED - " + str(EXPECTED_OUTPUT_LINES) + " output lines detected."
    sys.exit(0)
