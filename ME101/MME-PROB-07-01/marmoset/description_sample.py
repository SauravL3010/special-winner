#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
description_sample.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import re
import sys
import os

test_file = open("two_words.txt", "w");
test_file.write("Hello World!\n");
test_file.close();

cproc=Popen("./read_two_words", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

os.remove("two_words.txt");

check_output = re.search("Hello World!", out)

if not check_output :
    print "failed - Input file contains 'Hello World!'"
    sys.exit(1)

print "passed - Input file contains 'Hello World!'"
sys.exit(0)
