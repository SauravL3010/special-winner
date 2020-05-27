#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
load_course_configuration.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import re

class ConfigurationError(RuntimeError) :
    def __init__(self, arg) :
        self.args = arg

def load_configuration() :
    configuration_read = {}

    try :
        config_file = open("load_course.conf", "r")

        print("Opened load_course.conf successfully.")

        line_count = 0
        for line in config_file :
            line_count += 1
            split_line = re.split("=", line)
            if len(split_line) != 2 :
                raise ConfigurationError([line_count, line])

            configuration_read[split_line[0]] = split_line[1].strip()
    except IOError :
        print("ERROR - Could not open load_course.conf.")
        return None
    except ConfigurationError as exception :
        print("ERROR - load_course.conf is not valid, line " + str(exception.args[0]) + ":")
        print(exception.args[1])
        return None
    else :
        return configuration_read

def verify_configuration(marmoset_configuration) :
    configuration_valid = True
    expected_fields = ["submitserver", "course_name", "semester"]
    for verify_field in expected_fields :
        if marmoset_configuration.get(verify_field) == None :
            print("ERROR - load_course.conf missing field: " + verify_field)
            configuration_valid = False
    return configuration_valid
