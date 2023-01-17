#!/usr/bin/python3
for alphabet in range(97, 123):
    if alphabet == ord('e') or alphabet == ord('q'):
        continue
    print("{:c}".format(alphabet), end="")