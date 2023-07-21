#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Function displays a given string"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function displays a given string"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_Text(text):
    """Function displays C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_Text(text="is cool"):
    """Function displays Python, followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """Function displays n is a number, only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """Function displays a HTML page only if n is an integer"""
    return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even(n):
    """Function displays a HTML page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
