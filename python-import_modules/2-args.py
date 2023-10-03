#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    element = 0
    if length == 0:
        print("{} arguments.".format(length))
    elif (length == 1):
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))
    if (length > element):
        for element in range(1, length + 1):
            print("{0}: {1}".format(element, sys.argv[element]))
