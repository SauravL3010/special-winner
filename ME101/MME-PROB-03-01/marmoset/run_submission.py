#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
run_submission.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import pexpect
import re

def run_code(code_instance, input_string) :
    try :
        MAX_QTY_CHARS = 256
        qty_chars = 0
        while qty_chars < MAX_QTY_CHARS :
            read_char = code_instance.read_nonblocking(size=1, timeout=0.1)
            qty_chars += 1
    except pexpect.TIMEOUT :
        code_instance.send(input_string + "\n")

    read_output = code_instance.read(-1)
    read_output = re.split("\r*\n", read_output)
    read_output = [output_element for output_element in read_output if output_element]
    read_output = read_output[1:]

    return(read_output)

def run_canonical(input_string) :
    submission_instance = pexpect.spawn("./numerical_notation_canonical", encoding='utf-8')
    read_output = run_code(submission_instance, input_string)
    return(read_output)

def run_submission(input_string) :
    submission_instance = pexpect.spawn("./numerical_notation", encoding='utf-8')
    read_output = run_code(submission_instance, input_string)
    return(read_output)
