#!/usr/bin/python3
""" Task 0 """


def read_file(filename=""):
    """ Read a file """
    with open(filename, 'r') as f:
        for line in f.readlines():
            print(f"{line}", end="")
