#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
distances.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

SOLUTION_TOLERANCE = 0.01

from subprocess import Popen,PIPE
import re
import math
import sys

cproc=Popen("./coordinates_file_read", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()
output_lines = re.split("\n", out)
while len(output_lines[-1]) == 0 :
    del output_lines[-1]

targets_file = open("targets.txt", "r")

input_lines = []
for read_line in targets_file :
    input_lines.append(read_line.strip())

if len(input_lines) != len(output_lines) :
    print "FAILED - Number of output lines does not match number of lines in input file."
    sys.exit(1)

for line_number in range(len(input_lines)) :
    input_line_split = re.split(" ", input_lines[line_number])
    output_line_split = re.split(" ", output_lines[line_number])

    if len(output_line_split) != 3 :
        print "FAILED - Did not find three output fields.<br>"
        print output_line_split
        sys.exit(1)

    coordinate_x = float(input_line_split[1])
    coordinate_y = float(input_line_split[2])

    distance = math.sqrt(coordinate_x * coordinate_x + coordinate_y * coordinate_y)

    if abs(distance - float(output_line_split[1])) > SOLUTION_TOLERANCE :
        print "FAILED - Calculated distance not accurate.<br>"
        print "input: " + read_line
        sys.exit(1)

print "PASSED - Distances calculated correctly."
sys.exit(0)
