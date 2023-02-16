#!/usr/bin/python3
"""Unittest base.
Test cases for class Base.
"""
from models.base import Base
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

    def test_json_to_string(self):
        json_none = Base.to_json_string(None)
        self.assertEqual(json_none, '[]')

        json_empty = Base.to_json_string([])
        self.assertEqual(json_empty, '[]')

        json_dictionnary_1 = Base.to_json_string([ { 'id': 12 }])
        self.assertEqual(json_dictionnary_1, '[ { "id": 12 }]')

if __name__ == '__main__':
    unittest.main()

