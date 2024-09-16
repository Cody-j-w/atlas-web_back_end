#!/usr/bin/env python3
""" Module of auth methods
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Auth class
        Contains methods for authenticating users
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ return a route's auth requirement
        """
        if path is not None and excluded_paths is not None:
            for route in excluded_paths:
                if path == route or path + "/" == route:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ return an auth header
        """
        if request is None:
            return None
        else:
            if 'Authorization' not in request.headers:
                return None
            else:
                return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ return the current user object
        """
        return None

    def session_cookie(self, request=None):
        """ retrieve session cookie
        """

        if request is None:
            return None
        cookie = request.cookies.get(os.getenv('SESSION_NAME'))
        return cookie
