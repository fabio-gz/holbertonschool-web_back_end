#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """Class: Configure available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel(app)
app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """simple home page"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
