#!/usr/bin/env python3
"""
Password encryption module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ encode and encrypt a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
