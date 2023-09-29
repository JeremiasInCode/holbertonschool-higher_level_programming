#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for element in range(x):
            print(("{:d}".format(my_list[element])), end="")
    except Exception:
        # space if it failed
        print()
        return element
    # space if it success
    print()
    return x
