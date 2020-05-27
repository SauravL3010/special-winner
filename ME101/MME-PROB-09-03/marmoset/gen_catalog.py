#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
gen_catalog.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import random
import re

catalog_master_file = open("catalog_master.txt", "r")
catalog_file = open("catalog.txt", "w+")

catalog_master = catalog_master_file.read()
catalog_master = re.split("\n", catalog_master)
catalog_master = [re.split("\s+", catalog_master_line) for catalog_master_line in catalog_master if catalog_master_line]

MIN_CATALOG_PARTS = 10
MAX_CATALOG_PARTS = 30
qty_catalog_parts = random.randint(MIN_CATALOG_PARTS, MAX_CATALOG_PARTS)

print "catalog.txt : <br>"
for part_num in range(qty_catalog_parts) :
    selected_part = random.choice(catalog_master)
    catalog_master.remove(selected_part)
    output_string = "{part_description:30s}{part_number:12s}{part_cost:10s}" \
                    .format(part_description=selected_part[0], part_number=selected_part[1], part_cost=selected_part[2])
    catalog_file.write(output_string+"\n")
    print output_string+"<br>"

catalog_master_file.close()
catalog_file.close()

exit(0)
