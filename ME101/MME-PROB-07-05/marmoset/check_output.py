#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
check_output.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import re

class check_output_consts() :
    SUCCESS_OUTPUT_GOOD = 0
    ERROR_TOO_FEW_OUTPUT_LINES = -1
    ERROR_TOO_MANY_OUTPUT_LINES = -2
    ERROR_COUNTRY_MISMATCH = -3
    ERROR_MEDAL_ORDER = -4
    ERROR_MEDAL_COUNT = -5
    ERROR_MOST_COUNTRY = -6
    ERROR_MOST_MEDALS = -6

def check_medal_order(chart_string) :
    encountered_silver = False
    encountered_gold = False

    for character in chart_string :
        if character == 'B' and (encountered_silver == True or encountered_gold == True) :
            return False
        if character == 'S' :
            encountered_silver = True
            if encountered_gold :
                return False
        if character == 'G' :
            encountered_gold = True
    return True

def count_medals(chart_string) :
    qty_bronze = 0
    qty_silver = 0
    qty_gold = 0

    for character in chart_string :
        if character == 'B' :
            qty_bronze += 1
        elif character == 'S' :
            qty_silver += 1
        elif character == 'G' :
            qty_gold += 1

    return (qty_gold, qty_silver, qty_bronze)

def check_output(output, filename) :
    success = check_output_consts.SUCCESS_OUTPUT_GOOD

    # split out into lines
    output = re.split("\n", output)
    # remove empty lines
    output = [out_line for out_line in output if out_line]
    # remove beginning and ending whitespace from each line
    output = [str.strip(out_line) for out_line in output]
    # split each line into country name and medal chart
    output = [re.split("\s+", out_line) for out_line in output]

    input_file = open(filename, "r")

    count_file_lines = input_file.readlines()
    if len(output) <= len(count_file_lines) :
        success = check_output_consts.ERROR_TOO_FEW_OUTPUT_LINES
        
    if len(output) > len(count_file_lines) + 1:
        success = check_output_consts.ERROR_TOO_MANY_OUTPUT_LINES

    line_count = 0
    find_most_qty = 0
    find_most_country = ""
    
    input_file.seek(0)    
    for input_line in input_file :
        if (success == check_output_consts.SUCCESS_OUTPUT_GOOD) :
            input_line_parsed = re.split("\s+", input_line)

            if input_line_parsed[0] != output[line_count][0] :
                success = check_output_consts.ERROR_COUNTRY_MISMATCH

            # check order of medals in chart (should be B, S, G)
            elif check_medal_order(output[line_count][1]) == False :
                success = check_output_consts.ERROR_MEDAL_ORDER

            else :
                output_medals = count_medals(output[line_count][1])
                if (int(input_line_parsed[1]) != output_medals[0]) or \
                    (int(input_line_parsed[2]) != output_medals[1]) or \
                    (int(input_line_parsed[3]) != output_medals[2]):
                    success = check_output_consts.ERROR_MEDAL_COUNT

                else :
                    total_medals = int(input_line_parsed[1]) + \
                                   int(input_line_parsed[2]) + \
                                   int(input_line_parsed[3])

                    if total_medals > find_most_qty :
                        find_most_qty = total_medals
                        find_most_country = input_line_parsed[0]

        line_count += 1

    if (success == check_output_consts.SUCCESS_OUTPUT_GOOD) :
        output_has_most_country = False
        output_has_most_qty = False
        for output_last_line_word in output[-1] :
            if re.search("^"+find_most_country+"$", output_last_line_word) :
                output_has_most_country = True
            if re.search("^"+str(find_most_qty)+"$", output_last_line_word) :
                output_has_most_qty = True

        if output_has_most_country == False :
            success = check_output_consts.ERROR_MOST_COUNTRY
        elif output_has_most_qty == False :
            success = check_output_consts.ERROR_MOST_MEDALS

    return success

def output_message(test_result) :
    if test_result == check_output_consts.SUCCESS_OUTPUT_GOOD :
        print "PASSED <br>"
        print "Program output matches expected output. <br>"
        print "Elements checked: <br>"
        print "* number of output line <br>"
        print "* country names displayed in same order as received <br>"
        print "* medals in chart displayed in B, S, G order <br>"
        print "* number of medals in chart match input file <br>"
        print "* name of country with most medals <br>"
        print "* number of most medals"
        return 0

    elif test_result == check_output_consts.ERROR_TOO_FEW_OUTPUT_LINES :
        print "FAILED <br>"
        print "Too few output lines in program output."

    elif test_result == check_output_consts.ERROR_TOO_MANY_OUTPUT_LINES :
        print "FAILED <br>"
        print "Too many output lines in program output."

    elif test_result == check_output_consts.ERROR_COUNTRY_MISMATCH :
        print "FAILED <br>"
        print "Program output did not display all country names. Check spelling and order."

    elif test_result == check_output_consts.ERROR_MEDAL_ORDER :
        print "FAILED <br>"
        print "Chart output did not display medals in expected order. <br>"
        print "Order should be bronze, silver, then gold."

    elif test_result == check_output_consts.ERROR_MEDAL_COUNT :
        print "FAILED <br>"
        print "Chart output did not display the expected number of medals."

    elif test_result == check_output_consts.ERROR_MOST_COUNTRY :
        print "FAILED <br>"
        print "Output incorrect for country with most medals."

    else :
        print "FAILED <br>"
        print "Unknown error."

    return 1
