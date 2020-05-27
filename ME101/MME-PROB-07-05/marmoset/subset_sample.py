#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
subset_sample.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import random
from check_output import *
from subprocess import Popen,PIPE
import re
import sys
import os

def randomize_input_file() :
    MINIMUM_FILE_SIZE = 10

    sorted_file = open("medal_count_2018.txt", "r")
    randomized_file = open("medal_count.txt", "w+")

    input_data = sorted_file.readlines()
    # filter out empty lines
    input_data = [input_line for input_line in input_data if len(input_line) > 3]

    print "INPUT: <br>"
    total_countries = len(input_data)
    num_countries = random.randint(MINIMUM_FILE_SIZE, len(input_data))
    while len(input_data) > (total_countries - num_countries) :
        pick_position = random.randint(0, len(input_data) - 1)
        randomized_file.write(input_data[pick_position])
        print input_data[pick_position] + " <br>"
        input_data.pop(pick_position)

    randomized_file.close()

print "Program tested using a scrambled subset of the sample input file. <br>"
randomize_input_file()

cproc=Popen("./medal_count", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

test_result = check_output(out, "medal_count.txt")

os.remove("medal_count.txt")

return_code = output_message(test_result)

exit(return_code)
