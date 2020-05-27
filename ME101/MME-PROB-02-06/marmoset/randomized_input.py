#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
randomized_input.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import random
from run_balance_1 import *

print "10 randomized test cases"
print

for run_number in range(10) :
    print "Random test number: " + str(run_number + 1)

    weight_david = random.randint(50, 100)
    weight_daughter = random.randint(15, 40)

    print "Input > <br>"
    print "daughter's weight: " + str(weight_daughter) + " <br>"
    print "David's weight : " + str(weight_david) + " <br>"

    result = run_Balance(weight_daughter, weight_david)

    if len(result) > 2 :
        print "FAILED - too many numbers found in output"
        exit(1)

    if len(result) < 1 :
        print "FAILED - too few numbers found in output"
        exit(1)

    found_expected_result = False

    balance_distance = 1.6 * weight_daughter / weight_david

    for check_result in result :
        if abs(check_result - balance_distance) < 0.01 :
            found_expected_result = True

    if found_expected_result == False :
        print "FAILED - Outputted value did not match expected value. Expected output to be between " \
            + str.format("{:.3f}", balance_distance - 0.01) + " and " \
            + str.format("{:.3f}", balance_distance + 0.01) + ". <br>"
        exit(1)

    print "PASSED - Outputted value within expected range of " \
        + str.format("{:.3f}", balance_distance - 0.01) + " and " \
        + str.format("{:.3f}", balance_distance + 0.01) + ". <br><br>"
    print

exit(0)
