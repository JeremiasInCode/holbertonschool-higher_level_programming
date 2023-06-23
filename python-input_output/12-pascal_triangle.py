#!/usr/bin/python3
""" Task 12 """


def pascal_triangle(n):
    """Implement pascal algoritm"""

    triangle = []
    row = [1]
    cero = [0]

    for element in range(n):
        triangle.append(row)
        """
            row + cero - Example: [1, 2, 1] + cero = [1, 2, 1, 0].
            cero + row - Example: cero + [1, 2, 1] = [0, 1, 2, 1].
            Zip: Combines the elements of the two lists in pairs.
            Element + d: Add the pairs.
        """
        row = [element + d for element, d in zip(row + cero, cero + row)]
    return triangle
