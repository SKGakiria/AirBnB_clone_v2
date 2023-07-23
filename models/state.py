#!/usr/bin/python3
"""State Module for the HBNB project"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
import models


class State(BaseModel, Base):
    """Represents the State class"""
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='delete')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns listings of City instances with state_id
                equals the current State.id"""
            from models import storage
            rel_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    rel_cities.append(city)
            return rel_cities
