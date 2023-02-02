#!/usr/bin/python
"""
unittests for the function def max_integer(list=[])
"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    max = list[0]
    i = 0
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    return max