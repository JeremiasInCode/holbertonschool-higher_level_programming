#!/usr/bin/python3
""" Task 12 """


def pascal_triangle(n):
    """Implement pascal triangle in a algoritm"""

    triangle = []
    row = [1]
    cero = [0]

    concat1 = row + cero
    concat2 = cero + row

    pairs = zip(concat1, concat2)
    add = [element + d for element, d in pairs]
    triangle.append(add)
    return triangle
