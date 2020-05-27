#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
gen_ratings.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

QTY_INPUT_FILES = 3

TEMP_MIN = 91
TEMP_MAX = 99

COARSENESS_MIN = 1
COARSENESS_MAX = 4

RATING_MIN = 1
RATING_MAX = 10

import numpy
import random

def more_ratings_to_write_to_file(ratings_table) :
    for temperature_row in range(TEMP_MAX-TEMP_MIN+1) :
        for coarseness_col in range(COARSENESS_MAX-COARSENESS_MIN+1) :
            if ratings_table[temperature_row][coarseness_col] > 0 :
                return True
    return False

random.seed()

ratings_files = []
for file_num in range(QTY_INPUT_FILES) :
    ratings_files.append(open("coffee"+str(file_num+1)+".txt", "w+"))

    ratings_table = numpy.zeros((TEMP_MAX-TEMP_MIN+1, COARSENESS_MAX-COARSENESS_MIN+1), dtype=int)

    for temperature_row in range(TEMP_MAX-TEMP_MIN+1) :
        for coarseness_col in range(COARSENESS_MAX-COARSENESS_MIN+1) :
            ratings_table[temperature_row][coarseness_col] = random.randint(RATING_MIN, RATING_MAX)

    while more_ratings_to_write_to_file(ratings_table) == True :
        write_row = random.randint(0, TEMP_MAX-TEMP_MIN)
        write_col = random.randint(0, COARSENESS_MAX-COARSENESS_MIN)
        if ratings_table[write_row][write_col] > 0 :
            output_string = "{write_temperature:5}{write_coarseness:4}{write_rating:5}".\
                format(write_temperature=TEMP_MIN+write_row,\
                    write_coarseness=COARSENESS_MIN+write_col,\
                    write_rating=ratings_table[write_row][write_col])
            ratings_files[file_num].write(output_string+"\n")
            ratings_table[write_row][write_col] = 0

    ratings_files[file_num].close()
