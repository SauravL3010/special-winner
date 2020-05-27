#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
16_digits.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from run_submission import run_canonical, run_submission

LINE_NUMBER = 3

input_file = open("input_strings.txt", "r")

for line in input_file :
    canonical_result = run_canonical(line.strip())
    submission_result = run_submission(line.strip())

    submission_matches = True
    if (submission_result[LINE_NUMBER - 1][:13] == canonical_result[LINE_NUMBER - 1][:13]) :
        print("PASSED - line " + str(LINE_NUMBER) + " output: " + submission_result[LINE_NUMBER - 1] + " <br>")
    else :
        print("FAILED - line " + str(LINE_NUMBER) + " does not match expected output for input: " + line.strip() + " <br>")
        exit(1)

print("PASSED - line " + str(LINE_NUMBER) + " output good for all inputs <br>")
exit(0)
