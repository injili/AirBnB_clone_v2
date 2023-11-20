#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    Returns "Python" followed by the text passed
    If no text is passedit returns Python is cool
    """
    response = "Python {}".format(text.replace("_", " "))
    return response


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """is n an integer?"""
    if isinstance(n, int):
        return ("{} is a number".format(n))
    else:
        abort(404)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """if n is an integer display a HTML page"""
    if isinstance(n, int):
        return render_template('5-number.html', my_int=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """if n is an integer the HTML page is rendered"""
    response = ""
    if isinstance(n, int):
        if n % 2 == 0:
            response = "even"
        else:
            response = "odd"
        return render_template('6-number_odd_or_even.html',
                               my_int=n, response=response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
