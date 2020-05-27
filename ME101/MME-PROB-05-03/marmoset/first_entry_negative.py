#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
first_entry_negative.py
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

negative_number_1 = randint(-100000,-1)
positive_number_1 = randint(1,100000)*2-1

input = ["./first_do_while"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
first_prompt = output_buffer_read.read()

cproc.stdin.write(str(negative_number_1) + "\n")
time.sleep(0.1)
second_prompt = output_buffer_read.read()

if first_prompt != second_prompt :
    print "FAILED - second prompt did not match first prompt."
    sys.exit(1)

cproc.stdin.write(str(positive_number_1) + "\n")
time.sleep(0.1)
first_prompt = output_buffer_read.read()

negative_number_2 = randint(-100000,-1)
positive_number_2 = randint(1,100000)*2-1

cproc.stdin.write(str(negative_number_2) + "\n")
time.sleep(0.1)
second_prompt = output_buffer_read.read()

if first_prompt != second_prompt :
    print "FAILED - second prompt did not match first prompt."
    sys.exit(1)

cproc.stdin.write(str(positive_number_2) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

found_expected_number = re.search(str(positive_number_1+positive_number_2), out)

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

if found_expected_number :
    print "PASSED - First entry is negative."
    sys.exit(0)
else :
    print "FAILED - Did not find expected number."
    print "first number: " + str(first_number)
    print "second number: " + str(second_number)
    sys.exit(1)
