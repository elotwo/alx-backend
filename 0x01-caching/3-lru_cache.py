#!/usr/bin/python3
BaseCaching = __import__('base_caching').BaseCaching
class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order = []
        
    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
        else:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_freq = self.order.pop(0)
                del self.cache_data[least_freq]
                print (f"DISCARD: {least_freq}")
            self.cache_data[key] = item 
        self.order.append(key) 
    def get(self, key):
        if key is None or key not in self.cache_data:
            return
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
