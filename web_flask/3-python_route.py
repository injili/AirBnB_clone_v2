#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Returns Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnbb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun():
    """Returns "C" followed by text that's been passed"""
    response = "C {}".format(text.replace("_", " "))
    return response


@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(test):
    """Returns "Python "followed by the text passed
    If no text is passedit returns Python is cool"""
    if text:
        response = "Python {}".format(text.replace("_", " "))
    else:
        response = "Python Is cool"

    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
