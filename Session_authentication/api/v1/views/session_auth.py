#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ log a user in
    """
    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': email})
    if len(user) == 0:
        return jsonify({ "error": "no user found for this email" }), 400
    from api.v1.app import auth
    sesh_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    response.set_cookie(getenv('SESSION_NAME'), user[0].id)
    return response
