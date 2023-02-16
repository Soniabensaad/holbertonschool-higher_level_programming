import unittest
from models.base import Base
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    
    def setUp(self):
        Base._Base__nb_objects = 0
    def test_id(self):
        """test id"""

        r0 = Rectangle(1, 2)
        self.assertEqual(r0.id, 1)
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 3)
        r3 = Rectangle(10, 2, 0, 0, 11)
        self.assertEqual(r3.id, 11)
        r4 = Rectangle(10, 2, 4, 5, 30)
        self.assertEqual(r4.id, 30)
        r5 = Rectangle(10, 2, 4, 5, -3)
        self.assertEqual(r5.id, -3)
        r6 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(r6.id, 9)

    def test_width_height_x_y(self):
        """test attributes class"""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 2, 4, 5, 11)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)
    
    def test_attributes_wrong(self):
        """Test Rectangle class: check for wrong attributes."""

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle("a", 2)
        self.assertEqual("width must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r2 = Rectangle(2, "b")
        self.assertEqual("height must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r3 = Rectangle(1, 2, "c", 3)
        self.assertEqual("x must be an integer", str(x.exception))

        with self.assertRaises(TypeError) as x:
            r4 = Rectangle(1, 2, 2, "d")
        self.assertEqual("y must be an integer", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r5 = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r6 = Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r7 = Rectangle(2, -1)
        self.assertEqual("height must be > 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r8 = Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(x.exception))

        with self.assertRaises(ValueError) as x:
            r9 = Rectangle(2, 8, 9, -6)
        self.assertEqual("y must be >= 0", str(x.exception))
    
    def test_area(self):
        """checks for the area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(11, 2)
        self.assertEqual(r2.area(), 22)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_update_rectangle(self):
        """checks update"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)

    



