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
        return False


    def authorization_header(self, request=None:request) -> str:
        return None


    def current_user(self, request=None:request) -> TypeVar('User'):
        return None