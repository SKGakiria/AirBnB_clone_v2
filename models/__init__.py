#!/usr/bin/python3
"""This module instantiates an instance of the Storage that will be used"""
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


#storage_type = getenv('HBNB_TYPE_STORAGE')

#if storage_type == 'db':
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
