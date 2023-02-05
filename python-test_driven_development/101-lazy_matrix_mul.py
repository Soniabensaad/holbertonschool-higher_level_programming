#!/usr/bin/python3

"""multiplies 2 matrices by using the module NumPy
"""


def lazy_matrix_mul(m_a, m_b):
    import numpy as np
    """multiplies 2 matrices by using the module NumPy"""
    return (np.dot(m_a, m_b))
