#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
load_course_activate_projects.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import lxml.html
import time

def init_projects_to_activate_list(marmoset_configuration, marmoset_session, coursePK) :
    project_listing_page = marmoset_session.get("https://" + marmoset_configuration['submitserver'] +
        "/view/instructor/course.jsp?coursePK=" + coursePK, timeout=15)
    project_listing_html = lxml.html.fromstring(project_listing_page.text)

    projects_to_activate = []
    links_to_inactive = project_listing_html.xpath("//a[text()=' inactive ']")
    for element in links_to_inactive :
        project_to_activate = {}

        path_to_project_utilities = element.attrib['href']
        URL_project_utilities = "https://" + marmoset_configuration['submitserver'] + \
                                path_to_project_utilities

        project_to_activate['URL_project_utilities'] = URL_project_utilities
        project_to_activate['activation_state'] = "WAITING FOR TESTING"

        projects_to_activate.append(project_to_activate)

    return projects_to_activate

def state_WAITING_FOR_TESTING(marmoset_configuration, marmoset_session, project) :
    project_utilities_page = marmoset_session.get(project['URL_project_utilities'], timeout=15)
    project_utilities_html = lxml.html.fromstring(project_utilities_page.text)

    project['heading'] = project_utilities_html.xpath("//h1")[0].text

    search_for_assign_points = project_utilities_html.xpath("//a[text()='assign points']")
    if len(search_for_assign_points) > 0 :
        link_to_assign_points = project_utilities_html.xpath("//a[text()='assign points']")[0].attrib['href']
        project['URL_assign_points'] = "https://" + marmoset_configuration['submitserver'] + link_to_assign_points
        project['activation_state'] = "PASSED TEST"
    else :
        search_for_failure = project_utilities_html.xpath("//a[text()='failed']")
        if len(search_for_failure) > 0 :
            project['activation_state'] = "FAILED TEST"

    return project

def state_PASSED_TEST(marmoset_configuration, marmoset_session, project) :
    assign_points_page = marmoset_session.get(project['URL_assign_points'], timeout=15)
    assign_points_html = lxml.html.fromstring(assign_points_page.text)

    params = {'service' : 'https://' + marmoset_configuration['submitserver']
                            + '/action/instructor/AssignPoints'}

    hidden_elements = assign_points_html.xpath('//form//input[@type="hidden"]')
    form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

    pointValue_elements = assign_points_html.xpath("//input[@class='pointValue']")

    for pointValue_element in pointValue_elements :
        form[pointValue_element.attrib['name']] = '1'

    assign_points_result = marmoset_session.post(params['service'], data=form, params=params, timeout=15)

    project['activation_state'] = "ACTIVATED"
    return project

def state_ACTIVATED(marmoset_configuration, marmoset_session, project) :
    project_utilities_page = marmoset_session.get(project['URL_project_utilities'], timeout=15)
    project_utilities_html = lxml.html.fromstring(project_utilities_page.text)

    hidden_elements = project_utilities_html.xpath('//form//input[@type="hidden"]')
    form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

    params = {'service' : 'https://' + marmoset_configuration['submitserver']
                            + '/action/instructor/MakeProjectVisible'}
    make_visible_result = marmoset_session.post(params['service'], data=form, params=params, timeout=15)

    project['activation_state'] = "VISIBLE"
    return project

# Uses state machine. States: WAITING FOR TESTING, PASSED TEST, ACTIVATED, FAILED TEST
def activate_projects(marmoset_configuration, marmoset_session, coursePK) :
    projects_to_activate = init_projects_to_activate_list(marmoset_configuration,
                                                        marmoset_session,
                                                        coursePK)

    project_activation_complete = False
    while project_activation_complete == False :
        for project in projects_to_activate :
            if project['activation_state'] == "WAITING FOR TESTING" :
                project = state_WAITING_FOR_TESTING(marmoset_configuration, marmoset_session, project)
            elif project['activation_state'] == "PASSED TEST" :
                project = state_PASSED_TEST(marmoset_configuration, marmoset_session, project)
            elif project['activation_state'] == "ACTIVATED" :
                project = state_ACTIVATED(marmoset_configuration, marmoset_session, project)

        project_activation_complete = True
        for project in projects_to_activate :
            if project['activation_state'] != "VISIBLE" and project['activation_state'] != "FAILED TEST" :
                project_activation_complete = False

        for print_project in projects_to_activate :
            print(print_project['heading'])
            print(print_project['activation_state'])

        if project_activation_complete == False :
            print("waiting 30 seconds...")
            time.sleep(30)

    count_failed_projects = 0
    for project in projects_to_activate :
        if project['activation_state'] == "FAILED TEST" :
            count_failed_projects += 1
    print(str(count_failed_projects) + " projects not activated.")


    return None
