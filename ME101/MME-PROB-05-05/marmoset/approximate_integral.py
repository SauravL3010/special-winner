#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
approximate_integral.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import math

def approximate_integral(step_size) :
    x_val = 3.1
    integral_sum = 0.0

    while x_val <= 17.9 :
        f_x = math.sin(math.log(2*pow(x_val,3)-5*pow(x_val,2)+math.sqrt(3*x_val)+2))/(8*pow(x_val,2));
        integral_sum = integral_sum + f_x * step_size
        x_val = x_val + step_size

    return integral_sum
