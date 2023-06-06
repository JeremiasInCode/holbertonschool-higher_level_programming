#!/usr/bin/python3
def safe_print_integer(value):
    if not value:
        return
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        return False
