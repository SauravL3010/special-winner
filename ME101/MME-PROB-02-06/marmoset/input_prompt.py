#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
input_prompt.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import pexpect

run_balance = pexpect.spawn("./balance_1")

try :
    run_balance.expect("weight", timeout=3)
except :
    run_balance.kill(0)
    print "FAILED <br>"
    print "Did not detect the keyword 'weight' in input prompt."
    exit(1)

print "PASSED <br>"
print "Found the keyword 'weight' in the input prompt."
exit(0)
