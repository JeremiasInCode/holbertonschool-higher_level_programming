#!/usr/bin/python3

def no_c(my_string):
    if not my_string:
        return my_string

    new_string = ""
    for character in my_string:
        if character.lower() != 'c' and character.upper() != 'C':
            new_string += character

    return new_string
