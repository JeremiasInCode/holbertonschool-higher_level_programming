#!/usr/bin/python3
import unittest

from is_same_class import is_same_class
""" Unittest for is_same_class(obj, a_class) """

class TestMaxNumber(unittest.TestCase):
    """ Test cases bases for is_same_class function """

    def test_positive(self):
        a = 1
        result = is_same_class(a, int)
        self.assertEqual(result, True)

    def test_string(self):
        a = 'False'
        result = is_same_class(a, int)
        self.assertEqual(result, False)
    
    def test_negative(self):
        a = -20
        result = is_same_class(a, int)
        self.assertEqual(result, True)

    if __name__ == "__main__":
        unittest.main()
