#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
BOM_master.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import re

class design_master :
    def __init__(self, init_name) :
        self.name = init_name
        self.parts = []
        self.cost = 0.0

    def add_part(self, input_string) :
        parse_string = re.split("\s+", input_string.strip())
        self.parts.append([int(parse_string[0]), int(parse_string[1])])

    def get_cost(self, master_catalog) :
        total_cost = 0
        for part in self.parts :
            total_cost += master_catalog.get_part_cost(part[0]) * part[1]
        return total_cost

    def get_qty_parts(self, master_catalog) :
        total_parts = 0
        for part in self.parts :
            total_parts += part[1]
        return total_parts
            
    def print_design(self) :
        print self.name
        print len(self.parts)
        for part in self.parts :
            print part

class BOM_master :
    def __init__(self) :
        self.designs = []
        
        BOM_file = open("BOMs.txt", "r")
        
        design_name = BOM_file.readline().strip()
        while (design_name) :
            new_design = design_master(design_name)
            
            qty_parts = int(BOM_file.readline())
            
            for part_index in range(qty_parts) :
                new_design.add_part(BOM_file.readline())
                
            self.designs.append(new_design)
                
            BOM_file.readline()
            
            design_name = BOM_file.readline().strip()
        
        BOM_file.close()
    