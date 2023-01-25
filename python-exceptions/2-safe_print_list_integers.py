#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        c = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{}".format(my_list[i]), end="")
                c += 1
        print()
    except:
        print()
    return c
