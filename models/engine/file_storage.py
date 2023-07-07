#!/usr/bin/python3
'''new class'''
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''all func'''
        return FileStorage.__objects

     def new(self, obj):
         '''new func'''
         name_clas = obj.__class__.__name__
         key = name_clas + "." + obj.id
         FileStorage.__objects[key] = obj
         return True

     def save(self):
         with open(FileStorage.__file_path, 'w') as f:
             new_dict = {}
             x = self.all()
             for element in x:
                 new_dict[element] = x[element].to_dict()
             f.write(json.dumps(new_dict))
         return True

     def reload(self):
         if os.path.exists(FileStorage.__file_path):
             with open(FileStorage.__file_path, 'r') as f:
                 content = f.read()
                 if len(content) != 0:
                     obj = json.loads(content)
                     for key, value in obj.items():
                         value = eval(value['__class__'])(**value)
                         FileStorage.new(self, value)
         return True

    def file_path(self):
        return FileStorage.__file_path
