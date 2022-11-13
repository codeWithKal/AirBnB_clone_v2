#!/usr/bin/python3
"""
File: 0-hello_route.py
Author: Kaleab Shiferaw Girma
Discreption: A script that starts flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    A method that greets
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
