#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
negative_int.py
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

input_number = 0 - randint(100,999)
cproc.stdin.write(str(input_number) + "\n")

time.sleep(0.01)
out = output_buffer_read.read()

parse_output = re.split(":", out)
parse_output2 = parse_output[1].strip()
regex_string = "^" + str(input_number) + "$"
match_number = re.match(regex_string,parse_output2)

if match_number:
    print "passed - Inputted " + str(input_number) + ". Outputted " + str(input_number) + "."
    sys.exit(0)
else :
    print "failed - Inputted " + str(input_number) + ". Did not find expected output."
    sys.exit(1)
