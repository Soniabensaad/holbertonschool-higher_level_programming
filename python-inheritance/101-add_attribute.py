#!/usr/bin/python3
"""
Can I?
"""


def add_attribute(obj, attr, value):
    """ adds a new attribute to an object if it’s possible"""
    no_add = (int, float, str, bool, tuple, range)
    if type(obj) in no_add:
        raise TypeError("can't add new attribute")
    obj.__setattr__(attr, value)
