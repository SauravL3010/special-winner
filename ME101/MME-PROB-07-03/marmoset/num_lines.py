#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
num_lines.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from shutil import copyfile
from subprocess import Popen,PIPE
from random import randint
from calc_coordinates import calc_coordinates
import re
import sys

copyfile("drone_directions_backup.txt", "drone_directions.txt")

# add random number of lines to the input file
num_additional_lines = randint(1, 20)

input_file = open("drone_directions.txt", "a")

for line_number in range(0, num_additional_lines) :
    distance = randint(100,9999) / 100.0
    heading = randint(0, 36000) / 100.0 - 180.0;
    input_file.write(str(distance) + " " + str(heading) + "\n")

input_file.close()

canonical_coordinates = calc_coordinates()
cproc=Popen("./coordinate_tracking", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

output_lines = re.split("\n", out)
while len(output_lines[-1]) <= 1 :
    del output_lines[-1]

if len(canonical_coordinates) == len(output_lines) :
    print "PASSED - Number of output lines matches input file."
    sys.exit(0)
else :
    print "FAILED - Number of output lines do not match input file.<br>"
    print "Number of output lines: " + str(len(output_lines)) + " <br>"
    print "Number of input lines: " + str(len(canonical_coordinates)) + " <br>"
    sys.exit(1)
