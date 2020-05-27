#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys

cproc=Popen("./steel_MSDS", stdin=PIPE, stderr=PIPE, stdout=PIPE)
input = "9996 Pre Painted Sheet Steel 2 2 1 95.1 2.225 0.65 0.25".encode('utf8')
out,err=cproc.communicate(input)
out = out.decode('utf8')
err = err.decode('utf8')

total_match = re.search(r"""
    \s*SDS:\s*9996\s+Identifier:\s*Pre[ ]Painted[ ]Sheet[ ]Steel\s*$
    \s*Hazard:\s*2-2-1\s*$
    \s*Composition:\s*$
    \s*Fe\s+Mn\s+Cr\s+Ni\s*$
    \s*95.1\s+2.225\s+0.65\s+0.25\s*$
    """, out, re.MULTILINE|re.VERBOSE)

if not total_match :
    print("FAILED - did not match expected output <br>")
    print("expected output: <br>")
    print("SDS: 9996    Identified: Pre Painted Sheet Steel <br>")
    print("Hazard: 2-2-1 <br>")
    print("Composition: <br>")
    print("Fe     Mn      Cr      Ni <br>")
    print("95.1   2.225   0.65    0.25 <br>")
    sys.exit(1)

print("PASSED - output fields and values match expected output <br>")
sys.exit(0)
