#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
uses_do_while.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import sys

source_file = open("first_do_while.cpp", "r")

count_do = 0;
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
        match_do = re.search("\sdo\s\{", read_line)
        if match_do :
            count_do = count_do + 1;

    if match_single_comment :
        within_comment = False;

source_file.close()

if count_do < 2 :
    print "FAILED - Too few do-while loops detected."
    sys.exit(1)
elif count_do > 2 :
    print "FAILED - Too many do-while loops detected."
    sys.exit(1)
else :
    print "PASSED - Two do-while loops detected."
    sys.exit(0)
