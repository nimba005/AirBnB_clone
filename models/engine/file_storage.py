#!/usr/bin/env python3
''' Module that serializes and deserializes '''

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''serialize and deserialize objects '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary of objects """
        return (FileStorage.__objects)

    def new(self, obj):
        """sets objs with keys"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objs to json files"""
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes json file to obj"""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for j in obj_dict.values():
                    cls_name = j["__class__"]
                    del j["__class__"]
                    self.new(eval(cls_name)(**j))
        except FileNotFoundError:
            return
