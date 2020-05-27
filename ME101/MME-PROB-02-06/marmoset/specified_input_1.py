#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
specified_input_1.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from run_balance_1 import *

print "Input > <br>"
print "daughter's weight: 20 <br>"
print "David's weight : 60 <br>"

result = run_Balance(20, 60)

if len(result) > 2 :
    print "FAILED - too many numbers found in output <br>"
    print result
    exit(1)

if len(result) < 1 :
    print "FAILED - too few numbers found in output"
    exit(1)

found_expected_result = False
for check_result in result :
    if (0.52 < check_result and check_result < 0.54) :
        found_expected_result = True

if found_expected_result == False :
    print "FAILED - Outputted value did not match expected value. Expected output to be between 0.52 and 0.54."
    exit(1)

print "PASSED - Outputted value within expected range of 0.52 to 0.54."
exit(0)
