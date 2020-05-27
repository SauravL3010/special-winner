#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
many_invalids.py
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

num_invalids_1 = randint(50,100)

input = ["./first_do_while"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
original_prompt_1 = output_buffer_read.read()

for entry_number in range(num_invalids_1) :
    # print "1 - " + str(entry_number)
    invalid_number = 1
    while invalid_number % 2 == 1 and invalid_number > 0 :
        invalid_number = randint(-500000,500000)

    cproc.stdin.write(str(invalid_number) + "\n")
    time.sleep(0.1)
    repeat_prompt = output_buffer_read.read()

    if repeat_prompt != original_prompt_1 :
        print "FAILED - repeat prompt did not match original prompt."
        sys.exit(1)

odd_number_1 = randint(1,100000)*2-1
cproc.stdin.write(str(odd_number_1) + "\n")
time.sleep(0.1)
original_prompt_2 = output_buffer_read.read()

num_invalids_2 = randint(50,100)

for entry_number in range(num_invalids_2) :
    # print "2 - " + str(entry_number)
    invalid_number = 1
    while invalid_number % 2 == 1 and invalid_number > 0 :
        invalid_number = randint(-500000,500000)

    cproc.stdin.write(str(invalid_number) + "\n")
    time.sleep(0.1)
    repeat_prompt = output_buffer_read.read()

    if repeat_prompt != original_prompt_2 :
        print "FAILED - repeat prompt did not match original prompt."
        sys.exit(1)

odd_number_2 = randint(1,100000)*2-1
cproc.stdin.write(str(odd_number_2) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

found_expected_number = re.search(str(odd_number_1+odd_number_2), out)

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

if found_expected_number :
    print "PASSED - Many invalid entries."
    sys.exit(0)
else :
    print "FAILED - Did not find expected number."
    print "first number: " + str(first_number)
    print "second number: " + str(second_number)
    sys.exit(1)
