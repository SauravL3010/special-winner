#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
gen_message.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

from random import randint

def gen_message(original_message) :

    message_split = original_message.split()
    message_index = [index for index in range(len(message_split))]
    message_split = [(message_element, index_element) for message_element, index_element in zip(message_split, message_index)]

    encoded = []
    while len(message_split) > 0:
        pick_index = randint(0, len(message_split)-1)
        encoded.append(message_split[pick_index])
        del message_split[pick_index]

    fout = open("secret_message.txt", "w")
    for encoded_element in encoded:
        fout.write(encoded_element[0] + " " + str(encoded_element[1]) + "\n")
