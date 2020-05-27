#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
not_for.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import sys

source_file = open("first_while_loop.cpp", "r")

found_for = False;
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
        match_for = re.search("\sfor\s\(", read_line)
        if match_for :
            found_for = True;

    if match_single_comment :
        within_comment = False;

source_file.close()

if not found_for :
    print "passed - No use of for loop."
    sys.exit(0)
else :
    print "failed - Found the use of a for loop."
    sys.exit(1)
