#!/usr/bin/python3
"""Unittest base.
Test cases for class Base.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_new_instance_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_specified_id(self):
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_to_json_string_none(self):
        rjson = Base.to_json_string(None)
        self.assertEqual(rjson, '[]')

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

        json_dictionary = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_dictionary, '[{"id": 12}]')

    def test_from_json_string(self):
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

if __name__ == '__main__':
    unittest.main()