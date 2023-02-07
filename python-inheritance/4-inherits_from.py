#!/usr/bin/python3
"""
Only sub class of
"""


def inherits_from(obj, a_class):
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
