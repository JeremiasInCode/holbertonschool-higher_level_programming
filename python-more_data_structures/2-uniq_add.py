#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return

    acc = 0
    new_list = []

    for element in my_list:
        if element in new_list:
            continue
        new_list.append(element)

    for item in new_list:
        acc = acc + item

    return acc
