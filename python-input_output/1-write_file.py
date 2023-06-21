#!/usr/bin/python3
""" Task 1 """


def write_file(filename="", text=""):
    """ Write a file """
    with open(filename, mode="w+") as MyFile
        MyFile.write(text)
    return len(text)
