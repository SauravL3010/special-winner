#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
function_declarations.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import re

found_all_function_declarations = True

submission_source_file = open("filling_potholes.cpp", "r")
submission_source_text = submission_source_file.read()
submission_source_file.close()

if not re.search("double\s+pothole_volume\s*\(\s*double\s+\w+\s*\)", submission_source_text) :
    print("FAILED <br>")
    print("Did not find function declaration for pothole_volume()")
    found_all_function_declarations = False

if not re.search("void\s+read_file\s*\(\s*\w*(::)?ifstream\s*&\s*\w+,\s*int\s+\w+\s*\[\s*\w*\s*\]\s*\[\s*\w*\s*\]\s*\)", submission_source_text) :
    print("FAILED <br>")
    print("Did not find function declaration for read_file()")
    found_all_function_declarations = False

if not re.search("double\s+repair_volume\s*\(\s*int\s+\w+\s*\[\s*\w*\s*\]\s*\[\s*\w*\s*\]\s*,\s*int\s+\w+\s*,\s*bool\s+\w+\s*\)", submission_source_text) :
    print("FAILED <br>")
    print("Did not find function declaration for repair_volume()")
    found_all_function_declarations = False

if found_all_function_declarations :
    print("PASSED <br>")
    print("Found all expected function declarations: <br>")
    print("pothole_volume() : returns double, receives double <br>")
    print("read_file() : does not return value, receives ifstream passed by reference and 2D int array <br>")
    print("repair_volume() : returns double, receives 2D int array, int, and bool <br>")
    exit(0)
else :
    exit(1)
