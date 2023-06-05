#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    separator = " "
    for row in matrix:
        print(separator.join("{:d}".format(element) for element in row))
