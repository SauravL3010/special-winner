#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
output_file_exists.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import os

input = ["./request_for_quote"]
cproc=Popen(input, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True)
out,err = cproc.communicate()

if os.path.isfile("./BOM_costs.txt") :
    print "PASSED<br>"
    print "Found expected output file BOM_costs.txt."
    exit(0)
else :
    print "FAILED<br>"
    print "Did not find expected output file BOM_costs.txt."
    exit(1)
