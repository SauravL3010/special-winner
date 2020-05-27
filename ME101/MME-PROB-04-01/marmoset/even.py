#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
even.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import re
import sys
import time

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./even_or_odd"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)

time.sleep(0.01)
# discard initial prompt
output_buffer_read.read()

input_number = randint(100,999)
while input_number % 2 != 0 :
    input_number = randint(100,999)

cproc.stdin.write(str(input_number) + "\n")

time.sleep(0.01)
out = output_buffer_read.read()

match_odd = re.search("(?i)odd", out)
match_even = re.search("(?i)even", out)

overall_pass = True;

if match_odd :
    overall_pass = False;
    print "Found unexpected output keyword 'odd'.<br>"

if not match_even :
    overall_pass = False;
    print "Did not find output keyword 'even'.<br>"

if overall_pass :
    print "passed - Detected even number successfully."
    sys.exit(0)
else :
    print "failed - Did not detect even number successfully.<br>"
    print "         Input: " + str(input_number)
    sys.exit(1)
