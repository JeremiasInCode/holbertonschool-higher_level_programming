#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None:
        return
    for element in my_list:
        print("{:d}".format(element))
