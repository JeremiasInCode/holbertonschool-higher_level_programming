#!/usr/bin/python3
""" Test for base class """
import unittest
from models import Base


class TestBase(unittest.TestCase):
    """ Test base class """
    def test_id(self):
        """ id test """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base(10)
        self.assertEqual(obj3.id, 10)
        obj4 = Base(-20)
        self.assertEqual(obj4, -20)

    def test_to_json_string(self):
        """ convert list to json - test """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), {"id": 1})
        self.assertEqual(Base.to_json_string([False]), False)

    def test_from_json_string(self):
        """ convert json to list - test"""
        self.assertAlmostEqual(Base.from_json_string(None), [])
        self.assertAlmostEqual(Base.from_json_string("[]"), [])
        test = Base.from_json_string('[{ "id": 30 }]')
        self.assertAlmostEqual(test, [{"id": 30}])

    if __name__ == "__main__":
        unittest.main()
