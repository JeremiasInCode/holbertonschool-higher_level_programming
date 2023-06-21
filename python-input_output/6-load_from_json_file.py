#!/usr/bin/python3
""" Task 6 """
import json


def load_from_json_file(filename):
    """ To creates a object from Json file """
    with open(filename) as f:
        data_json = json.loads(f)
    return data_json
