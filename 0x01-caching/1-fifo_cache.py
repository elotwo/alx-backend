#!/usr/bin/python3
BaseCaching = __import__('base_caching').BaseCaching
class FIFOCache(BaseCaching):
    def __init__(self):
        BaseCaching.__init__(self)
    def put(self, key, item):
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item
        if len(self.cache_data[item]) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print (f"DISCARD: {first_key}")
            
    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
