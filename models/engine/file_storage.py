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
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes json file to obj"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
