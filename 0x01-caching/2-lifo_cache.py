#!/usr/bin/python3
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache class that implements a caching system using LIFO (Last In, First Out).
    """

    def __init__(self):
        """Initialize the cache and tracking order."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache using LIFO policy."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key) if key is not None else None
