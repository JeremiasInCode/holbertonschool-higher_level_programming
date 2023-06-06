#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list == []:
        return
    try:
        for element in range(x):
            print(("{:d}".format(my_list[element])), end="")
    except Exception:
        print() # space if it failed
        return element
    print() # space
    return x
