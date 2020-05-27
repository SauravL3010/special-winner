#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
run_find_slope.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

# reference: http://newbebweb.blogspot.ca/2012/02/python-head-ioerror-errno-32-broken.html
# prevents "IOError: [Errno 32] Broken pipe"
from signal import signal, SIGPIPE, SIG_DFL, SIG_IGN

from subprocess import Popen,PIPE
import time
import re
import sys

numeric_const_pattern = r"""
    \s*
    [-+]? # optional sign
    (?:
        (?: \d* \. \d+ ) # .1 .12 .123 etc 9.1 etc 98.1 etc
        |
        (?: \d+ \.? ) # 1. 12. 123. etc 1 12 123 etc
    )
    # followed by optional exponent part if desired
    (?: [Ee] [+-]? \d+ ) ?
    """

def run_find_slope(program_file_name, location_value) :
    # signal(SIGPIPE,SIG_DFL)

    parsed_output = []

    # output_buffer_write = open("out_buffer", "wb+")
    # output_buffer_read = open("out_buffer", "rU")
    output_buffer_write = open("out_buffer", "w")
    output_buffer_read = open("out_buffer", "r")

    input = [program_file_name]
    # cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
    cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=output_buffer_write)
    time.sleep(0.05)
    out = output_buffer_read.read()

    cproc.stdin.write(str(location_value) + "\n")
    time.sleep(0.05)
    out = output_buffer_read.read()

    parsed_output = re.findall(numeric_const_pattern, out, re.VERBOSE)

    for result_index in range(len(parsed_output)) :
        parsed_output[result_index] = float(parsed_output[result_index])

    output_buffer_write.close()
    output_buffer_read.close()

    return parsed_output
