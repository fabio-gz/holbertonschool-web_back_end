#!/usr/bin/env python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.name = []

    def put(self, key, item):
        """add an item in the cache"""
        if key or item:
            self.cache_data[key] = item
            if key not in self.name:
                self.name.append(key)
            if(len(self.cache_data) > BaseCaching.MAX_ITEMS):
                d = self.name.pop(0)
                del self.cache_data[d]
                print(f'DISCARD: {d}')

    def get(self, key):
        """get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key is not None and key in self.cache_data:
            self.name.remove(key)
            self.name.append(key)

        return self.cache_data.get(key, None)
