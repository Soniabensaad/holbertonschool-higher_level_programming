import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    
    def setUp(self):
        Base._Base__nb_objects = 0
    def test_id(self):

        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(3, 4, 5)
        self.assertEqual(r2.id, 3)
        r3 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r3.id, -5)
        r4 = Rectangle(10, 2, 4, 5, 30)
        self.assertEqual(r4.id, 30)
        

    def test_width_height_x_y(self):

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 2, 4, 5, 24)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)
