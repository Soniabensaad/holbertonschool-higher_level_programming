#!/usr/bin/python3
def common_elements(set_1, set_2):
    a_set = set(set_1)
    b_set = set(set_2)
    return list(a_set & b_set)
    e = common(set_1,set_2)
    print(e)
