#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = []
    for index, element in enumerate(a_dictionary):
        multiply = element * 2
        new_list[index] = multiply
    return new_list
