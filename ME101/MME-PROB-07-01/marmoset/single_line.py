#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
single_line.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys
import os

test_file = open("two_words.txt", "w");
test_file.write("Happy   Birthday!\n");
test_file.close();

cproc=Popen("./read_two_words", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

os.remove("two_words.txt");

count_lines = re.findall("\n", out)

if len(count_lines) > 1 :
    print "failed - Too many output lines."
    sys.exit(1)
else :
    print "passed - Single output line."
    sys.exit(0)
