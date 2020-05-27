#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
max_size.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from gen_message import gen_message
from subprocess import Popen,PIPE
import time
import os
import sys

MESSAGE = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. In " +
        "rutrum enim nisl, sit amet consequat purus hendrerit in. Integer " +
        "bibendum, nisi sed molestie blandit, justo metus vestibulum lorem, " +
        "sed cursus risus ex facilisis lorem. Pellentesque habitant morbi " +
        "tristique senectus et netus et malesuada fames ac turpis egestas. " +
        "Duis dignissim nec risus id vehicula. Nunc rutrum velit et orci " +
        "ornare aliquam. Vestibulum ante ipsum primis in faucibus orci " +
        "luctus et ultrices posuere cubilia Curae; Phasellus sodales sit " +
        "amet velit non ultricies. Nulla non arcu semper, pharetra urna sed, " +
        "dictum nibh. Nunc venenatis non est quis bibendum. Mauris " +
        "pellentesque sollicitudin posuere.")
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
    print "PASSED - max message size."
    sys.exit(0)
else :
    print "FAILED - max message size."
    sys.exit(1)
