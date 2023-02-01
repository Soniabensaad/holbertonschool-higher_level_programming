#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    matrix: list of lists of integers or floats
    div must be a number (integer or float)
    Each row of the matrix must be of the same size
    """
    new_matrix = []
    if matrix:
        for i in matrix:
            if any(type(j) is not int and type(j) is not float for j in i)\
                    or type(matrix) is not list or len(i) == 0:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row = len(matrix[0])
        for i in matrix:
            if row != len(i):
                raise TypeError("Each row of the matrix must have the same size")
    else:
        raise("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        d = []
        for value in row:
            division = round((value / div), 2)
            d.append(division)
        new_matrix.append(d)
    return new_matrix
