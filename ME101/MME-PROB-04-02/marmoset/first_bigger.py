#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
one_is_bigger.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import time
import sys
from bigger_or_smaller import bigger_or_smaller, check_output

# first is bigger
output_buffer_write = open("out_buffer", "wb+")
output_buffer_read = open("out_buffer", "rU")

input = ["./bigger_or_smaller"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=output_buffer_write, stderr=PIPE, bufsize=1, universal_newlines=True)
time.sleep(0.01)
out = output_buffer_read.read()

first_number = randint(-1000000, 1000000)
second_number = first_number - randint(1, 1000000)
canonical_result = bigger_or_smaller(first_number, second_number)

cproc.stdin.write(str(first_number) + " " + str(second_number) + "\n")
time.sleep(0.01)
out = output_buffer_read.read()

check_result = check_output(out, canonical_result, first_number, second_number)

cproc.terminate()
cproc.wait()
output_buffer_read.close()
output_buffer_write.close()

if check_result != 0 :
    sys.exit(1)
else :
    print "PASSED - first is larger"
    sys.exit(0)
