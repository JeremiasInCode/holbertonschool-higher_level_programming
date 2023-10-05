#!/usr/bin/python3
""" Task 6 """
import json


def load_from_json_file(filename):
    with open(filename) as f:
        data_obj = json.load(f)
    return data_obj
