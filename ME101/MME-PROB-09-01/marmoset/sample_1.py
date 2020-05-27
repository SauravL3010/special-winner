#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sample_1.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from run_find_slope import run_find_slope
import sys

SOLUTION_TOLERANCE = 0.01

numeric_const_pattern = r"""
    \s*
    [-+]? # optional sign
    (?:
        (?: \d* \. \d+ ) # .1 .12 .123 etc 9.1 etc 98.1 etc
        |
        (?: \d+ \.? ) # 1. 12. 123. etc 1 12 123 etc
    )
    # followed by optional exponent part if desired
    (?: [Ee] [+-]? \d+ ) ?
    """

canonical_result = run_find_slope("./canonical_finding_slope", 1)
student_result = run_find_slope("./finding_slope", 1)

if len(canonical_result) != len(student_result) :
    print "FAILED - Number of values outputted does not match expected output."
    print canonical_result
    print student_result
    sys.exit(1)
else :
    for check_results_index in range(len(canonical_result)) :
        if abs(student_result[check_results_index] - canonical_result[check_results_index]) > SOLUTION_TOLERANCE :
            print "FAILED - Value outputted does not match expected<br>"
            print "output for first sample case.<br>"
            print "Value outputted: " + str(student_result[check_results_index])
            sys.exit(1)

print "PASSED - Output matches sample case 1."
sys.exit(0)
