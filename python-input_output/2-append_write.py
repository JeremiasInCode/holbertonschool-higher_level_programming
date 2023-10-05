#!/usr/bin/python3
""" Task 2 """


def append_write(filename="", text=""):
    """ Append text at the end of the file """
    with open(filename, 'a') as f:
        return f.write(text)
