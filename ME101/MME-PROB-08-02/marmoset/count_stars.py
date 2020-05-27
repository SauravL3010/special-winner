#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys
import os
import random

test_cases = ["5", "1", "2", "0"]

test_cases.append(str(random.randint(10, 20)))

for case in test_cases :
    cproc=Popen("./star_pyramid", stdin=PIPE, stderr=PIPE, stdout=PIPE)
    out,err=cproc.communicate(case)

    star_count = 0;

    for character in out :
        if character is "*" :
            star_count = star_count + 1

    if star_count != int(case) * int(case) :
        print "failed - number of stars does not meet specification"
        print "input: " + case
        sys.exit(3)

print "passed - number of stars meets specification"
sys.exit(0)
