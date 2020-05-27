#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
gen_BOMs.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import random
import re

class design_names :
    def __init__ (self) :
        self.design_names = ["Enterprise",
            "HAL_9000",
            "WALL-E",
            "Model_T",
            "Saturn_V",
            "StarTAC",
            "iPhone",
            "Muira",
            "E-type",
            "R2D2",
            "C3PO",
            "Vision",
            "Optimus_Prime",
            "Terminator",
            "T-1000",
            "GT40"]

    def get_design_name(self) :
        issue_name = random.choice(self.design_names)
        self.design_names.remove(issue_name)
        return issue_name

def reset_catalog(catalog) :
    for catalog_line in catalog :
        catalog_line[3] = 0

def gen_part_qty(catalog, part_index) :
    MAX_QTY_010 = 100
    MAX_QTY_100 = 12
    MAX_QTY_999 = 4

    part_qty_return = 0
    if catalog[part_index][2] < 0.10 :
        part_qty_return = random.randint(1, MAX_QTY_010)
    elif catalog[part_index][2] < 1.00 :
        part_qty_return = random.randint(1, MAX_QTY_100)
    else :
        part_qty_return = random.randint(1, MAX_QTY_999)

    return part_qty_return

MIN_QTY_DESIGNS = 3
MAX_QTY_DESIGNS = 10

MIN_QTY_PARTS = 5
MAX_QTY_PARTS = 30

random.seed()

design_names_library = design_names()

catalog_file = open("catalog.txt", "r")
BOM_file = open("BOMs.txt", "w+")

catalog = catalog_file.read()
catalog = re.split("\n", catalog)
catalog = [re.split("\s+", catalog_line) for catalog_line in catalog if catalog_line]
catalog = [[catalog_line[0], int(catalog_line[1]), float(catalog_line[2]), 0] for catalog_line in catalog]

MAX_QTY_PARTS = len(catalog)

random.seed()

qty_designs = random.randint(MIN_QTY_DESIGNS, MAX_QTY_DESIGNS)

print "BOMs.txt : <br>"

for design_num in range(qty_designs) :
    design_name = design_names_library.get_design_name()
    BOM_file.write(design_name + "\n")
    print design_name + "<br>"
    # BOM_file.write("Design_%d\n" % (design_num+1))

    reset_catalog(catalog)

    qty_parts = random.randint(MIN_QTY_PARTS, MAX_QTY_PARTS)
    BOM_file.write("%d\n" % qty_parts)
    print str(qty_parts) + "<br>"

    for part_num in range(qty_parts) :
        part_index = random.randint(0, MAX_QTY_PARTS - 1)
        while (catalog[part_index][3] == 1) :
            part_index = random.randint(0, MAX_QTY_PARTS - 1)

        output_string = "{part_number:25}{part_qty:10}".format(part_number=catalog[part_index][1], part_qty=gen_part_qty(catalog, part_index))
        BOM_file.write(output_string + "\n")
        print(output_string+"<br>")
        # BOM_file.write("%d   " % catalog[part_index][1])
        # BOM_file.write("%d\n" % gen_part_qty(catalog, part_index))

        catalog[part_index][3] = 1

    BOM_file.write("\n")
    print "<br>"
