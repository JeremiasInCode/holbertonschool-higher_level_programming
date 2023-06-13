#!/usr/bin/python3
"""Task 0"""


def add_integer(a, b=98):
    """Add two integers"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    else:
        a_int = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        b_int = int(b)
    return a_int + b_int
