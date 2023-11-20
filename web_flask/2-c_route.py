#!/usr/bin/python3
"""
Display custom text and C, C is fun
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Displays Hello HBNB
    """
    return ("Hello HBNB")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays HBNB when called
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Displays C followed by the value in 'text'
    """
    response = 'C {}'.format(text.replace("_", " "))
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
