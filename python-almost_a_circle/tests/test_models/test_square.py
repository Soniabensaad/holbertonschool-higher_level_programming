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

    def test_update(self):
        """update(self, *args, **kwargs)"""
        s = Square(1, 1, 2, 5)
        s.update()
        self.assertEqual(s, s)

        s = Square(1, 1, 2, 5)
        s.update(98)
        self.assertEqual(s, s)

        s = Square(1, 1, 2, 5)
        s.update(89, 1)
        self.assertEqual(s, s)

        s = Square(1, 1, 2, 5)
        s.update(89, 1, 2)
        self.assertEqual(s, s)

        s = Square(1, 1, 2, 5)
        s.update(89, 1, 2, 3)
        self.assertEqual(s, s)

        s = Square(1, 1, 2, 5)
        s.update(**{'id': 89})
        self.assertEqual(s, s)

        s = Square(1, 1, 2, 5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s, s)

        s = Square(1, 1, 2, 5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s, s)

        s = Square(1, 1, 2, 5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s, s)

    def test_create_square(self):
        """test for Dictionary to Instance"""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s, s)

        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s, s)

        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s, s)

    def test_to_dict_rectangle(self):
        r1 = Square(10, 2, 1)
        r1_dictionary = r1.to_dictionary()
        r_dictionary = {'x': 1, 'y': 9, 'id': 2, 'size': 1}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Square(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(r1 == r2)

    def test_str_square(self):
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(str(r1), "[Square] (12) 2/1 - 4")

    def test_save_to_file_rectangle(self):
     
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            s = file.read()
            self.assertEqual(s, '[]')

        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertEqual(
                f.read(), '[{"id": 1, "x": 0, "size": 1, "y": 0}]')

        Square.save_to_file(None)
        with open("Square.json", mode="r") as file:
            s = file.read()
            self.assertEqual(s, '[]')

    def test_load_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        s = [s1, s2]

        Square.save_to_file(s)

        s = Square.load_from_file()
        self.assertEqual(s, s)

    def test_display(self):
       
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(9, 6)
            r1.display(9)
        self.assertEqual(
            "display() takes 1 positional argument but 2 were given", str(
                x.exception))


