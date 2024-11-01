#!/usr/bin/env python3
"""cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """basic cache"""
    def __init__(self):
        """initializing"""
        super().__init__()

    def put(self, key, item):
        """exam """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """na so"""
        if key is None or key not in self.cache_data:
            return(None)
        return self.cache_data[key]
