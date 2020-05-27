#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
test_read_file.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re

input = ["./test_read_file"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True)
out,err = cproc.communicate()

output_lines = re.split("\n", out)
output_lines = [re.split("\s+", output_line) for output_line in output_lines if output_line]
output_lines = [[int(element) for element in output_line if element] for output_line in output_lines]

test_file = open("potholes_read_file.txt", "r")
test_file_lines = re.split("\n", test_file.read())
test_file_lines = [re.split("\s+",test_file_line) for test_file_line in test_file_lines if test_file_line]
test_file_lines = [[int(element) for element in test_file_line]  for test_file_line in test_file_lines]

all_elements_found = True
for test_file_line in test_file_lines :
    if not (test_file_line in output_lines) :
        all_elements_found = False

if not all_elements_found :
    # check if index order was swapped in the function
    swap_index_lines = test_file_lines.copy()
    swap_index_lines = [[swap_index_element[1], swap_index_element[0], swap_index_element[2]] for swap_index_element in swap_index_lines]

    suspected_swap_index = True
    for swap_index_line in swap_index_lines :
        if not (swap_index_line in output_lines) :
            suspected_swap_index = False

    if suspected_swap_index :
        print("It is suspected that the 2D array has put the avenue index first and the street index second. <br>")
        print("The problem description specifies that the street index needs to be first for this test to run. <br>")

if all_elements_found :
    print("PASSED <br>")
    print("read_file() function successfully reads potholes data file into 2D array. <br>")
    exit(0)
else :
    print("FAILED <br>")
    print("Error detected with read_file() function. Unsuccessful file read into 2D array. <br>")
    exit(1)
