#!/usr/bin/python3
"""
My integer
"""

class MyInt(int):
    """class MyInt that inherits from int"""
    def __init__(self, value):
        """initialisation"""
        self.value = value

    def __eq__(self, other):
        """equal comparaison"""
        return self.value != other

    def __ne__(self, other):
        """inequal comparaison"""
        return self.value == other
