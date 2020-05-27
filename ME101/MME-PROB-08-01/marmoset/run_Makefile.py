#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import sys
import os
import subprocess
from subprocess import Popen, PIPE
from shutil import copyfile

COMPILE_SUCCESSFUL_FILE = "compile_successful.txt"

if os.path.exists(COMPILE_SUCCESSFUL_FILE) :
    os.remove(COMPILE_SUCCESSFUL_FILE)

copyfile("Makefile.real", "Makefile")

# subprocess.call(["make", "-s"])
cproc=Popen("make", stdin=PIPE, stderr=PIPE, stdout=PIPE)
out,err=cproc.communicate()

copyfile("Makefile.dummy", "Makefile")

function_does_not_return_1 = re.search("warning: control reaches end of non-void function", err)
function_does_not_return_2 = re.search("warning: no return statement in function returning non-void", err)
if function_does_not_return_1 or function_does_not_return_2 :
    print "failed - function does not return a value"
    sys.exit(1)

if os.path.isfile("time_of_flight") :
    outfile = open(COMPILE_SUCCESSFUL_FILE, "w")
    outfile.write("time_of_flight.cpp compiled successfully")

    print "passed - time_of_flight compiled successfully"
    sys.exit(0)
else :
    print "failed - did not compile successfully"
    sys.exit(1)
