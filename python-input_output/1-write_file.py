#!/usr/bin/python3
""" Task 1 """


def write_file(filename="", text=""):
    """ Write a file """
    with open(filename, 'w') as f:
        return f.write(text)
