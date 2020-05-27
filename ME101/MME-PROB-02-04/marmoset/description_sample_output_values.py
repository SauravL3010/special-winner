#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys

cproc=Popen("./steel_MSDS", stdin=PIPE, stderr=PIPE, stdout=PIPE)
input = "9994 Cold Rolled Sheet Steel 2 2 1 95 2.225 0.65 0.25".encode('utf8')
out,err=cproc.communicate(input)
out = out.decode('utf8')
err = err.decode('utf8')

output_values = ["9994",
                 r"Cold[ ]Rolled[ ]Sheet[ ]Steel",
                 "2-2-1",
                 r"95\s+2\.225\s+0\.65\s+0\.25"]

for check_value in range(len(output_values)) :
    if not re.search(output_values[check_value], out, re.VERBOSE) :
        print("FAILED - input value not found in output: <br>")
        print(output_values[check_value])
        sys.exit(1)

print("PASSED - all expected output values found <br>")
sys.exit(0)
