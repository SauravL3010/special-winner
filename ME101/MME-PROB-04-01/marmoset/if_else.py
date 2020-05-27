#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
if_else.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import sys

source_file = open("even_or_odd.cpp", "r")

count_ifs = 0;
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
        match_if = re.search("\sif\s", read_line)
        if match_if :
            count_ifs = count_ifs + 1;

    if match_single_comment :
        within_comment = False;

if count_ifs == 1 :
    print "passed - Expected number of if statements."
    sys.exit(0)
elif count_ifs > 1:
    print "failed - Too many if statements detected."
    sys.exit(1)
else :
    print "failed - Insufficient if statements detected."
    sys.exit(1)
