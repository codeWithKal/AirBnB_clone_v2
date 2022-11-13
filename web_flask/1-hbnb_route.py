#!/usr/bin/python3
"""
File: 1-hbnb_route.py
Author: Kaleab Shiferaw Girma
Description: a python script that runs a flask on port number 5000
    also can routes to two routes.
"""
from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
