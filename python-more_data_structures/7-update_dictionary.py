#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if (a_dictionary == []):
        return
    for element in a_dictionary:
        if element in a_dictionary:
            a_dictionary.update({element: value})
        else:
            a_dictionary[element] = value
    return (a_dictionary)
