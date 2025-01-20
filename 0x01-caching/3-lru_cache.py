#!/usr/bin/env python3
"""
This module implements the LRUCache class,
which inherits from BaseCaching.
LRUCache uses the least recently used
(LRU) caching strategy to manage the
cache with a fixed size defined by
BaseCaching.MAX_ITEMS.

Functions:
- put(key, item): Adds an item to the cache.
If the cache exceeds its limit,
  the least recently used item is removed.
- get(key): Retrieves an item from
the cache by key, updating its usage.
"""

from collections import OrderedDict
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and uses
    an OrderedDict to implement an LRU caching strategy.
    """

    def __init__(self):
        """
        Initialize the cache as an OrderedDict
        to maintain the order of item usage.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache using LRU policy.
        If key or item is None, do nothing.
        If the cache exceeds MAX_ITEMS,
        discard the least recently used item.

        Args:
            key (str): The key of the item to add.
            item (Any): The item to store in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item by key from
        the cache and update its usage.

        Args:
            key (str): The key to look up in the cache.

        Returns:
            Any: The value associated with
            the key, or None if not found.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
