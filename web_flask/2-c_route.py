#!/usr/bin/python3
"""
Display custom text and C, C is fun
"""
from flask import Flask

app = Flask("__name__")


@app.route('/')
def hello():
    """
    Displays Hello HBNB
    """
    return ("Hello HBNB")


@app.route('/hbnb')
def hbnb():
    """
    Displays HBNB when called
    """
    return ("HBNB")


@app.route('/c/<text>')
def c_ic_fun(text):
    """
    Displays C followed by the value in 'text'
    """
    response = 'C {}'.format(text)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', strict_slashes=False)
