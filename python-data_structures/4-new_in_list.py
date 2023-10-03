#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    lenghtArr = len(my_list)
    if not my_list or idx < 0 or idx >= lenghtArr:
        return my_list

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
