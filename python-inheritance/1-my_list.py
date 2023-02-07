#!/usr/bin/python3
"""
inherits from list
"""


class MyList(list):
    """contains the class MyList inherited from list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
