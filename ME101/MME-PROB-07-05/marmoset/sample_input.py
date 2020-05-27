#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sample_input.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from shutil import copyfile
from check_output import *
from subprocess import Popen,PIPE
import re
import sys
import os

print "Program tested using sample input file. <br>"

copyfile("medal_count_sample.txt", "medal_count.txt")

cproc=Popen("./medal_count", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

test_result = check_output(out, "medal_count.txt")

os.remove("medal_count.txt")

return_code = output_message(test_result)

exit(return_code)
