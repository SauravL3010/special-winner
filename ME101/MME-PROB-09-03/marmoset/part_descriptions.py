#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
part_descriptions.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import os
import re
from catalog_master import catalog_master

if not os.path.isfile("./BOM_costs.txt") :
    print "FAILED<br>"
    print "Did not find expected output file BOM_costs.txt."
    exit(1)

output_file = open("BOM_costs.txt", "r")
output_text = output_file.read()
output_file.close()

master_catalog = catalog_master()

# build search string consisting of all the part descriptions
all_descriptions_found = True
last_position_found = 0
BOM_file = open("BOMs.txt", "r")
design_name = BOM_file.readline()
design_name = design_name.strip()
while (design_name) :
    qty_parts = int(BOM_file.readline())
    for part_line in range(qty_parts) :
        part_line_parsed = re.split("\s+", BOM_file.readline().strip())
        part_line_parsed = [int(part_line_parsed[0]), int(part_line_parsed[1])]
        regex_search = re.compile(master_catalog.get_description(part_line_parsed[0]))
        regex_match = regex_search.search(output_text, last_position_found)
        if not regex_match :
            print "Did not find expected part description: " + master_catalog.get_description(part_line_parsed[0]) + " <br>"
            all_descriptions_found = False
        else :
            last_position_found = regex_match.start()

    BOM_file.readline()

    design_name = BOM_file.readline()
    design_name = design_name.strip()
BOM_file.close()

if all_descriptions_found :
    print "PASSED <br>"
    print "Found all expected part descriptions, in correct order. <br>"
    exit(0)
else :
    print "FAILED <br>"
    exit(1)
