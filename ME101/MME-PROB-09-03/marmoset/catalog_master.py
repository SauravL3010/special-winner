#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
catalog_master.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import re

class catalog_master :
    def __init__(self) :
        self.parts = []

        catalog_file = open("catalog_master.txt", "r")

        for catalog_file_line in catalog_file :
            parsed_line = re.split("\s+", catalog_file_line.strip())
            self.parts.append([parsed_line[0], int(parsed_line[1]), float(parsed_line[2])])

        catalog_file.close()

    def get_description(self, part_number) :
        index_check = 0
        return_description = ""
        while index_check < len(self.parts) and return_description == "" :
            if part_number in self.parts[index_check] :
                return_description = self.parts[index_check][0]
            index_check += 1
        return return_description

    def get_part_cost(self, part_number) :
        index_check = 0
        return_cost = 0.00
        while index_check < len(self.parts) and return_cost <= 0.00 :
            if part_number in self.parts[index_check] :
                return_cost = self.parts[index_check][2]
            index_check += 1
        return return_cost
        