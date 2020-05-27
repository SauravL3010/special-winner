#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
quantity_of_numbers.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
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

starting_number = randint(1,100)

cproc.stdin.write(str(starting_number) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

ending_number = randint(101,200)

cproc.stdin.write(str(ending_number) + "\n")
time.sleep(0.1)
out = output_buffer_read.read()

find_numbers = re.split("[\s]+", out)
for number in find_numbers :
    if len(number) < 1 :
        find_numbers.remove(number)

output_buffer_write.close()
output_buffer_read.close()
os.remove("out_buffer")

if len(find_numbers) == ending_number - starting_number + 1 :
    print "PASSED - Quantity of numbers outputted."
    sys.exit(0)
elif len(find_numbers) > ending_number - starting_number + 1 :
    print "FAILED - Too many numbers detected."
    sys.exit(1)
else :
    print "FAILED - Too few numbers detected."
    sys.exit(1)
