#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    if len(arg) - 1 == 0:
        print("{} arguments.".format(len(arg) - 1, end=" "))
    elif len(arg) - 1 == 1:
        print("{} argument:".format(len(arg) - 1, end=" "))
    else:
        print("{} arguments:".format(len(arg) - 1, end=" "))

    for i, argument in enumerate(arg):
        if(i == 0):
            continue
        else:
            print("{}:{}".format((i), argument))

        
    


