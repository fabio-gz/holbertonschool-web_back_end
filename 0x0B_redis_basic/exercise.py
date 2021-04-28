#!/usr/bin/env python3
"""string to redis"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """redis cache class"""
    def __init__(self):
        """init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """generates random key"""
        rkey = str(uuid.uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(self, key: str, fn: Optional[callable] = None)
    -> Union[bytes, str, int, float]:
        """convert the data back"""
        if fn:
            return fn(data)
        return data
