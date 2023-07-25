#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def td_database(self):
    """Function to remove current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function displays the HTML page with filters."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return (render_template("100-hbnb.html",
                            states=states, amenities=amenities,
                            places=places))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
