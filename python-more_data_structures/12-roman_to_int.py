#!/usr/bin/python3
romans = {
    "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
}
def roman_to_int(roman_string):
    number = 0
    i = 0
    l = len(roman_string)
    if not  isinstance(roman_string, str):
        return None
    while i < l:
        r1 = romans[roman_string[i]]
        if i+1 < l:
            r2 = romans[roman_string[i + 1]]
            if r1 >= r2:
                number = number + r1
                i = i + 1
            else:
                number = number - r1
                i = i + 1
        else:
            number = number + r1
            i = i + 1
    return number

