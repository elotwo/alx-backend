#!/usr/bin/python3
""" LRU """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ cache LRU """
    def __init__(self):
        """initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """This mothod update cache using LRU"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_freq = self.order.pop(0)
                del self.cache_data[least_freq]
                print(f"DISCARD: {least_freq}")
            self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """" the method keep track """
        if key is None or key not in self.cache_data:
            return
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
