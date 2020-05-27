#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
overall_output.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import subprocess
from extract_numbers import extract_numbers
import math
import re


def run_test() :
    # 1) generate new input files
    # 2) run canonical code to file best temperature and coarseness
    # 3) run submission code

    subprocess.run(["./gen_ratings.py"])
    subprocess.run(["./coffee_rating_canonical"])
    run_submission = subprocess.Popen(["./coffee_rating"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    submission_output, submission_errors = run_submission.communicate()

    return submission_output, submission_errors

def check_output_for_numbers(submission_output) :
    submission_output_numbers = extract_numbers(submission_output)

    if (len(submission_output_numbers) < 2) :
        print("FAILED - Found fewer than two numerical values in output. <br>")
        return(1, submission_output_numbers)

    if (len(submission_output_numbers) > 2) :
        print("FAILED - Found more than two numerical values in output. <br>")
        return(1, submission_output_numbers)

    for output_number in submission_output_numbers :
        if math.modf(output_number)[0] != 0 :
            print("FAILED - The numerical values in the output were not integers. <br>")
            return(1, submission_output_numbers)

    return(0, submission_output_numbers)

def check_output_values(submission_output_numbers) :
    submission_output_numbers = [int(output_number) for output_number in submission_output_numbers]

    canonical_results_file = open("coffee_rating_canonical.txt", "r")
    canonical_results = [int(canonical_number) for canonical_number in re.split(" ", canonical_results_file.read())]
    print("Expected values: " + str(canonical_results) + " <br>")

    if submission_output_numbers != canonical_results :
        print("FAILED - The outputted temperature and coarseness values did not match the expected values. <br>")
        print("Outputted values: " + str(submission_output_numbers) + " <br>")
        return(1)

    return(0)

# main test body

QTY_TESTS = 10;

subprocess.run(["make", "-s", "-f", "Makefile_overall_output"])

for test_number in range(QTY_TESTS) :
    print("Test number: " + str(test_number + 1) + " <br>")

    submission_output, submission_errors = run_test()

    # check form of numerical values in submission output
    check_output_for_numbers_result = check_output_for_numbers(submission_output)
    if check_output_for_numbers_result[0] != 0 :
        exit(1)

    if check_output_values(check_output_for_numbers_result[1]) != 0:
        exit(1)

    print("PASSED - Program output agrees with expected values. <br>")
    print(" <br>")

exit(0)
