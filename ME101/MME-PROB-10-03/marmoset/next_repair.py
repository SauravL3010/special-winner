#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
test_repair_volume.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
from pothole_map import pothole_map
import re

the_map = pothole_map()

TARGET_VOLUME = 0.25
canonical_results = the_map.next_repair(TARGET_VOLUME)

cproc=Popen("./filling_potholes", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True)
out,err = cproc.communicate()

result_correct = True

if not re.search(str(canonical_results[0]), out) :
    print("FAILED <br>")
    print("Output does not contain the expected street/avenue number. <br>")
    result_correct = False

if canonical_results[1] == "Street" :
    if (not re.search("street", out, re.IGNORECASE)) or \
        re.search("avenue", out, re.IGNORECASE) :
        print("FAILED <br>")
        print("Output did not correctly identify road as a street. <br>")
        result_correct = False

if canonical_results[1] == "Avenue" :
    if (not re.search("avenue", out, re.IGNORECASE)) or \
        re.search("street", out, re.IGNORECASE) :
        print("FAILED <br>")
        print("Output did not correclty identify road as an avenue. <br>")
        result_correct = False

if result_correct :
    print("PASSED <br>")
    print("Correctly identified the next street/avenue to be repaired as <br>")
    print(str(canonical_results[0]) + " " + canonical_results[1] + " <br>")
    exit(0)
else :
    exit(1)
