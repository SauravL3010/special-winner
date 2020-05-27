#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
prompt.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys
import time

overall_pass = True;

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./read_and_print"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.01)
out = output_buffer_read.read()

match_expected_prompt_1 = re.search("(?i)enter", out)

if match_expected_prompt_1 :
    print "passed - Program prompts for user the to enter an integer. <br>"
else :
    print "failed - Did not detect prompt from program for user to enter an integer. Looking for keyword 'enter'."
    overall_pass = False;

cproc.stdin.write("42\n")
time.sleep(0.01)
out = output_buffer_read.read()

match_expected_prompt_2 = re.search(":", out)

if match_expected_prompt_2 :
    print "passed - Program includes prompt before outputting number."
else :
    print "failed - Did not detect prompt from program before outputting number. Look for a colon ':'."
    overall_pass = False;

if overall_pass :
    sys.exit(0)
else :
    sys.exit(1)
