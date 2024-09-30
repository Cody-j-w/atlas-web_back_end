#!/usr/bin/env python3
""" Redis exercise module
"""

import redis
import uuid
from typing import Union, Callable
from redis.commands.core import CoreCommands
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args, **kwargs):
        wrapped_redis = args[0]._redis
        wrapped_redis.incr(method.__qualname__)
        return method(*args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args, **kwargs):
        key_in = method.__qualname__+":inputs"
        key_out = method.__qualname__+":outputs"
        self = args[0]
        self._redis.rpush(key_in, str(args))
        output = method(*args, **kwargs)
        self._redis.rpush(key_out, output)
        return output
    return wrapper


class Cache:
    """ Redis Cache class
    """

    def __init__(self) -> None:
        self._redis = redis.Redis(host='localhost',
                                  port=6379)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(self, key: str, fn: Callable = None):
        if key is not None:
            if fn is not None:
                return fn(self._redis.get(key))
            return self._redis.get(key)

    @count_calls
    def get_str(self, val: bytes):
        return str(val)

    @count_calls
    def get_int(self, val: bytes):
        return int(val)
