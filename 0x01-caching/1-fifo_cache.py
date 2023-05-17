#!/usr/bin/env python3
"""
Contains a FIFO based caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFO Based caching system inheriting from BaseCaching
    """

    def __init__(self):
        """
        Initialize FIFOCache
        """
        super().__init__()
        self.limit = BaseCaching.MAX_ITEMS

    def put(self, key, item):
        """
        Add an item in the cache if limit passed then
        discard First item in dictionary
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.limit:
                for key in self.cache_data.keys():
                    print("DISCARD: {}".format(key))
                    del self.cache_data[key]
                    break

    def get(self, key):
        """
        Gets an item by key
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
