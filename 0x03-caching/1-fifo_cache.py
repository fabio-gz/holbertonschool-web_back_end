#!/usr/bin/env python3
""". FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache"""

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
        return self.cache_data.get(key, None)
