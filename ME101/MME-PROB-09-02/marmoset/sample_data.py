#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sample_data.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from gen_message import gen_message
from subprocess import Popen,PIPE
import time
import os
import sys

MESSAGE = "The journey of a thousand miles begins with a single step."
gen_message(MESSAGE)

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./secret_message"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = output_buffer_read.read().strip()

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

if out == MESSAGE :
    print "PASSED - same as Problem Description."
    sys.exit(0)
else :
    print "FAILED - same as Problem Description."
    sys.exit(1)
