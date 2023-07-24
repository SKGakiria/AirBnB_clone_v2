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


@app.route('/states', strict_slashes=False)
def state_list():
    """Function that displays list of States"""
    states = storage.all(State)
    return (render_template("9-states.html", states=states,
            mode="all"))


@app.route('/states/<id>', strict_slashes=False)
def city_state_id(id):
    """Function that displays list of cities linked to the state"""
    for state in storage.all(State).values():
        if state.id == id:
            return (render_template("9-states.html", states=state, mode='id'))
    return (render_template("9-states.html", states=state, mode='none'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
