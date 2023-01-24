#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max = 0
    for i in range(len(my_list)):
        if max < my_list[i]:
            max = my_list[i]
    return max
