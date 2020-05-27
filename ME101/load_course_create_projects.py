#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
load_course_create_projects.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import os
import re
import lxml.html

def project_list() :
    question_folders = []
    for entry in os.listdir('.') :
        if re.search("MME-PROB-", entry) :
            question_folders.append(entry)
    question_folders.sort()
    return question_folders

def get_title(projectNumber) :
    file_list = os.listdir('./' + projectNumber + '/marmoset/canonical/')
    return file_list[0][:-4]

def projectNumber_to_time(projectNumber) :
    projectNumber_split = re.split("-", projectNumber)
    result_time = projectNumber_split[2] + ":" + projectNumber_split[3] + ":00"
    return result_time

def add_project(marmoset_configuration, marmoset_session, coursePK,
        projectNumber, title) :
    URL_new_project = 'https://' + marmoset_configuration['submitserver'] + \
                        '/view/instructor/createProject.jsp?coursePK=' + coursePK

    new_project_page = marmoset_session.get(URL_new_project, timeout=15)
    # print(new_project_page.text)

    params = {'service' : 'https://' + marmoset_configuration['submitserver']
                            + '/action/instructor/CreateProject'}

    new_project_html = lxml.html.fromstring(new_project_page.text)
    hidden_elements = new_project_html.xpath('//form//input[@type="hidden"]')
    form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

    form['projectNumber'] = projectNumber
    due_time = projectNumber_to_time(projectNumber)
    form['ontime'] = "2020-12-31 " + due_time
    form['late'] = "2020-12-31 " + due_time
    form['title'] = title
    form['stackTracePolicy'] = "full_stack_trace"
    form['releasePolicy'] = "after_public"
    form['bestSubmissionPolicy'] = "edu.umd.cs.submitServer.BestBestSubmissionPolicy"
    form['numReleaseTestsRevealed'] = "-1"
    form['releaseTokens'] = "3"
    form['regenerationTime'] = "12"
    form['initialBuildStatus'] = "new"
    form['kindOfLatePenalty'] = "constant"
    form['lateConstant'] = "0"
    form['lateMultiplier'] = "0"

    canonicalStudentRegistrationPK = new_project_html.xpath("//select[@name='canonicalStudentRegistrationPK']/option")
    form['canonicalStudentRegistrationPK'] = canonicalStudentRegistrationPK[0].attrib.get('value')

    project_utilities_page = marmoset_session.post(params['service'], data=form, params=params, timeout=15)

    return project_utilities_page


def upload_project_zip(marmoset_configuration,
                        marmoset_session,
                        project_utilities_page,
                        projectNumber) :
    print("Uploading project zip file for " + projectNumber + ".")
    project_utilities_html = lxml.html.fromstring(project_utilities_page.text)

    params = {'service' : 'https://' + marmoset_configuration['submitserver']
                            + '/action/instructor/UploadProjectJarfile'}

    hidden_elements = project_utilities_html.xpath('//form//input[@type="hidden"]')
    form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

    upload_file = {'file' : open('./' + projectNumber + '/marmoset/Archive.zip', 'rb')}

    upload_file_result = marmoset_session.post(params['service'],
        data=form, params=params, files=upload_file)

    return upload_file_result

def upload_canonical(marmoset_configuration,
                    marmoset_session,
                    project_utilities_page,
                    projectNumber,
                    title) :
    print("Uploading canonical: " + title + ".cpp")
    project_utilities_html = lxml.html.fromstring(project_utilities_page.text)

    params = {'service' : 'https://' + marmoset_configuration['submitserver']
                            + '/action/SubmitProjectViaWeb'}

    hidden_elements = project_utilities_html.xpath('//form//input[@type="hidden"]')
    form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

    upload_file = {'file' : open('./' + projectNumber + '/marmoset/canonical/' + title + '.cpp', 'rb')}

    upload_file_result = marmoset_session.post(params['service'],
        data=form, params=params, files=upload_file)

    return upload_file_result

def create_all_projects(marmoset_configuration, marmoset_session, coursePK) :
    for projectNumber in project_list() :
        title = get_title(projectNumber)
        print("creating project " + projectNumber + " : " + title)

        project_utilities_page = add_project(marmoset_configuration,
                                            marmoset_session,
                                            coursePK,
                                            projectNumber,
                                            title)

        upload_project_zip(marmoset_configuration,
                            marmoset_session,
                            project_utilities_page,
                            projectNumber)

        upload_canonical(marmoset_configuration,
                        marmoset_session,
                        project_utilities_page,
                        projectNumber,
                        title)

    return None
