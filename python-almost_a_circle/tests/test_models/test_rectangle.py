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

        r2.x = 11
        self.assertEqual(r2.x, 11)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)


if __name__ == "__main__":
    unittest.main()