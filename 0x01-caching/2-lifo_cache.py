#!/usr/bin/env python3
"""
Contains a LIFO based caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A LIFO Based caching system inheriting from BaseCaching
    """

    def __init__(self):
        """
        Initialize LIFOCache
        """
        super().__init__()
        self.limit = BaseCaching.MAX_ITEMS
        self.key_stack = []

    def put(self, key, item):
        """
        Add an item in the cache if limit passed then
        discard Last item added in dictionary
        """
        if key and item:
            if len(self.cache_data) == self.limit \
                    and key not in self.cache_data.keys():
                k = self.key_stack.pop()
                while k in self.key_stack:
                    self.key_stack.remove(k)
                print("DISCARD: {}".format(k))
                del self.cache_data[k]
            self.cache_data[key] = item
            self.key_stack.append(key)

    def get(self, key):
        """
        Gets an item by key
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
