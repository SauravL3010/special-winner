#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys

cproc=Popen(["./steel_MSDS"], stdin=PIPE, stderr=PIPE, stdout=PIPE)
input = "9994 Cold Rolled Sheet Steel 2 2 1 95 2.225 0.65 0.25".encode('utf8')
out,err=cproc.communicate(input)
out = out.decode('utf8')
err = err.decode('utf8')

fields = ["SDS ID No.:",
          "Product Identifier:",
          "Carcinogenity:",
          "STOT Repeat Exposure:",
          "Composition \(\% weight\)\:",
          "Iron:",
          "Manganese:",
          "Chromium:",
          "Nickel:"]

matches = []
for field in fields :
    matches.append(re.search(field, out))

for match_num in range(len(matches)) :
    if not matches[match_num] :
        print("FAILED - input field heading not found: <br>")
        print(fields[match_num])
        sys.exit(1)

print("PASSED - all defined headings for input fields found <br>")
sys.exit(0)
