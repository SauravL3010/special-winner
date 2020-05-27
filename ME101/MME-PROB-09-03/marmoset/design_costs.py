#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
design_costs.py
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

for design in master_BOM.designs :
    if not re.search(str(design.get_cost(master_catalog)), output_text) :
        print "FAILED <br>"
        print "Did not find expected design cost for design: " + design.name + " <br>"
        exit(1)

print "PASSED <br>"
print "Found expected design costs for all designs. <br>"
exit(0)
