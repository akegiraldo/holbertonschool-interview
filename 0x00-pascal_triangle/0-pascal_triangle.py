#!/usr/bin/python3
"""
Python function that returns a list of lists of integers representing
the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Python function that returns a list of lists of integers representing
    the Pascal's triangle of n
    """
    result = []

    for i in range(0, n):
        list_ = []

        if i == 0:
            list_ = [1]
        else:
            for x in range(0, len(ant) + 1):

                if x == 0 or x == len(ant):
                    list_.append(1)
                else:
                    list_.append(ant[x-1] + ant[x])

        ant = list_
        result.append(list_)

    return result
