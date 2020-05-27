#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
on_exact.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import time
from above_or_below import above_or_below, check_output
import sys

overall_pass = True;

for run_number in range(5) :
    output_buffer_write = open("out_buffer", "wb+")
    output_buffer_read = open("out_buffer", "rU")

    input = ["./above_or_below"]
    cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
    time.sleep(0.01)
    out = output_buffer_read.read()

    x_coordinate = randint(-1000000, 1000000) / 1000.0
    y_coordinate = x_coordinate
    canonical_result = above_or_below(x_coordinate, y_coordinate)

    cproc.stdin.write(str(x_coordinate) + " " + str(y_coordinate) + "\n")
    time.sleep(0.01)
    out = output_buffer_read.read()

    check_result = check_output(out, canonical_result, x_coordinate, y_coordinate)

    if check_result != 0 :
        overall_pass = False

    cproc.terminate()
    cproc.wait()
    output_buffer_read.close()
    output_buffer_write.close()

if overall_pass :
    sys.exit(0)
else :
    sys.exit(1)
