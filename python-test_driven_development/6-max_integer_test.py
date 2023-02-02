import unittest
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def empty_test_list(self):
        self.assertEqual(max_integer([]), None)
    def test_one_element(self):
        self.assertEqual(max_integer([3]), 3)
    def test_positive_elements(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
    def test_mixed_elements(self):
        self.assertEqual(max_integer([-2, -1, 3, 4]), 4)
    def test_negative_elements(self):
        self.assertEqual(max_integer([-1, -2, -3, -5]), -1)
if __name__ == '__main__':
    unittest.main()
