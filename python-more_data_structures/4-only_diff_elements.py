#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_a = set(set_1)
    set_b = set(set_2)
    set_a.symmetric_difference_update(set_b)
    return(set_a)