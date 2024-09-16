#!/usr/bin/env python3
""" Session Authorization module
"""
from flask import request
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session Authorization class
    """
