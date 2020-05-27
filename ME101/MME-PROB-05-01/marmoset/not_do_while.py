#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
not_for.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import sys

source_file = open("first_while_loop.cpp", "r")

found_do_while = False;
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
        match_do_while = re.search("\sdo\s", read_line)
        if match_do_while :
            found_do_while = True;

    if match_single_comment :
        within_comment = False;

source_file.close()

if not found_do_while :
    print "passed - No use of do-while loop."
    sys.exit(0)
else :
    print "failed - Found the use of a do-while loop."
    sys.exit(1)
