#!/usr/bin/env python3
"""Flask app module
"""

from flask import Flask, jsonify, abort, request, redirect
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ base route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """ User registration route
    """
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ User login route
    """
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        AUTH.create_session(email)
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ User logout route
    """
    session = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/', 302)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
