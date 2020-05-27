#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
function_declarations.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from pathlib import Path
from remove_comments import remove_comments
import re

check_file_exists = Path("./coffee_rating.cpp")

if not check_file_exists.is_file() :
    print("ERROR - Did not find expected input file: coffee_rating.cpp")
    exit(1)

remove_comments("coffee_rating.cpp", "comments_removed.cpp")

submission_file_comments_removed = open("comments_removed.cpp", "r")
submission_file_text = submission_file_comments_removed.read()
submission_file_comments_removed.close()

found_read_file_function = False
found_best_coffee_function = False

if re.search("read_file\s*\(", submission_file_text) :
    found_read_file_function = True
if re.search("best_coffee\s*\(", submission_file_text) :
    found_best_coffee_function = True

if not found_read_file_function :
    print("FAILED - Did not find read_file() function. <br>")
    exit(1)
elif not found_best_coffee_function :
    print("FAILED - Did not find best_coffee() function. <br>")
    exit(1)
else :
    print("PASSED - Found declarations for read_file() and best_coffee() functions. <br>")
    exit(0)
