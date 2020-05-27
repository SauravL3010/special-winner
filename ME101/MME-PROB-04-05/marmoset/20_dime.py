#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect

pexpect_process = pexpect.spawn("./making_change")
pexpect_process.expect("(?i)enter")
pexpect_process.sendline("0")
pexpect_process.expect("(?i)enter")
pexpect_process.sendline("20")
pexpect_process.expect("(?i)coins")
pexpect_process.expect("[\d.]+")

output_number_bytestring = pexpect_process.after
output_number_string = str(output_number_bytestring, 'utf-8')
print("Inputted value: 0 dollars and 20 cents")
print("Expected output (number of coins): 2")
if output_number_string == "2" :
    print("PASSED")
    exit(0)
else :
    print("FAILED")
    exit(1)
