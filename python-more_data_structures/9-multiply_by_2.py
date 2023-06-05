#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = a_dictionary.copy()
    for index in a_dictionary:
        new_list[index] = new_list[index] * 2 
    return new_list
