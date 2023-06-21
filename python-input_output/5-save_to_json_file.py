#!/usr/bin/python3
""" Task 5 """
import json


def save_to_json_file(my_obj, filename):
    """ Save the json to the file """
    json_represent = json.dumps(my_obj)
    with open(filename, 'w') as f:
        return f.write(json_represent)
