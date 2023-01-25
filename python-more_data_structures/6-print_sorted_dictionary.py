#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    m_keys = list(a_dictionary.keys())
    m_keys.sort()
    for key in m_keys:
        print("{}: {}".format(key, a_dictionary[key]))
