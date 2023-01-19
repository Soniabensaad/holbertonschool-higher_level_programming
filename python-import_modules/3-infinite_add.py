#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    Sum = 0
    for i in range (1,arg):
        Sum += int(sys.argv[i])
    print(Sum, end=" ")