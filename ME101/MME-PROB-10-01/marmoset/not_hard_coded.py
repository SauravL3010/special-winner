#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
not_hard_coded.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import sys

source_file = open("2D_print.cpp", "r")

count_cout = 0;
count_endl = 0;
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
        if re.search("\s+cout\s+", read_line) :
            count_cout = count_cout + 1
        if re.search("[\<\s]endl", read_line) :
            count_endl = count_endl + 1

    if match_single_comment :
        within_comment = False;

source_file.close()

if count_cout > 9 or count_endl > 9 :
    print "FAILED - Too many cout or endl statements.<br>"
    print "Suspected hard-coded solution."
    sys.exit(1)
else :
    print "PASSED - No hard-coded solution detected."
    sys.exit(0)
