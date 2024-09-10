#!/usr/bin/env python3
"""
Password encryption module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ encode and encrypt a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ tell whether a provided password is a valid password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
