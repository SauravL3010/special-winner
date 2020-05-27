#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
words_separated.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from random import randint
import re
import sys
import os

test_strings=[["Hello", "World"], ["R2", "D2"], ["Happy", "Birthday!"],
              ["Tau", "6.28318530718"],
              ["Pneumonoultramicroscopicsilicovolcanoconiosis",
              "Hippopotomonstrosesquipedaliophobia"]]

def get_whitespace() :
    gen_whitespace = ""
    num_tabs = randint(0,3)
    for gen_tabs in range(num_tabs) :
        gen_whitespace = gen_whitespace + "\t"
    num_endlines = randint(0,3)
    for gen_endlines in range(num_endlines) :
        gen_whitespace = gen_whitespace + "\n"
    num_spaces = randint(0,3)
    for gen_spaces in range(num_spaces) :
        gen_whitespace = gen_whitespace + " "
    return gen_whitespace

# create file
for test_string in test_strings :
    test_file = open("two_words.txt", "w")
    whitespace = get_whitespace()
    test_file.write(test_string[0] + whitespace +
                    test_string[1] + "\n")
    test_file.close()

    cproc=Popen("./read_two_words", stdin=PIPE, stderr=PIPE, stdout=PIPE)
    out,err=cproc.communicate()

    os.remove("two_words.txt")

    output_matches = re.search(test_string[0] + " " + test_string[1], out)
    if not output_matches :
        print "failed - console output does not match expected string"
        print test_string[0] + " " + test_string[1]
        sys.exit(1)

print "passed - all " + str(len(test_strings)) + " cases"
sys.exit(0)
