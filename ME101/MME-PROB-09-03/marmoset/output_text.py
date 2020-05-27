#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
output_text.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import os
import re

if not os.path.isfile("./BOM_costs.txt") :
    print "FAILED<br>"
    print "Did not find expected output file BOM_costs.txt."
    exit(1)

output_file = open("BOM_costs.txt", "r")
output_text = output_file.read()

found_lowest_cost = False
if re.search("lowest\s+cost", output_text, re.IGNORECASE) or \
    re.search("least\s+cost", output_text, re.IGNORECASE) or \
    re.search("min(imum)*\s+cost", output_text, re.IGNORECASE) :
    found_lowest_cost = True
else :
    print "FAILED <br>"
    print "Did not find an output phrase for the lowest cost. <br>"
    exit(1)

found_most_parts = False
if re.search("most\s+(\w+\s)*parts", output_text, re.IGNORECASE) :
    found_most_parts = True
else :
    print "FAILED <br>"
    print "Did not find an output phrase for the most parts. <br>"
    exit(1)

if found_lowest_cost and found_most_parts :
    print "PASSED <br>"
    print "Found output phrases for the lowest cost and most parts. <br>"
    exit(0)
