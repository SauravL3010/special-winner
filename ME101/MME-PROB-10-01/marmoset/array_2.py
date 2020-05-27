#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
array_2.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import os
import time
import re
import sys

SOLUTION = [[3.2, -1.7, 3.6, 1.2, -0.6, 8.0, -7.7],
    [-0.8, 1.1, 2.3, 2.3, -4.8, 8.0, -1.2],
    [1.2, 3.3, 6.8, -2.1, 0.0, 2.3, -8.0],
    [4.2, 5.7, 3.3, -9.0, -8.0, -3.3, 2.2],
    [0.9, 5.7, 3.2, -8.9, 8.0, -8.0, -7.7]]
TOLERANCE = 1e-6

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

row_index = 3
all_match = True;
for row in SOLUTION :
    element_index = 0
    split_row = filter(None, re.split("\s+" ,split_lines[row_index]))
    for element in row :
        if abs(float(split_row[element_index]) - element) > TOLERANCE :
            print "FAILED - " + str(element) + "<br>"
            all_match = False;
        element_index = element_index + 1
    row_index = row_index + 1

if all_match :
    print "PASSED - All values for array_2 match."
    sys.exit(0)
else :
    sys.exit(1)

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")
