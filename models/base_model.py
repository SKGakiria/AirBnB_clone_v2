#!/usr/bin/python3
"""Module defines a base class for all models in our hbnb clone"""
import uuid
from os import getenv
from datetime import datetime
from sqlalchemy import Column, String, DateTime
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
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        from models import storage
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

        if not self.id:
            self.id = str(uuid.uuid4())

        t = datetime.now()
        if not self.created_at:
            self.created_at = t
            self.updated_at = t
        if not self.updated_at:
            self.updated_at = t

            # if storage_type == 'db':
            if getenv('HBNB_TYPE_STORAGE') == 'db':
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                    if not hasattr(kwargs, 'created_at'):
                        setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        c_name = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(c_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if my_dict.get('_sa_instance_state'):
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
