#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """caching system"""
    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
