#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
all_valid.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import time
import os
import re
import sys

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

first_number = randint(1,100000)*2-1
second_number = randint(1,1000000)*2-1

input = ["./first_do_while"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = output_buffer_read.read()

cproc.stdin.write(str(first_number) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

cproc.stdin.write(str(second_number) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

found_expected_number = re.search(str(first_number+second_number), out)

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

if found_expected_number :
    print "PASSED - No invalid numbers inputted."
    sys.exit(0)
else :
    print "FAILED - Did not find expected number."
    print "first number: " + str(first_number)
    print "second number: " + str(second_number)
    sys.exit(1)
