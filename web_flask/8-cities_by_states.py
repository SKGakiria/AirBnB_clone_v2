#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def td_database(self):
    """Function to remove current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_state_list():
    """Function that displays list of States and their Cities"""
    states = storage.all(State)
    return (render_template("8-cities_by_states.html", states=states))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
