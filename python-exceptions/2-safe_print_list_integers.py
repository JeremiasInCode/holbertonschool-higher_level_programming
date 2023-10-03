#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # return in silence
    counter = 0
    try:
        for element in range(x):
            if isinstance(my_list[element], int):
                print(("{:d}".format(my_list[element])), end="")
                counter += 1
    except Exception:
        return
    # space if it success
    print()
    return counter
