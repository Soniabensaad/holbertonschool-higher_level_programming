#!/usr/bin/python3
"""
Pascal's Triangle
Technical interview preparation
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    new = []
    if n <= 0:
        return new
    for i in range(n):
        pascal = []
        for j in range(i + 1):
            if j == 0:
                pascal.append(1)
            elif j == i:
                pascal.append(1)
            else:
                pascal.append(new[i - 1][j - 1] + new[i - 1][j])
        new.append(pascal)
    return new
