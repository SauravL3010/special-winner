#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
specified_input_2.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from run_balance_1 import *

print "Input > <br>"
print "daughter's weight: 32 <br>"
print "David's weight : 73 <br>"

result = run_Balance(32, 73)

if len(result) > 2 :
    print "FAILED - too many numbers found in output <br>"
    print result
    exit(1)

if len(result) < 1 :
    print "FAILED - too few numbers found in output"
    exit(1)

found_expected_result = False;
for check_result in result :
    if (0.69 < check_result and check_result < 0.71) :
        found_expected_result = True;

if found_expected_result == False :
    print "FAILED - Outputted value did not match expected value. Expected output to be between 0.69 and 0.71."
    exit(1)

print "PASSED - Outputted value within expected range of 0.69 to 0.71."
exit(0)
