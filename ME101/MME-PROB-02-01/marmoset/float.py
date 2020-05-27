#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
three_digit_int.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import re
import sys
import time

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./read_and_print"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)

time.sleep(0.01)
# discard initial prompt
output_buffer_read.read()

generate_integer = randint(1000,9999);
input_float = generate_integer / 100.0;

cproc.stdin.write(str(input_float) + "\n")

time.sleep(0.01)
out = output_buffer_read.read()

parse_output = re.split(":", out)
parse_output2 = parse_output[1].strip()
regex_string = "^" + str(int(input_float)) + "$"
match_number = re.match(regex_string,parse_output2)

if match_number:
    print "passed - Program is reading input as integer.<br>"
    print "         Inputted: " + str(input_float) + "<br>"
    print "         Outputted: " + out + "<br>"
    sys.exit(0)
else :
    print "failed - Inputted " + str(input_float) + ". Did not find expected output.<br>"
    print "         Program is likely reading and storing input as a<br>"
    print "         floating point number, instead of an integer.<br>"
    sys.exit(1)
