#!/usr/bin/python3
for element in range(0, 100):
    if (element == 99):
        print("{:02d}".format(element))
    else:
        print("{:02d}".format(element), end=", ")
