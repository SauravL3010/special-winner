#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
pothole_map.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import math
import numpy

class pothole_map :
    def __init__(self) :
        self.QTY_STREET = 75
        self.QTY_AVENUE = 75

        self.map = numpy.zeros((self.QTY_STREET, self.QTY_AVENUE))

        pothole_file = open("potholes.txt", "r")

        for pothole_line in pothole_file :
            pothole_line = re.split("\s+", pothole_line)
            pothole_line = [int(element) for element in pothole_line if element]

            street_num = pothole_line[0]
            avenue_num = pothole_line[1]
            radius = pothole_line[2]

            self.map[street_num - 1][avenue_num - 1] = radius

    def volume_repair(self, street_or_avenue, road_num) :
        if street_or_avenue == "street" :
            return sum(map(lambda r:2/3.0*math.pi*pow(r/1000.0,3) ,self.map[road_num - 1][:]))
        else :
            # print self.map[:,road_num - 1]
            return sum(map(lambda r:2/3.0*math.pi*pow(r/1000.0,3) ,self.map[:,road_num - 1]))

    def next_repair(self, target_volume) :
        best_delta_volume = target_volume
        next_road_num = 0
        next_road_is_street = True

        for street_num in range(self.QTY_STREET) :
            street_volume = self.volume_repair("street", street_num)
            if target_volume - street_volume < best_delta_volume and \
                target_volume - street_volume > 0 :
                best_delta_volume = target_volume - street_volume
                next_road_num = street_num
                next_road_is_street = True

        for avenue_num in range(self.QTY_AVENUE) :
            avenue_volume = self.volume_repair("avenue", avenue_num)
            if target_volume - avenue_volume < best_delta_volume and \
                target_volume - avenue_volume > 0 :
                best_delta_volume = target_volume - street_volume
                next_road_num = avenue_num
                next_road_is_street = False

        if next_road_is_street :
            return (next_road_num, "Street")
        else :
            return (next_road_num, "Avenue")
