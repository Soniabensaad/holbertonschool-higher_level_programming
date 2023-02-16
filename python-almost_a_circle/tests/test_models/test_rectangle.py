#!/usr/bin/python3
"""Unittest rectangle.
Test cases for class Rectangle.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_Rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.id, 4)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, 5)
