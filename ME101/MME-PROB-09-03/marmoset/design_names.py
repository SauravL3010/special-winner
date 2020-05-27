#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
design_names.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import os
import re

if not os.path.isfile("./BOM_costs.txt") :
    print "FAILED<br>"
    print "Did not find expected output file BOM_costs.txt."
    exit(1)

all_designs_found = True

BOM_file = open("BOMs.txt", "r")
output_file = open("BOM_costs.txt", "r")

output_text = output_file.read()

design_name = BOM_file.readline()
design_name = design_name.strip()
while (design_name and all_designs_found) :
    if not re.search(design_name, output_text) :
        print "FAILED <br>"
        print design_name + " not found in output file. <br>"
        all_designs_found = False

    qty_parts = int(BOM_file.readline())
    for part_line in range(qty_parts) :
        BOM_file.readline()
    BOM_file.readline()

    design_name = BOM_file.readline()
    design_name = design_name.strip()

BOM_file.close()
output_file.close()

if all_designs_found :
    print "PASSED <br>"
    print "All design names from BOMs.txt found in output file. <br>"
    exit(0)
else :
    exit(1)
