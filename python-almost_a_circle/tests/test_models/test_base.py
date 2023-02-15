#!/usr/bin/python3
"""Unittest base.
Test cases for class Base.
"""
from models import Base
import unittest
class TestBase(unittest.TestCase):
    """Test case for class Base."""


    def test_1_0(self):
        """Check for id."""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
if __name__ == "__main__":
    unittest.main()