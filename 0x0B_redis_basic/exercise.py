#!/usr/bin/env python3
""" Redis exercise module
"""

import redis
import uuid
from typing import Union, Callable


class Cache:
    """ Redis Cache class
    """

    def __init__(self) -> None:
        self._redis = redis.Redis(host='localhost',
                                  port=6379)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        if key is not None:
            if fn is not None:
                return fn(self._redis.get(key))
            return self._redis.get(key)

    def get_str(self, val: bytes):
        return str(val)

    def get_int(self, val: bytes):
        return int(val)