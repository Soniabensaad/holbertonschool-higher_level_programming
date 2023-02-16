
#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_new_Rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, 6)

        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)