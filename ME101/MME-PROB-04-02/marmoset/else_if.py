#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
else_if.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import os
import sys
import re

if not os.path.isfile("bigger_or_smaller.cpp") :
    print "ERROR - Could not find bigger_or_smaller.cpp."
    sys.exit(1)

source_file = open("bigger_or_smaller.cpp", "r")

match_if = 0
match_else = 0
match_else_if = 0
within_comment = False;
for read_line in source_file :
    match_begin_comment = re.search("\/\*", read_line)
    if match_begin_comment :
        within_comment = True;
    match_end_comment = re.search("\*\/", read_line)
    if match_end_comment :
        within_comment = False;
    match_single_comment = re.search("\/\/", read_line)
    if match_single_comment :
        within_comment = True;

    if not within_comment :
        if re.search("\sif\s", read_line) :
            match_if += 1
        if re.search("\selse\s", read_line) :
            match_else += 1
        if re.search("\selse\sif\s", read_line) :
            match_else_if += 1

    if match_single_comment :
        within_comment = False;

if match_if > 2 :
    print "FAILED - too many if statements"
    sys.exit(1)
if match_else < 2 :
    print "FAILED - too few else statements"
    sys.exit(1)
if match_else_if < 1 :
    print "FAILED - too few 'else if' statements"
    sys.exit(1)
if match_else_if > 1 :
    print "FAILED - too many 'else if' statements"
    sys.exit(1)

print "PASSED - concise if statement structure"
sys.exit(0)
