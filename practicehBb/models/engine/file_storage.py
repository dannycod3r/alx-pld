#!/usr/bin/python3
"""Module file storage"""
import json

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """class File storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dict __objects"""
        return self.__objects

    def all_classes(self):
        """return a list of class names"""
        classes = set()
        for key in self.__objects.keys():
            class_name = key.split('.')[0]
            classes.add(class_name)
        return list(classes)

    def new(self, obj):
        """ sets in __objects the obj with key
        <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the
        JSON file (path: __file_path)"""
        """Serializes __objects to the JSON file"""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = key.split('.')[0]
                    cls = eval(class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
