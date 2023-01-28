#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
          print("{}".format(value))
          return True
    except Exception:
        sys.stderr.write("Exception: " + "False" + "\n")
