#!/usr/bin/python3
"""Unittest base.
Test cases for class Base.
"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id , 1)
        self.assertEqual(r1.height, 2)
