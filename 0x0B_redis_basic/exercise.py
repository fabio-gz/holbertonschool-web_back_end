#!/usr/bin/env python3
"""string to redis"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """increments the count for the key"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wraper for count calls"""
        self._redis.incr(key)
        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ store the history of inputs and outputs"""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper for call history"""
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        outputs = str(method(self, *args, **kwds))
        self._redis.rpush(method.__qualname__ + ":outputs", outputs)

        return outputs

    return wrapper


def replay(method: Callable):
    """display the history of calls of a particular function."""
    r = method.__self__._redis
    qua_name = method.__qualname__
    number_calls = r.get(qua_name).decode("utf-8")

    inputs = r.lrange(f"{qua_name}:inputs", 0, -1)
    outputs = r.lrange(f"{qua_name}:outputs", 0, -1)

    print(f"{qua_name} was called {number_calls} times:")

    for i, o in zip(inputs, outputs):
        print(f"{qua_name}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


class Cache:
    """redis cache class"""
    def __init__(self):
        """init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates random key"""
        rkey = str(uuid.uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(self, key: str, fn: Optional[callable] = None)\
            -> Union[bytes, str, int, float]:
        """convert the data back"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """get data in str format"""
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """get data in int"""
        return int.from_bytes(date, byteorder)
