#!/usr/bin/python3
""" Task 12 """

def pascal_triangle(n):
    """Implement pascal triangle in an algorithm"""

    triangle = []

    for _ in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            new_row = [sum(pair) for pair in zip(last_row, last_row[1:])]
            row.extend(new_row)
            row.append(1)

        triangle.append(row)

    return triangle
