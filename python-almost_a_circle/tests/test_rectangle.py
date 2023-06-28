import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle1 = Rectangle(5, 10)
        self.rectangle2 = Rectangle(7, 3, 2, 4, 1)

    def test_area(self):
        self.assertEqual(self.rectangle1.area(), 50)
        self.assertEqual(self.rectangle2.area(), 21)

    def test_display(self):
        expected_output = "#######\n" \
                          "#######\n" \
                          "#######\n"
        self.assertEqual(self.rectangle1.display(), expected_output)

    def test_update(self):
        self.rectangle1.update(2, 8, 6, 1, 2)
        self.assertEqual(self.rectangle1.width, 8)
        self.assertEqual(self.rectangle1.height, 6)
        self.assertEqual(self.rectangle1.x, 1)
        self.assertEqual(self.rectangle1.y, 2)


if __name__ == '__main__':
    unittest.main()
