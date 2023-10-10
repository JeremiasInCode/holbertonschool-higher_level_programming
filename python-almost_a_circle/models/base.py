#!/usr/bin/python3
"""Task 1"""
import json


class Base:
    """ Define a private attribute """
    __nb_objects = 0
    """ Class constructor"""
    def __init__(self, id=None):
        """
            Initialize an instance abd verify if id is None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert a list of dictionaries to Json format """
        if not list_dictionaries:
            return "[]"

        json_data = json.dumps(list_dictionaries)
        return json_data

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert a list of dictionaries to Json format """
        if not list_dictionaries:
            return "[]"

        json_data = json.dumps(list_dictionaries)
        return json_data

    @staticmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        name_class = cls.__name__ + "json"
        dict_list = []
        for obj in list_objs:
            dictionary_element = obj.to_dictionary()
            dict_list.append(dictionary_element)
