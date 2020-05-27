#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
gen_numbers.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import random
import pexpect

random.seed()

def gen_many_pos_fixed() :
    return(random.randint(1E15,1E16))

def gen_many_pos_scientific() :
    mantissa = random.randint(1E15,1E16) / 1E15
    exponent = random.randint(1,200)
    return(mantissa*pow(10,exponent))

def run_submission(input_number) :
    submission = pexpect.spawn("./numerical_notation", encoding="utf-8")

    submission.sendline(str(input_number))

    submission.expect(str(input_number))
    print(submission.read())

run_submission(gen_many_pos_fixed())
