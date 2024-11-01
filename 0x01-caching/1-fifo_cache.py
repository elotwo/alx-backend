#!/usr/bin/python3
""" First in First out FIFO """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ creating cache for FIFO"""
    def __init__(self):
        """ initialize """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ this method is used for updating the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ this method is for updating track"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
