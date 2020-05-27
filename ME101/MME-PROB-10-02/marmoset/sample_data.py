#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sample_data.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from shutil import copyfile
from subprocess import Popen,PIPE
from random import randint
import os
import time
import re
import sys

# copy matrix_data_1.txt to matrix_data.txt
copyfile("matrix_data_1.txt", "matrix_data.txt")

data_file = open("matrix_data_1.txt", "r")

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./transpose_matrix"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = filter(None, output_buffer_read.read().split("\n"))
out_split = [out_line.split() for out_line in out]

data_file_lines = data_file.readlines()
data_file_lines = [data_line.split() for data_line in data_file_lines]
del data_file_lines[0]
del data_file_lines[0]
data_file_lines = zip(*data_file_lines)

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

data_file.close()

output_values_expected = True;
if len(out_split) != len(data_file_lines) :
    print "FAILED - dimensions of transposed matrix do not match expected dimensions"
    sys.exit(1)
for out_line, data_line in zip(out_split, data_file_lines) :
    if len(out_line) != len(data_line) :
        print "FAILED - dimensions of transposed matrix do not match expected dimensions"
        sys.exit(1)
    for out_element, data_element in zip(out_line, data_line) :
        if out_element != data_element :
            print "FAILED - output does not match expected data element: " + data_element
            output_values_expected = False;

if output_values_expected :
    print "PASSED - matrix transposed successfully using sample data."
    sys.exit(0)
else :
    sys.exit(1)
