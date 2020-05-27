#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sphere_calculations.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import math

def sphere_calculations(radius_yards) :
    YARDS_TO_METERS = 0.9144
    radius_meters = radius_yards * YARDS_TO_METERS
    surface_area = 4 * math.pi * pow(radius_meters,2)
    volume = 4.0/3 * math.pi * pow(radius_meters,3)

    return [radius_meters, surface_area, volume]
