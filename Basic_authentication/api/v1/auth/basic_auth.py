#!/usr/bin/env python3
""" Module of auth methods
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth class
        Contains methods for authenticating users
    """

    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """ Extract an authorization header
        """
        if auth_header is None or type(auth_header) is not str:
            return None
        if auth_header.split(" ")[0] != 'Basic':
            return None
        return auth_header.split(" ")[1]


    def decode_base64_authorization_header(self, auth_header_64: str) -> str:
        """ decode base64 string
        """
        if auth_header_64 is None or type(auth_header_64) is not str:
            return None
        try:
            result = base64.b64decode(auth_header_64).decode('utf-8')
        except base64.binascii.Error:
            result = None
        return result
