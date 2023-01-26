#!/usr/bin/python3
def safe_print_division(a, b):
    c = None
    try:
        c = int(a) / int(b)
    except ZeroDivisionError:
        c = None
    finally:
        print("Inside result : {}".format(c))
        return c