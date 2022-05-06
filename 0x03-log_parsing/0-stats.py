#!/usr/bin/python3
"""0. Log parsing"""

import signal
import sys
import re

sum = 0
codes_keys = ['200', '301', '400', '401', '403', '404', '405', '500']
codes_values = [0, 0, 0, 0, 0, 0, 0, 0]


def print_results():
    """Functions that prints the metrics"""
    print("File size: {}".format(sum))
    for key, value in zip(codes_keys, codes_values):
        if value > 0:
            print("{}: {}".format(key, value))


def signal_handler(signum, frame):
    """Function for handler signals"""
    print_results()


def is_valid_line(line):
    """Function that checks the line format"""

    pattern = '^[a-zA-Z0-9.]+\s?-\s?\[[0-9]{4}-[0-9]{2}-[0-9]\
{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}([.][0-9]+)?\]\s("GET /projects\
/260 HTTP/1.1")\s[0-9]{3}\s[0-9]{1,4}$'
    if not re.search(pattern, line):
        return False

    splitted = line.split()

    if splitted[-2] not in codes_keys:
        return False

    return True


signal.signal(signal.SIGINT, signal_handler)


idx = 1
printed_results = False
for line in sys.stdin:
    printed_results = False
    if not is_valid_line(line):
        try:
            splitted = line.split()
            size = int(splitted[-1])
            sum += size
        except Exception as _:
            pass
        continue

    splitted = line.split()
    code = splitted[-2]
    size = int(splitted[-1])

    sum += size
    codes_values[codes_keys.index(code)] += 1
    if idx % 10 == 0:
        printed_results = True
        print_results()

    idx += 1


if not printed_results:
    print_results()
