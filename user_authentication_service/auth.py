#!/usr/bin/env python3
"""auth module
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register a new user
        """

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)


def _hash_password(password: str) -> bytes:
    """ hash and salt a password string
    """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
