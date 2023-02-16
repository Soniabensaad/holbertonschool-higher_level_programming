import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square(self):
        s0 = Square(1)
        self.assertEqual(s0.width, 1)
        s2 = Square(1, 2)
        self.assertEqual(s2.x, 2)
        s1 = Square(5, 3, 4)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 2)

    def test_attributes_square_(self):
        """checks for wrong attributes."""

        with self.assertRaises(TypeError) as x:
            s4 = Square("1")
        self.assertEqual(str(x.exception), "width must be an integer")

        with self.assertRaises(TypeError) as x:
            s5 = Square(1, "2")
        self.assertEqual(str(x.exception), "x must be an integer")

        s6 = Square(1, 2, 3, 4)
        self.assertEqual(s6.id, 4)

        with self.assertRaises(ValueError) as x:
            s7 = Square(-1)
        self.assertEqual(str(x.exception), "width must be > 0")

        with self.assertRaises(ValueError) as x:
            s8 = Square(1, -2)
        self.assertEqual(str(x.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as x:
            s9 = Square(1, 2, -3)
        self.assertEqual(str(x.exception), "y must be >= 0")

        with self.assertRaises(ValueError) as x:
            s10 = Square(0)
        self.assertEqual(str(x.exception), "width must be > 0")

        with self.assertRaises(TypeError) as x:
            s11 = Square(1, 2, "3")
        self.assertEqual(str(x.exception), "y must be an integer")