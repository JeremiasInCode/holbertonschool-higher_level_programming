#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if (my_list is None):
        return

    my_list = my_list[::-1]
    
    for element in len(my_list):
        print("{:d}".format(my_list[element]))
