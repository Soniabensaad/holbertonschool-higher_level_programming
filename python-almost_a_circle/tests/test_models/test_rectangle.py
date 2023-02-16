#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest


class TestRectangle (unittest.TestCase):

    def test_simple_using(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.height, 10)
