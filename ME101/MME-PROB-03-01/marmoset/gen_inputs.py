#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
gen_inputs.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import random

random.seed()

create_input_file = open("input_strings.txt", "w+")

print("Input numbers: <br>")

# generate a 6-digit integer
input_number = random.randint(1e5, 1e6)
create_input_file.write(str(input_number) + "\n")
print(str(input_number) + " <br>")

# negative version of 6-digit integer
create_input_file.write("-" + str(input_number) + "\n")
print("-" + str(input_number) + " <br>")

# generate a 2-digit integer
input_number = random.randint(1e1, 1e2)
create_input_file.write(str(input_number) + "\n")
print(str(input_number) + " <br>")

# negative version of 2-digit integer
create_input_file.write("-" + str(input_number) + "\n")
print("-" + str(input_number) + " <br>")

# generate an 19-digit integer
input_number = random.randint(1e18, 1e19)
create_input_file.write(str(input_number) + "\n")
print(str(input_number) + " <br>")

# negative version of 19-digit integer
create_input_file.write("-" + str(input_number) + "\n")
print("-" + str(input_number) + " <br>")

# generate a floating point number
input_mantissa = random.randint(1e5, 1e6) / 1e5
input_exponent = random.randint(0, 100)
create_input_file.write(str(input_mantissa) + "E" + str(input_exponent) + "\n")
print(str(input_mantissa) + "E" + str(input_exponent) + " <br>")
