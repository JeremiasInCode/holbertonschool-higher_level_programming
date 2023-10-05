#!/usr/bin/python3
""" Task 11 """


class Student:
    def __init__(self, first_name, last_name, age):
        """ Initialization of attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a JSON representation of a dictionary of Student class"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for element in attrs:
                if hasattr(self, element):
                    new_dict[element] = getattr(self, element)
                    if new_dict[element] is AttributeError:
                        continue
            return new_dict

    def reload_from_json(self, json):
        for element in json:
            """Verify that the attribute exist in the class instance"""
            if hasattr(self, element):
                """
                    Sets the name of the element and
                    the value of itself.
                """
                setattr(self, element, json[element])
