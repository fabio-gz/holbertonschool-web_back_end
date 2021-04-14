#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request, abort
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """json payload"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """register an user"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"message": "email required"}), 400
    elif not password:
        return jsonify({"message": "password required"}), 400
    try:
        new = AUTH.register_user(email, password)
        created = {"email": "{}".format(new.email),
                   "message": "user created"}
        return jsonify(created), 200
    except Exception:
        return jsonify({'message': 'email already registered'}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """login post route"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)
    else:
        session = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session)
        return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
