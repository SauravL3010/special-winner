#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
modulus.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import sys

source_file = open("even_or_odd.cpp", "r")

found_modulus = False;
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
        match_modulus = re.search("%", read_line)
        if match_modulus :
            found_modulus = True;

    if match_single_comment :
        within_comment = False;

source_file.close()

if found_modulus :
    print "passed - Found use of modulus operator."
    sys.exit(0)
else :
    print "failed - Did not find use of modulus operator.<br>"
    print "Make sure there is no comment on the line with the modulus operator."
    sys.exit(1)
