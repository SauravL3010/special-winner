#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
square.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from shutil import copyfile
from subprocess import Popen,PIPE
from random import randint
import os
import time
import re
import sys

matrix_size = randint(5,20)
data_matrix = [[randint(1,100) for col in range(matrix_size)] for row in range(matrix_size)]

create_data_file = open("matrix_data.txt", "w")
create_data_file.write(str(matrix_size) + "\n")
create_data_file.write(str(matrix_size) + "\n")
for row in data_matrix :
    for col in row :
        create_data_file.write(str(col) + " ")
    create_data_file.write("\n")
create_data_file.close()

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./transpose_matrix"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = filter(None, output_buffer_read.read().split("\n"))
out_split = [[int(element) for element in out_line.split()] for out_line in out]

data_matrix = zip(*data_matrix)
out_split = [tuple(row) for row in out_split]

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

if data_matrix == out_split :
    print "PASSED - successful transpose of square matrix"
    sys.exit(0)
else :
    print "FAILED - output does not match for square matrix<br>"
    for row in data_matrix :
        print str(row) + "<br>"
    sys.exit(1)
