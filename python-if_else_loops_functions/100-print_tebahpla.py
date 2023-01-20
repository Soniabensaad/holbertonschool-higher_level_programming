#!/usr/bin/python3
for a in range(122, 96, -1):
    b = a
    if a % 2 != 0:
        b = a - 32
    print("{}".format(chr(b)), end="")
