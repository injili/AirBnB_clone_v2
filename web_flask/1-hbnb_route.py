#!/usr/bin/python3

"""
The script that starts a Flask web application
"""
from flask import Flask


app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """
    return a hello message
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns a hbnb message
    """
    return ("HBNB")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
