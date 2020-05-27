#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
run_balance_1.py
© 2019 DAVID LAU ALL RIGHTS RESERVED
'''

from subprocess import Popen,PIPE
import re
import threading
import time
import Queue

class ReadOutput :
    def __init__(self) :
        self.flag_run_read_output_thread = True

    def read_output_pipe(self, pipe, queue) :
        while self.flag_run_read_output_thread :
            from_pipe = pipe.read()
            queue.put(from_pipe)

def get_output_threaded(output_queue) :
    output_string = ""
    start_time = time.time()
    try_output = Queue.Empty
    while (try_output == Queue.Empty and (time.time() - start_time < 0.25)) :
        try :
            try_output = output_queue.get(False)
            output_string = output_string + try_output
            time.sleep(0)
        except Queue.Empty :
            pass
    if try_output == Queue.Empty :
        return "TIME_OUT"
    else :
        return output_string

def get_output_numbers(output_string) :
    numeric_const_pattern = r"""
    \s*
    [-+]? # optional sign
    (?:
        (?: \d* \. \d+ ) # .1 .12 .123 etc 9.1 etc 98.1 etc
        |
        (?: \d+ \.? ) # 1. 12. 123. etc 1 12 123 etc
    )
    # followed by optional exponent part if desired
    (?: [Ee] [+-]? \d+ ) ?
    """

    extracted_numbers = re.findall(numeric_const_pattern, output_string, re.MULTILINE | re.VERBOSE)
    extracted_numbers = [float(text_number) for text_number in extracted_numbers]
    return extracted_numbers

def run_Balance(weight_david, weight_daughter, parse_numbers=True) :
    cproc=Popen('./balance_1', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=0, universal_newlines=True)
    output_queue = Queue.Queue()
    read_output_function = ReadOutput()
    read_output_thread = threading.Thread(target=read_output_function.read_output_pipe, args=(cproc.stdout, output_queue))
    # read_output_thread.daemon = True
    read_output_thread.start()

    cproc.stdin.write(str(weight_david) + "\n")
    cproc.stdin.write(str(weight_daughter) + "\n")

    cproc_out = get_output_threaded(output_queue)

    cproc.wait()
    read_output_function.flag_run_read_output_thread = False

    if parse_numbers :
        return get_output_numbers(cproc_out)
    else :
        return cproc_out
