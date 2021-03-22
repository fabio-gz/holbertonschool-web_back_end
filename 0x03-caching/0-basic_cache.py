#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """caching system"""
    def put(self, key, item):
        """put"""
        if key and item :
            self.cache_data[key] = item

    def get(self, key):
        """get"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
