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

match_hello = re.search("hello", out, re.IGNORECASE)
match_world = re.search("world", out, re.IGNORECASE)

if match_hello and match_world :
    print "passed - has the words 'hello' and 'world'"
    sys.exit(0)
elif not match_hello and not match_world :
    print "failed - missing the words 'hello' and 'world'"
    sys.exit(1)
elif not match_world:
    print "failed - missing the word 'world'"
    sys.exit(1)
else :
    print "failed - missing the word 'hello'"
    sys.exit(1)
