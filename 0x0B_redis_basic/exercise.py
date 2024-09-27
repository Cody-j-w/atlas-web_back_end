#!/usr/bin/env python3
""" Redis exercise module
"""

import redis
import uuid
from typing import Union


class Cache:
    """ Redis Cache class
    """

    def __init__(self) -> None:
        self._redis = redis.Redis(host='localhost',
                                  port=6379,
                                  decode_responses=True)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
