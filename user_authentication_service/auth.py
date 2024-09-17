#!/usr/bin/env python3
"""auth module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """ hash and salt a password string
    """

    return bcrypt.hashpw(password, bcrypt.gensalt())