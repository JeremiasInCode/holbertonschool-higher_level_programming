#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multiply_of_two = my_list.clear()

    if (len(my_list) == 0 or my_list == []):
        return None

    add_true = multiply_of_two.append(True)
    add_false = multiply_of_two.append(False)
    
    for element in my_list:
        add_true if element % 2 == 0 else add_false

    return (multiply_of_two)
