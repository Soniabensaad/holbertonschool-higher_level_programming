#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(x):
        my_list[i]
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                c += 1
        except ValueError and TypeError:
            continue
    print()
    return c
 
