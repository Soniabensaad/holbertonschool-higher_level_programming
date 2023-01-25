#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for delete in a_dictionary:
        if delete == key:
            remove_key = a_dictionary.pop(key)
            return a_dictionary
    return a_dictionary
