#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if (a_dictionary == []):
        return

    if key in a_dictionary:
        a_dictionary.update({key: value})
    else:
        a_dictionary[key] = (value)
    return (a_dictionary)
