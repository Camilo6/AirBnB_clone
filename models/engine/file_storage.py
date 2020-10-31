#!/usr/bin/python3
""" Module class Filestorage """


import json


class FileStorage:
    """ Class convert to JSON """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """  Sets in __objects the obj with key """
        self.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file"""
        js_cp = {}
        for key in self.__objects:
            js_cp[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as fl:
           json.dump(js_cp, fl)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as fl:
                for line in fl:
                    dz = json.loads(line)
        except :
            pass