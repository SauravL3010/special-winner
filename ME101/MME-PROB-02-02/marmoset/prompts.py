#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
prompts.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import time
import os
import sys
import re

KEYWORDS = ["enter", "radius", "yard"]

output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./sphere_calculations"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.1)
prompt_1 = output_buffer_read.read()

cproc.stdin.write("1\n")
time.sleep(0.1)
prompt_2 = output_buffer_read.read()

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

keywords_found = True

for keyword in KEYWORDS :
    if not re.search(keyword, prompt_1, re.IGNORECASE) :
        print "FAILED - keyword not found in first prompt: " + keyword + "<br>"
        keywords_found = False
for keyword in KEYWORDS :
    if not re.search(keyword, prompt_2, re.IGNORECASE) :
        print "FAILED - keyword not found in second prompt: " + keyword + "<br>"
        keywords_found = False

if keywords_found :
    print "PASSED - all expected keywords found in prompts"
    sys.exit(0)
else :
    sys.exit(1)
