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

    line_split = re.split("start of output\n", out)
    del line_split[0]

    line_split = re.split("end of output", line_split[0])
    del line_split[1]

    spaces_count = len(re.findall(" ", line_split[0]))

    if spaces_count != int(case) * (int(case) - 1) / 2 :
        print "failed - incorrect spacing"
        print "input: " + case
        sys.exit(3)

print "passed - correct spacing"
sys.exit(0)
