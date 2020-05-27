#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
colons.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import time
import os
import sys
import re

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./sphere_calculations"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
out = output_buffer_read.read()

cproc.stdin.write("1\n")
time.sleep(0.1)
out = output_buffer_read.read()

cproc.stdin.write("2\n")
time.sleep(0.1)
out = output_buffer_read.read()

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

if len(re.findall(":", out)) < 3 :
    print "FAILED - output formatting<br>"
    print "colons expected after row headings"
    sys.exit(1)
else :
    print "PASSED - output formatting"
    sys.exit(0)
