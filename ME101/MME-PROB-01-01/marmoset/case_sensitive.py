#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import sys

input = ["./hello_world"]
cproc=Popen(input, stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

match_case_1 = re.search("Hello", out)
match_case_2 = re.search("World", out)

if match_case_1 and match_case_2 :
    print "passed - correct capitalization of letters"
    sys.exit(0)
elif not match_case_1 and not match_case_2 :
    print "failed - neither 'Hello' nor 'World' have the correct capitalization"
    sys.exit(1)
elif not match_case_1 :
    print "failed - 'Hello' does not have the correct capitalization"
    sys.exit(1)
else :
    print "failed - 'World' does not have the correct capitalization"
    sys.exit(1)
