#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
© 2017 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import sys
import os
import subprocess
from shutil import copyfile

copyfile("Makefile.real", "Makefile")

subprocess.call(["make", "-s"])

copyfile("Makefile.dummy", "Makefile")


if os.path.isfile("star_pyramid") :
    print "passed - star_pyramid compiled successfully"
    sys.exit(0)
else :
    print "failed - did not compile successfully"
    sys.exit(1)
