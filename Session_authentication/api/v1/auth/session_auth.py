#!/usr/bin/env python3
""" Session Authorization module
"""
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Session Authorization class
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create a session id for a user
        """

        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id.update({session_id: user_id})
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ retrieve user id associated with session_id
        """

        if session_id is None or type(session_id) is not str:
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """ return the authenticated user
        """

        sesh_cookie = self.session_cookie(request)
        print("Cookie: "+sesh_cookie)
        user_id = self.user_id_for_session_id(sesh_cookie)
        print("ID: "+str(user_id))
        user = User.get(user_id)
        return user
