#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
test_repair_volume.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import random
from subprocess import Popen,PIPE
from pothole_map import pothole_map

CORRECTNESS_TOLERANCE = 1e-4

MIN_TEST_ROADS = 5
MAX_TEST_ROADS = 10

def gen_test_sequence() :
    return_repair_volumes = []

    the_map = pothole_map()
    test_sequence_file = open("test_repair_volume.txt", "w+")

    random.seed()

    print "Test Sequence: <br>"
    qty_test_roads = random.randint(MIN_TEST_ROADS, MAX_TEST_ROADS)
    for test_road_num in range(qty_test_roads) :
        if random.randint(0,1) == 0 :
            test_sequence_file.write("S ")
            road_number = random.randint(1, the_map.QTY_STREET)
            return_repair_volumes.append(the_map.volume_repair("street", road_number))
            print "Street " + str(road_number) + " <br>"
        else :
            test_sequence_file.write("A ")
            road_number = random.randint(1, the_map.QTY_AVENUE)
            return_repair_volumes.append(the_map.volume_repair("avenue", road_number))
            print "Avenue " + str(road_number) + " <br>"
        test_sequence_file.write(str(road_number)+"\n")
    test_sequence_file.close()

    return return_repair_volumes


def run_submission() :
    input = ["./test_repair_volume"]
    cproc=Popen(input, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True)
    out,err = cproc.communicate()

    output_lines = re.split("\n", out)
    output_lines = [float(output_element) for output_element in output_lines if output_element]

    return output_lines



canonical_repair_volumes = gen_test_sequence()
submission_output_values = run_submission()

all_outputs_correct = True
for check_output_num in range(len(canonical_repair_volumes)) :
    if (abs(canonical_repair_volumes[check_output_num] - submission_output_values[check_output_num]) > CORRECTNESS_TOLERANCE) :
        print "Did not find expected output for test case " + str(check_output_num)
        all_outputs_correct = False

print "<br>"
if all_outputs_correct :
    print "PASSED <br>"
    print "repair_volume() function works as defined. <br>"
    exit(0)
else :
    print "FAILED <br>"
    print "repair_volume() function does not work as defined. <br>"
    exit(1)
