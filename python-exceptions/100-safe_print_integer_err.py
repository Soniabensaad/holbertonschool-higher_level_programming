#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    if isinstance(value, int):
        print("{}".format(value))
        return True
    else:
        sys.stderr.write("Exception: " + "False" + "\n")
