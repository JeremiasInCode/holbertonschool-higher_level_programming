#!/usr/bin/python3
combinations = []

for first in range(10):
    for second in range(first + 1, 10):
        combinations.append("{}{}".format(first, second))

print(", ".join(combinations))

