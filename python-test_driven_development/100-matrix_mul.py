#!/usr/bin/python
"""
function that multiplies 2 matrices
"""

def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")
    if not all(all(isinstance(j, (int, float))for j in i)for i in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(j, (int, float))for j in i)for i in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(i) for i in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(i) for i in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("matrices can not be multiplied")
   

    rows_A = len(m_a)
    cols_A = len(m_a[0])
    rows_B = len(m_b)
    cols_B = len(m_b[0])

    if cols_A != rows_B:
        return

    
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += m_a[i][k] * m_b[k][j]
    return C




