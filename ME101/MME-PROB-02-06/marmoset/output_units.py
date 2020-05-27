#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
output_units.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from run_balance_1 import *

import re

result = run_Balance(60, 20, False)

found_units = False

if re.search("\s+meter", result) :
    print "Found phrase 'meter' in output. <br>"
    found_units = True
else :
    print "Did not find phrase 'meter' in output. <br>"

if re.search("\s+m\s+", result) :
    print "Found unit 'm' in output. <br>"
    found_units = True
else :
    print "Did not find unit 'm' in output. <br>"

if found_units :
    print "PASSED - Output includes units of meters. <br>"
    exit(0)
else :
    print "FAILED - No output units of meters found in output. Make sure there is a space before and after the unit. <br>"
    exit(1)
