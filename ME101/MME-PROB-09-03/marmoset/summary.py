#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
summary.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import os
import re
from catalog_master import catalog_master
from BOM_master import BOM_master

if not os.path.isfile("./BOM_costs.txt") :
    print "FAILED<br>"
    print "Did not find expected output file BOM_costs.txt."
    exit(1)

output_file = open("BOM_costs.txt", "r")
output_text = output_file.read()
output_file.close()

master_catalog = catalog_master()
master_BOM = BOM_master()

# find designs with lowest cost and most parts

lowest_cost = -1
most_parts = 0
for design in master_BOM.designs :
    if design.get_cost(master_catalog) < lowest_cost or lowest_cost < 0 :
        lowest_cost = design.get_cost(master_catalog)
        lowest_cost_design = design
    if design.get_qty_parts(master_catalog) > most_parts :
        most_parts = design.get_qty_parts(master_catalog)
        most_parts_design = design

# look in the last 5 lines of the output file for the design_names
# of the lowest cost design and the design with the most parts

output_text_lines = re.split("\n", output_text)
if not re.search(lowest_cost_design.name, str(output_text_lines[-5:])) :
    print "FAILED <br>"
    print "Did not correctly identify lowest cost design: " + lowest_cost_design.name + " <br>"
    exit(1)
if not re.search(most_parts_design.name, str(output_text_lines[-5:])) :
    print "FAILED <br>"
    print "Did not correctly identify design with most parts: " + most_parts_design.name + " <br>"
    exit(1)

print "PASSED <br>"
print "Correctly identified lowest cost design and design with the most parts. <br>"
exit(0)
