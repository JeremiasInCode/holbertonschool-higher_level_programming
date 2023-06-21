#!/usr/bin/python3
""" Task 7 """
import json
""" arguments """
import sys

save_to_json_file = __import__('save_to_json_file').save_to_json_file
load_from_json_file = __import__('load_from_json_file').load_from_json_file

try:
    with open('add_item.json') as f:
        data_obj = load_from_json_file('add_item.json')
except FileNotFoundError:
    data_obj = []

data_obj.extend(args)
save_to_json_file(data_obj, 'add_item.json')
