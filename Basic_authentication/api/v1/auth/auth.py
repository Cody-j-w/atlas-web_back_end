#!/usr/bin/env python3
""" Module of auth methods
"""
from flask import request
from typing import List

class Auth():
    """ Auth class
        Contains methods for authenticating users
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ return a route's auth requirement
        """
        return False


    def authorization_header(self, request=None) -> str:
        """ return an auth header
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ return the current user object
        """
        return None