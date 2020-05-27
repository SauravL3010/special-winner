#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
check_spacing.py
© 2017 DAVID LAU ALL RIGHTS RESERVED
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

check_space = re.search(r"y +B", out, re.IGNORECASE)
if not check_space :
    print "failed - no space found"
    sys.exit(1)

count_spaces = re.findall(" ", check_space.group(0))

if len(count_spaces) != 1 :
    print "failed - number of spaces between words should be 1"
    print "number of spaces found: " + str(len(count_spaces))
    sys.exit(1)

print "passed - space between words"
sys.exit(0)
