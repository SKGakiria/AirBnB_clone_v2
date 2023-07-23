#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id")), Column("amenity_id",
                                         String(60), ForeignKey(
                                             "amenities.id")))


class Place(BaseModel, Base):
    """ A place to stay """
    """ This class inherits from Base and links to MySQL
    table - places """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place",
                           cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             backref="place", viewonly=False,
                             overlaps="amenities,place")

    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Return a list of reviews instances"""
            rev_list = []
            # iterate through values in storage(Review)
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    rev_list.append(review)
            return rev_list

        @property
        def amenities(self):
            """ Return a list of Amenities"""
            from models import storage
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
