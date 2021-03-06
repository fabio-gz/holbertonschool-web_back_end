#!/usr/bin/env python3
""". FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class system"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.name = []

    def put(self, key, item):
        """add an item in the cache"""
        if None not in {key, item}:
            self.cache_data[key] = item
            if key not in self.name:
                self.name.append(key)

            if(len(self.cache_data) > BaseCaching.MAX_ITEMS):
                d = self.name.pop(0)
                del self.cache_data[d]
                print('DISCARD: {}'.format(d))

    def get(self, key):
        """get an item by key"""
        return self.cache_data.get(key, None)
