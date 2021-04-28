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
