#!/usr/bin/python3

"""
The script that starts a Flask web application
"""
import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    return a hello message
    """
    return "Hello HBNB!"
