#!/usr/bin/env python3
"""
Password encryption module
"""

import bcrypt
from typing import ByteString


def hash_password(password: str) -> ByteString:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
