#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
randomize_0_255.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import time
import os
import sys
import re

def convert_to_binary(decimal_to_convert) :
    binary_string = ""
    working_decimal = decimal_to_convert

    while (working_decimal > 0) :
        next_binary_digit = str(working_decimal % 2)
        binary_string = binary_string + next_binary_digit
        working_decimal = working_decimal / 2

    # reverse the string before returning
    return binary_string[::-1]

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

for test_run_number in range(0, 3):
    input = ["./binary_conversion"]
    cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
    time.sleep(0.1)
    out = output_buffer_read.read()

    test_input = randint(0, 255)
    binary_solution = convert_to_binary(test_input)
    print "input value: " + str(test_input)

    cproc.stdin.write(str(test_input) + "\n")
    time.sleep(0.1)
    out = output_buffer_read.read()
    find_binary_numbers = re.findall("[01]+", out, re.VERBOSE)

    if (len(find_binary_numbers) > 1) :
        print "failed - too many binary numbers in output"
        exit(1)
    elif (len(find_binary_numbers) < 1) :
        print "failed - did not find any binary numbers in output"
        exit(1)

    confirm_decimal_value = 0
    for binary_digit in range(len(find_binary_numbers[0])-1, -1, -1):
        confirm_decimal_value = confirm_decimal_value + int(find_binary_numbers[0][binary_digit])*2**(7-binary_digit)

    if (confirm_decimal_value != test_input) :
        print "failed - outputed binary value does not match input value"
        exit(1)

print "passed"
exit(0)
