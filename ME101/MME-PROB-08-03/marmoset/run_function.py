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

test_cases = [["5", 120],
              ["1", 1],
              ["11", 39916800],
              ["0", 1],
              ["20", 2432902008176640000]]

for case in test_cases :
    command_line = ["./factorial"]
    command_line.append(case[0])
    cproc=Popen(command_line, stdin=PIPE, stderr=PIPE, stdout=PIPE)
    out,err=cproc.communicate()

    result = re.findall(numeric_const_pattern, out, re.VERBOSE)
    result[0] = int(result[0])

    if result[0] != case[1] :
        print "failed - " + str(case[0]) + "!"
        sys.exit(1)

    print "passed - " + str(case[0]) + "!"

print "passed - all cases"
