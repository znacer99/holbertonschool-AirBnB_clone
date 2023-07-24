#!/usr/bin/python3
import json
import os
from datetime import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON files to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""

        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key
        <obj class name>.id.
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        (path: __file_path).
        """

        serializes_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    class_obj = eval(class_name)
                    self.__objects[key] = class_obj(**value)
