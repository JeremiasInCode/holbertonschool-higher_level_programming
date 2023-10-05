#!/usr/bin/python3
""" Task 4 """
import json


def from_json_string(my_str):
    """ Json to a object (deserealize) """
    return json.loads(my_str)
