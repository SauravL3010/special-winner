#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
calc_coordinates.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import math

def calc_coordinates() :
    return_coordinates = []

    drone_directions = open("drone_directions.txt", "r")

    coordinate_x = 0.0;
    coordinate_y = 0.0;
    current_heading = 0.0;

    for input_line in drone_directions :
        input_line_split = re.split(" ", input_line)
        input_line_split[1] = input_line_split[1].strip()
        input_line_float = [float(element) for element in input_line_split]

        current_heading = current_heading + input_line_float[1]
        coordinate_x = coordinate_x + input_line_float[0] * math.cos(math.radians(current_heading))
        coordinate_y = coordinate_y + input_line_float[0] * math.sin(math.radians(current_heading))

        return_coordinates.append([coordinate_x, coordinate_y])

    drone_directions.close()

    return return_coordinates
