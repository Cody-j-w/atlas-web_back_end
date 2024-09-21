#!/usr/bin/env python3
"""auth module
"""

import bcrypt
import uuid
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

    def valid_login(self, email: str, password: str) -> bool:
        """ determine validity of a login attempt
        """
        try:
            user = self._db.find_user_by(email=email)
            checked_pw = password.encode('utf-8')
            hashed_pw = user.hashed_password
            return bcrypt.checkpw(checked_pw, hashed_pw)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ creates a new session ID
        """

        try:
            user = self._db.find_user_by(email=email)
            new_session = _generate_uuid()
            self._db.update_user(user.id, session_id=new_session)
            session_user = self._db.find_user_by(session_id=new_session)
            return session_user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Retrieve a user based on session id
        """

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroy a user session
        """

        self._db.update_user(user_id, session_id=None)


def _hash_password(password: str) -> bytes:
    """ hash and salt a password string
    """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ generate a new UUID
    """

    return str(uuid.uuid4())
