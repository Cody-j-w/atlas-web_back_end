#!/usr/bin/env python3
""" Redis exercise module
"""

import redis
import uuid
from typing import Union, Callable
from redis.commands.core import CoreCommands
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ decorator that counts calls of decorated callable
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        wrapped_redis = args[0]._redis
        wrapped_redis.incr(method.__qualname__)
        return method(*args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ decorator tracks history of decorated callable
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        key_in = method.__qualname__+":inputs"
        key_out = method.__qualname__+":outputs"
        self = args[0]
        self._redis.rpush(key_in, str(args[1:]))
        output = method(*args, **kwargs)
        self._redis.rpush(key_out, output)
        return output
    return wrapper


def replay(method: Callable):
    """ print's a method's call history
            method: a method or function, decorated with @count_calls and
            @call_history
    """
    temp_redis = redis.Redis()
    count_key = str(method.__qualname__)
    count = temp_redis.get(count_key).decode('utf-8')
    print(f"{count_key} was called {count} times:")
    in_key = count_key+":inputs"
    out_key = count_key+":outputs"
    inputs = temp_redis.lrange(in_key, 0, -1)
    outputs = temp_redis.lrange(out_key, 0, -1)
    throughput = list(zip(inputs, outputs))
    for i in range(int(count)):
        inp = throughput[i][0].decode('utf-8')
        outp = throughput[i][1].decode('utf-8')
        print(f"{count_key}(*{inp}) -> {outp}")


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
        """ store data in redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(self, key: str, fn: Callable = None):
        """ retrieve data from redis
        """
        if key is not None:
            if fn is not None:
                return fn(self._redis.get(key))
            return self._redis.get(key)

    @count_calls
    def get_str(self, val: bytes):
        """ convert to str
        """
        return str(val)

    @count_calls
    def get_int(self, val: bytes):
        """ convert to int
        """
        return int(val)
