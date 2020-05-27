#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
qty_output_lines.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from run_submission import run_submission

submission_output = run_submission("12345678")
if len(submission_output) < 6 :
    print("FAILED - output contains fewer than 6 lines <br>")
    exit(1)
elif len(submission_output) > 6 :
    print("FAILED - output contains more than 6 lines <br>")
    exit(1)
else :
    print("PASSED - output contains 6 lines <br>")
    exit(0)
