#!/usr/bin/python3
"""Module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
#from models import storage_type
from os import getenv
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models

    Attributes:
        id: The BaseModel id.
        created_at: The datetime at creation.
        updated_at: The datetime of last update.
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key != '__class__':
                    setattr(self, key, kwargs[key])

            #if storage_type == 'db':
            if getenv('HBNB_TYPE_STORAGE') == 'db':
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                    if not hasattr(kwargs, 'created_at'):
                        setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        c_name = self.__class__.name__
        return '[{}] ({}) {}'.format(c_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        for k in dict:
            if type(dict[k]) is datetime:
                dict[k] = dict[k].isoformat()
        if '_sa_instance_state' in dict.keys():
            del(dict['_sa_instance_state'])
        return dict

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
