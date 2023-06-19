#!/usr/bin/python3
import unittest
Rectangle = __import__('2-rectangle')

class TestArea(unittest.TestCase):
    """ Test cases bases for area function """
    def test_negative(self):
        # Crear instancias de Rectangle con diferentes dimensiones
        rectangle1 = Rectangle(5, 10)
        rectangle2 = Rectangle(3, 7)
        rectangle3 = Rectangle(0, 0)

        # Calcular el área de cada rectángulo
        area1 = rectangle1.area()
        area2 = rectangle2.area()
        area3 = rectangle3.area()

        # Verificar que el área calculada sea correcta
        self.assertEqual(area1, 50)
        self.assertEqual(area2, 21)
        self.assertEqual(area3, 0)
    
    if __name__ == "__main__":
        unittest.main()
