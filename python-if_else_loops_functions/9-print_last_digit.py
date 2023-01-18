#!/usr/bin/python3
def print_last_digit(number):
        dg_str = repr(number)
        l_dg_str = dg_str[-1]
        l_dg = int(l_dg_str)
        print(f"{l_dg}", end="")
        return(l_dg)
