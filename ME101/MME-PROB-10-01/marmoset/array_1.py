#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
array_1.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import os
import time
import re
import sys

SOLUTION = [[5,3],
            [2,2],
            [1,7]]

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

row_index = 0
all_match = True;
for row in SOLUTION :
    if map(int, filter(None, re.split("\s+", split_lines[row_index]))) != row :
        print "FAILED - " + str(row) + "<br>"
        all_match = False;
    row_index = row_index + 1

if all_match :
    print "PASSED - All values for array_1 match."
    sys.exit(0)
else :
    sys.exit(1)

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")
