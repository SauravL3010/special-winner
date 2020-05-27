#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys
import os

SOLUTION_TOLERANCE = 0.001
COMPILE_SUCCESSFUL_FILE = "compile_successful.txt"

if not os.path.exists(COMPILE_SUCCESSFUL_FILE) :
    print "failed - did not compile successfully"
    sys.exit(1)

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

test_cases = [["20",4.07886],
              ["0.1", 0.0203943],
              ["0.0001", 2.03943e-05],
              ["343", 69.9525],
              ["299792458", 61140600]]

for case in test_cases :
    command_line = ["./time_of_flight"]
    input = case[0]
    cproc=Popen(command_line, stdin=PIPE, stderr=PIPE, stdout=PIPE)
    out,err=cproc.communicate(input)

    result = re.findall(numeric_const_pattern, out, re.VERBOSE)
    result[0] = float(result[0])

    if abs(result[0] - case[1]) > abs(case[1] * SOLUTION_TOLERANCE):
        print "FAILED - " + str(case[0]) + " [m/s]<br>"
        sys.exit(3)

    print "PASSED - " + str(case[0]) + " [m/s]<br>"

print "PASSED - all cases"
