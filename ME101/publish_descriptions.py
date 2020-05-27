#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
publish_descriptions.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import os
import re
import shutil

directory_listing = os.listdir(".")

for entry in directory_listing:
    if re.search("MME-PROB-", entry) :
        project_file_listing = os.listdir(entry)
        for project_file in project_file_listing :
            if re.search("Problem Description", project_file) :
                print entry + "/" + project_file
                shutil.copyfile(entry + "/" + project_file, "../marmoset_practice_published/" + project_file)
