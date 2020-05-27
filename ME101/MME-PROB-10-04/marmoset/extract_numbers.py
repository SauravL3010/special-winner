#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
extracted_numbers.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import re

def extract_numbers(output_string) :
    numeric_const_pattern = r"""
    \s*
    [-+]? # optional sign
    (?:
        (?: \d* \. \d+ ) # .1 .12 .123 etc 9.1 etc 98.1 etc
        |
        (?: \d+ \.? ) # 1. 12. 123. etc 1 12 123 etc
    )
    # followed by optional exponent part if desired
    (?: [Ee] [+-]? \d+ ) ?
    """

    extracted_numbers = re.findall(numeric_const_pattern, output_string, re.MULTILINE | re.VERBOSE)
    extracted_numbers = [float(text_number) for text_number in extracted_numbers]
    return extracted_numbers
