#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
target_names.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys

cproc=Popen("./coordinates_file_read", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

targets_file = open("targets.txt", "r")
output_lines = re.split("\n", out)

target_names_match = True;

# check each target name from input file has a match in console output
line_index = 0
for read_line in targets_file :
    input_line_split = re.split(" ", read_line)
    output_line_split = re.split(" ", output_lines[line_index])
    line_index = line_index + 1
    if input_line_split[0] != output_line_split[0] :
        print "FAILED - Mismatch on target name found between output and input file.<br>"
        print "Input: " + input_line_split[0] + "<br>"
        target_names_match = False;

# check that number of output lines in console output
# match number of lines in input file
while len(output_lines[-1]) == 0 :
    del output_lines[-1]
if len(output_lines) != line_index :
    print "FAILED - Number of output lines does not match number of lines in input file."
    target_names_match = False;

if target_names_match :
    print "PASSED - Output target names match file."
    sys.exit(0)
else :
    sys.exit(1)
