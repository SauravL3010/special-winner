#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
randomize.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

SOLUTION_TOLERANCE = 0.001

from shutil import copyfile
from subprocess import Popen,PIPE
from random import randint
from calc_coordinates import calc_coordinates
import re
import sys

coordinates_match = True;

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

out_split = re.split("\n", out)
while len(out_split[-1]) <= 1 :
    del out_split[-1]

out_split = re.split("\n", out)
out_split = [re.split(",", out_split_element) for out_split_element in out_split]
# remove elements created by empty lines in output
while len(out_split[-1]) <= 1 :
    del out_split[-1]
for out_split_element in out_split:
    for element_index in range(0,2) :
        out_split_element[element_index] = re.sub("[\(\)]", "", out_split_element[element_index])
        out_split_element[element_index] = float(out_split_element[element_index])

for canonical_coordinate,out_coordinate in zip(canonical_coordinates, out_split) :
    # if abs(canonical_coordinates[coordinate_index] - out_split)
    for element_index in range(0,2) :
        if abs(canonical_coordinate[element_index] - out_coordinate[element_index]) > SOLUTION_TOLERANCE :
            print "FAILED - Output coordinate not correct.<br>"
            print "element index: " + str(element_index) + "<br>"
            print "output received: " + str(out_coordinate)
            print
            coordinates_match = False;

if coordinates_match :
    print "PASSED - Output coordinates match sample output from problem description."
    sys.exit(0)
else :
    sys.exit(1)
