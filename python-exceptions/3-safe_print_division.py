#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
        c = int(a) / int(b)
        return c
    except ZeroDivisionError:
        c = None
        return None
    finally:
        print("Inside result: {}".format(c))