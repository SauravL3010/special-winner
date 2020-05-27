#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
load_course.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import re
from load_course_configuration import load_configuration, verify_configuration
from load_course_login_marmoset import marmoset_login
from load_course_create_projects import create_all_projects
from load_course_activate_projects import activate_projects
import lxml.html
import urllib3


class HaltScriptError(RuntimeError) :
    def __init__(self, arg) :
        self.args = arg

def get_coursePK(marmoset_configuration, marmoset_session) :
    URL_course_listing = 'https://' + marmoset_configuration['submitserver'] + '/view/index.jsp'
    course_listing_page = marmoset_session.get(URL_course_listing, timeout=15)
    course_listing_html = lxml.html.fromstring(course_listing_page.text)

    links_list = course_listing_html.xpath('//a')

    for link in links_list :
        if re.search(marmoset_configuration['course_name'], link.text) and \
            re.search(marmoset_configuration['semester'], link.text) :
            coursePK = (re.split('coursePK=',link.attrib.get('href')))[1]
            return coursePK

    print("ERROR - course not found: " + marmoset_configuration['course_name']
            + ", " + marmoset_configuration['semester'])
    return None


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try :
    marmoset_configuration = load_configuration()
    if marmoset_configuration == None :
        raise HaltScriptError(["marmoset_configuration is None."])

    configuration_valid = verify_configuration(marmoset_configuration)

    if configuration_valid == False:
        raise HaltScriptError(["configuration is not valid."])

    print("Course information: ")
    for configuration_key in marmoset_configuration :
        print(configuration_key + " : " + marmoset_configuration[configuration_key])

    print("Userid: ", end = '')
    username = input()
    marmoset_session = marmoset_login(username,
                                    'https://cas.uwaterloo.ca/cas/login',
                                    marmoset_configuration['submitserver'])

    if marmoset_session == None :
        raise HaltScriptError(["marmoset_session is None."])

    coursePK = get_coursePK(marmoset_configuration, marmoset_session)

    if coursePK == None :
        raise HaltScriptError(["coursePK not found."])
    else :
        print("retrieved coursePK: " + coursePK)

    create_all_projects(marmoset_configuration, marmoset_session, coursePK)
    activate_projects(marmoset_configuration, marmoset_session, coursePK)

except HaltScriptError as exception:
    print("ERROR - load_course.py terminated prematurely: " + exception.args[0])
