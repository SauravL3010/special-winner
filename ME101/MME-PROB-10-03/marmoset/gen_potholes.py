#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
gen_potholes.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import random

QTY_STREET = 75
QTY_AVENUE = 75

MIN_POTHOLE_RADIUS = 50
MAX_POTHOLE_RADIUS = 1000

MIN_POTHOLES = 100
MAX_POTHOLES = 200

pothole_map = [[0] * QTY_STREET for _ in range(QTY_AVENUE)]

random.seed()

qty_potholes = random.randint(MIN_POTHOLES, MAX_POTHOLES)

pothole_file = open("potholes.txt", "w+")

print "potholes.txt : <br>"
for pothole_num in range(qty_potholes) :
    street_number = random.randint(1, QTY_STREET)
    avenue_number = random.randint(1, QTY_AVENUE)

    while (pothole_map[street_number - 1][avenue_number - 1] != 0) :
        street_number = random.randint(1, QTY_STREET)
        avenue_number = random.randint(1, QTY_AVENUE)

    pothole_radius = random.randint(MIN_POTHOLE_RADIUS, MAX_POTHOLE_RADIUS)
    output_string = "{street_number:5}{avenue_number:5}{pothole_radius:10}".\
        format(street_number=street_number, avenue_number=avenue_number, pothole_radius=pothole_radius)
    pothole_file.write(output_string+"\n")
    print output_string + " <br>"

    pothole_map[street_number - 1][avenue_number - 1] = pothole_radius

pothole_file.close()
