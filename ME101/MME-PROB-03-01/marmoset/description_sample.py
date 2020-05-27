#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys
import os

def execute_programs(input_string) :
    cproc=Popen("./numerical_notation", stdin=PIPE, stderr=PIPE, stdout=PIPE)
    f_out,f_err=cproc.communicate(input_string)
    cproc=Popen("./numerical_notation_canonical", stdin=PIPE, stderr=PIPE, stdout=PIPE)
    f_out_canonical,f_err_canonical=cproc.communicate(input_string)

    return (f_out, f_err, f_out_canonical, f_err_canonical)

def extract_values(output_string) :
    split1 = output_string.split("\n")
    split2 = []
    split3 = []

    for i in range(len(split1)) :
        if len(split1[i]) > 1 :
            split2.append(split1[i])

    for i in range(len(split2)) :
        if re.search("[a-df-z]", split2[i], re.IGNORECASE) is None :
            split3.append(split2[i])

    return list_of_outputs

def outputs_match(student_output, canonical_output) :
    student_values = extract_values(student_output)
    canonical_values = extract_values(canonical_output)

    if len(student_values) != len(canonical_values) :
        print "failed - "

    return True;


input_list = ["299792458", "3.14159265358979323846264", "1.6021766208e-19", "6.02214085774E23"]

out = ""
err = ""
out_canonical = ""
err_canonical = ""

for next_input in input_list :
    out, err, out_canonical, err_canonical = execute_programs(next_input)

    print outputs_match(out, out_canonical)

sys.exit(0)
