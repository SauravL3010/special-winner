#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect
import re

pexpect_process = pexpect.spawn("./prime_number")
pexpect_process.expect("(?i)enter")
pexpect_process.sendline("1223")

print("Inputted values: 1223")
print("Expected output: prime")

pexpect_process.expect("\r\n")
# print(pexpect_process.before)
# this print of asterisks is necessary to ensure reliable capture of the output string
print("***")
pexpect_process.expect(".+")

output_string = str(pexpect_process.after, 'utf-8')
search_list = ["(?i)prime", "(?i)composite"]

found_list = []
for search_item in search_list :
    if re.search(search_item, output_string) :
        found_list.append(True)
    else :
        found_list.append(False)

if found_list == [True, False] :
    print("PASSED")
    exit(0)
else :
    print("FAILED")
    # print(output_string)
    # print(found_list)
    exit(1)
