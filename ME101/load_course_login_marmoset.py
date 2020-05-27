#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
load_course_login_marmoset.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

import requests
from requests.exceptions import Timeout
import lxml.html
from getpass import getpass

def cas_login(service, username, password):
    # GET parameters - URL we'd like to log into.
    params = {'service': service + '/'}
    LOGIN_URL = service

    # Start session and get login form.
    session = requests.session()
    login = session.get(LOGIN_URL, params=params)

    # Get the hidden elements and put them in our form.
    login_html = lxml.html.fromstring(login.text)
    hidden_elements = login_html.xpath('//form//input[@type="hidden"]')
    form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

    # "Fill out" the form.
    form['username'] = username
    form['password'] = password

    # Finally, login and return the session.
    session.post(LOGIN_URL, data=form, params=params)

    # TODO - check if login was successful or not

    return session

def marmoset_login(username, URL_CAS, marmoset_server) :
    marmoset_session = cas_login(URL_CAS, username, getpass())

    params = {'service' : 'https://' + marmoset_server + '/authenticate/PerformLogin'}
    try :
        login2 = marmoset_session.get('https://' + marmoset_server, params=params, verify=False, timeout=15)

        login_html = lxml.html.fromstring(login2.text)
        hidden_elements = login_html.xpath('//form//input[@type="hidden"]')
        form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

        form['campusUID'] = username
        form['uidPassword'] = username

        marmoset_session.post('https://' + marmoset_server + '/authenticate/PerformLogin', data=form, params=params, timeout=15)
    except Timeout as exception:
        print("ERROR - GET request timed out accessing https://" + marmoset_server)
        print(exception)
        return None

    return marmoset_session
