#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]

    if len(my_list) == 0 or my_list == []:
        return None

    for element in my_list:
        if element > max_value:
            max_value = element

    return max_value
