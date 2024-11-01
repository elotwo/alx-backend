#!/usr/bin/python3
"""LRU"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Cache MRU"""
    def __init__(self):
        """ initiallizing """
        super().__init__()
        self.order = []

    def get(self, key):
        """upadating cache using LRU arlgorithm"""
        if key is None or key not in self.cache_data:
            return None

        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]

    def put(self, key, item):
        """ upadting track """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            recent = self.order.pop()
            del self.cache_data[recent]
            print(f"DISCARD: {recent}")

        self.cache_data[key] = item
        self.order.append(key)
