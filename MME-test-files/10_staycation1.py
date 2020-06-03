#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect
import re

pexpect_process = pexpect.spawn("./vacation_decision")
pexpect_process.expect(".+")
pexpect_process.sendline("99")
pexpect_process.sendline("2")

print("Inputted values: $99 and 2 days")
print("Expected output: staycation")

pexpect_process.expect("\r\n")
# print(pexpect_process.before)
# this print of asterisks is necessary to ensure reliable capture of the output string
print("***")
pexpect_process.expect("(?i)staycation|Toronto|Vancouver|New York City|Hong Kong")

output_string = str(pexpect_process.after, 'utf-8')
search_list = ["(?i)staycation", "(?i)Toronto", "(?i)Vancouver", "(?i)New York City", "(?i)Hong Kong"]

found_list = []
for search_item in search_list :
    if re.search(search_item, output_string) :
        found_list.append(True)
    else :
        found_list.append(False)

if found_list == [True, False, False, False, False] :
    print("PASSED")
    exit(0)
else :
    print("FAILED")
    # print(output_string)
    # print(found_list)
    exit(1)
