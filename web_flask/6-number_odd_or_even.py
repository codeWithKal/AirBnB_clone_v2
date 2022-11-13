#!/usr/bin/python3
"""
File: 6-number_odd_or_even.py
Author: Kaleab Shiferaw Girma
Description: a python script that runs a flask on port number 5000
    also can routes to two routes.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root_route():
    """
    A method that routes to the root and displayes Hello HBNB
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """
    A method that displayes HBNB only
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def var_in_route(text):
    """
    A method that prints C and concatenate the argument passed to it
    it also replaces a _ with space
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def var_with_dflt(text="is cool"):
    """
    A method that uses a default value for an argument
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number_template/<int:n>", strict_slashes=False)
def htm_render(n):
    """
    A method that render a templet if the argument is an integer
    """
    return render_template("5-number.html", n=n)


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    """
    A method that prints if the argument is only an integer
    """
    return "{} is a number".fiormat(n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    A method that tests for the oddeness or eveness of a number if the
    argument passed is an integer
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
