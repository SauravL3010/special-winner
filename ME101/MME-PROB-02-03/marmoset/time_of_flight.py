#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
time_of_flight.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import math

def get_times(velocity, launch_angle, elevation) :
    angle_rad = launch_angle * math.pi / 180
    time_1 = -10.0/981 * (math.sqrt(2)*math.sqrt(50*pow(velocity,2)*pow(math.sin(angle_rad),2)-981*elevation) \
                          - 10 * velocity * math.sin(angle_rad));
    time_2 = 10.0/981 * (math.sqrt(2)*math.sqrt(50*pow(velocity,2)*pow(math.sin(angle_rad),2)-981*elevation) \
                          + 10 * velocity * math.sin(angle_rad));
    result = [time_1, time_2]
    result.sort()
    return result

def get_max_elevation(velocity, launch_angle) :
    angle_rad = launch_angle * math.pi / 180
    max_height = pow(velocity,2)*pow(math.sin(angle_rad),2)/(2*9.81)
    return max_height
