#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sample_input.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

SOLUTION_TOLERANCE = 0.001

from calc_coordinates import calc_coordinates
from subprocess import Popen,PIPE
import re
import sys

coordinates_match = True;

canonical_coordinates = calc_coordinates()

cproc=Popen("./coordinate_tracking", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

out_split = re.split("\n", out)
out_split = [re.split(",", out_split_element) for out_split_element in out_split]
# remove elements created by empty lines in output
while len(out_split[-1]) <= 1 :
    del out_split[-1]
for out_split_element in out_split:
    for element_index in range(0,2) :
        out_split_element[element_index] = re.sub("[\(\)]", "", out_split_element[element_index])
        out_split_element[element_index] = float(out_split_element[element_index])

# check first three coordinates from output match expected values
for coordinate_index in range(0,3) :
    canonical_coordinate = canonical_coordinates[coordinate_index]
    out_coordinate = out_split[coordinate_index]
    for element_index in range(0,2) :
        if abs(canonical_coordinate[element_index] - out_coordinate[element_index]) > SOLUTION_TOLERANCE :
            print "FAILED - Output coordinate not correct.<br>"
            print "coordinate index: " + str(coordinate_index)
            print "element index: " + str(element_index)
            print "output received: " + str(out_coordinate)
            print
            coordinates_match = False;

if coordinates_match :
    print "PASSED - Output coordinates match sample output from problem description."
    sys.exit(0)
else :
    sys.exit(1)
