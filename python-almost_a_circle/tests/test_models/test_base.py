#!/usr/bin/python3
"""Unittest base.
Test cases for class Base.
"""
from models import Base
import unittest
class TestBase(unittest.TestCase):

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_specified_id(self):
        b3 = Base(89)
        self.assertEqual(b3.id, 89)