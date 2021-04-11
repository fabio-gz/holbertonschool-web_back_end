#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Function: set up a basic Flask app"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
