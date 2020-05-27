#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
above_or_below.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re

TOLERANCE = 1e-6

def above_or_below(x_coordinate, y_coordinate) :
    return_list = [[],[]]
    if abs(x_coordinate - y_coordinate) < TOLERANCE :
        return_list = [["on"],["above", "below"]]
    elif x_coordinate > y_coordinate :
        return_list = [["below"],["above", "on"]]
    else :
        return_list = [["above"], ["below", "on"]]

    return return_list

def check_output(output, canonical_result, first_num, second_num) :
    return_code = 0

    for find_expected in canonical_result[0] :
        if not re.search("(?i)" + find_expected, output) :
            print "FAILED - Did not find the keyword '" + find_expected + "'.<br>"
            return_code += 1

    for find_excluded in canonical_result[1] :
        if re.search("(?i)" + find_excluded, output) :
            print "FAILED - Found keyword '" + find_excluded + "'.<br>"
            return_code += 2

    if return_code == 0 :
        print "PASSED - Found keyword '" + find_expected + "'.<br>"

    print "x_coordinate: " + str(first_num) + "<br>"
    print "y_coordinate: " + str(second_num) + "<br>"
    print "<br>"

    return return_code
