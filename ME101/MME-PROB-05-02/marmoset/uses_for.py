#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
uses_for.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import sys

source_file = open("first_for_loop.cpp", "r")

found_while = False;
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
        match_while = re.search("\sfor\s\(", read_line)
        if match_while :
            found_while = True;

    if match_single_comment :
        within_comment = False;

source_file.close()

if found_while :
    print "PASSED - Found use of for loop."
    sys.exit(0)
else :
    print "FAILED - Did not find use of a for loop.<br>"
    print "Make sure there is no comment on the line with the while loop."
    sys.exit(1)
