Problem Number: MME-PROB-02-04
------------------------------

Problem Title: Steel MSDS
=========================

Code filename: steel_MSDS.cpp

Write a program that provides a form for the user to fill out some Material Safety Data Sheet information. The form must have exactly the same format as the following example:

    SDS ID No.: 9994
    Product Identifier: Cold Rolled Sheet Steel
    Carcinogenity: 2
    Reproductive Toxicity: 2
    STOT Repeat Exposure: 1
    Composition (% weight):
    Iron: 95
    Manganese: 2.225
    Chromium: 0.65
    Nickel: 0.25

Note that the Product Identifier will always be composed of four words.

After the user has entered the information, reproduce the information in a compressed format:

    SDS: 9994     Identifier: Cold Rolled Sheet Steel
    Hazard: 2-2-1
    Composition:
    Fe    Mn    Cr    Ni
    95    2.225 0.65  0.25

You may reference the three included MSDS documents to see real-world examples of these types of documents.

© 2017 DAVID LAU ALL RIGHTS RESERVED
