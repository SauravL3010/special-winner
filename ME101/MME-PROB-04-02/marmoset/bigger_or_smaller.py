#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
bigger_or_smaller.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re

def bigger_or_smaller(first_num, second_num) :
    return_list = [[],[]]
    if first_num > second_num :
        return_list = [["first", "larger"],["second", "equal"]]
    elif second_num > first_num :
        return_list = [["second", "larger"],["first", "equal"]]
    else :
        return_list = [["equal"], ["first", "second", "larger"]]

    return return_list

def check_output(output, canonical_result, first_num, second_num) :
    return_code = 0

    for find_expected in canonical_result[0] :
        if not re.search("(?i)" + find_expected, output) :
            print "FAILED - Did not find the keyword '" + find_expected + "'."
            print "first number: " + str(first_num)
            print "second number: " + str(second_num)
            return_code += 1

    for find_excluded in canonical_result[1] :
        if re.search("(?i)" + find_excluded, output) :
            print "FAILED - Found keyword '" + find_excluded + "'."
            print "first number: " + str(first_num)
            print "second number: " + str(second_num)
            return_code += 2

    return return_code
