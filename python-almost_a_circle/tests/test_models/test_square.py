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
        s1 = Square(5, 3, 4)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 2)

    def test_attributes_wrong(self):
        """Test square class: check for wrong attributes."""

        with self.assertRaises(TypeError) as x:
            s = Square("1", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(1, "2")
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(1, 2, "3")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(-1)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(1, -2)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(1, 2, -3)
        self.assertEqual("y must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(0)
        self.assertEqual("width must be > 0", str(x.exception))

