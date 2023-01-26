#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = int(a) / int(b)
        print("{}".format(c))
    except ZeroDivisionError:
        c = None
    finally:
        print("Inside result : {}".format(c))
    return c