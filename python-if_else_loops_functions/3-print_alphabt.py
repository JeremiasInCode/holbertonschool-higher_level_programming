#!/usr/bin/python3
for element in range(97, 123):
    if (chr(element) == 'q' or chr(element) == 'e'):
        continue
    print("{}".format(chr(element)), end="")
