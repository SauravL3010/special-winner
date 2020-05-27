#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys
import os
from random import randint
from math import factorial

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

test_cases = []
for test_case_num in range(0, 5) :
    input_number = randint(1, 20)
    solution = factorial(input_number)
    test_cases.append([str(input_number), solution])

for case in test_cases :
    command_line = ["./factorial"]
    command_line.append(case[0])
    cproc=Popen(command_line, stdin=PIPE, stderr=PIPE, stdout=PIPE)
    out,err=cproc.communicate()

    result = re.findall(numeric_const_pattern, out, re.VERBOSE)
    result[0] = int(result[0])

    if result[0] != case[1] :
        print "failed - " + str(case[0]) + "!<br>"
        sys.exit(1)

    print "passed - " + str(case[0]) + "!<br>"

print "passed - all cases"
