#!/usr/bin/python3
"""LFU"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """cache LFU"""
    def __init__(self):
        """Initiallizing"""
        super().__init__()
        self.order = {}

    def get(self, key):
        """ updating stream """
        if key is None or key not in self.cache_data:
            return None

        self.order[key] += 1
        return self.cache_data[key]

    def put(self, key, item):
        """ upadating cache using LFU"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least = min(self.order, key=self.order.get)
                del self.cache_data[least]
                del self.order[least]
                print(f"DISCARD: {least}")
            self.cache_data[key] = item
        if key in self.order:
            self.order[key] += 1
        else:
            self.order[key] = 1
