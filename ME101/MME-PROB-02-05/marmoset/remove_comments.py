#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
remove_comments.py
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

# Removes C++ style comments from a file and outputs the result to
# the specified output file. Uses a state machine.
def remove_comments(code_file_name, output_file_name):
    current_state = "CODE"

    output_file = open(output_file_name, "w")
    file_text = open(code_file_name).read()

    for file_character in file_text:
        if current_state == "CODE":
            if file_character == "\"":
                current_state = "STRING"
                output_file.write(file_character)
            elif file_character == "/":
                current_state = "COMMENT_POSSIBLE"
            else:
                output_file.write(file_character)
        elif current_state == "COMMENT_POSSIBLE":
            if file_character == "/":
                current_state = "COMMENT_SINGLE_LINE"
            elif file_character == "*":
                current_state = "COMMENT_MULTILINE"
            else:
                current_state = "CODE"
                output_file.write("/")
                output_file.write(file_character)
        elif current_state == "COMMENT_SINGLE_LINE":
            if file_character == "\n":
                current_state = "CODE"
                output_file.write(file_character)
        elif current_state == "COMMENT_MULTILINE":
            if file_character == "*":
                current_state = "COMMENT_MULTILINE_POSSIBLE_END"
        elif current_state == "COMMENT_MULTILINE_POSSIBLE_END":
            if file_character == "/":
                current_state = "CODE"
            else:
                current_state = "COMMENT_MULTILINE"
        elif current_state == "STRING":
            output_file.write(file_character)
            if file_character == "\"":
                current_state = "CODE"
