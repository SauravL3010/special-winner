#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
prompt.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import os
import time
import re
import sys

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./counting_up"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = output_buffer_read.read()

match_enter = re.search("enter", out, re.IGNORECASE)

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

if match_enter :
    print "PASSED - Prompted for input using keyword 'enter'."
    sys.exit(0)
else :
    print "FAILED - Did not detect prompt for input. Keyword 'etner'."
    sys.exit(1)
