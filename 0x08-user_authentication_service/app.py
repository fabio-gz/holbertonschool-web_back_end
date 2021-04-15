#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """Logout function"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not session_id or not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """profile function"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not session_id or not user:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """Get reset password token"""
    try:
        email = request.form.get("email")
        reset_t = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_t}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
