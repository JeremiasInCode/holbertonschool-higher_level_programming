#!/usr/bin/python3
def element_at(my_list, idx):
    lenghtArr = len(my_list)

    if idx >= lenghtArr or idx < 0:
        return None

    for element in my_list:
        if (element == idx):
            return (my_list[element])
