#!/usr/bin/env python3
"""
Contains a caching system inheriting from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Implements a caching system inheriting from BaseCaching
    implements put and get methods for adding and accesing
    cache items respectively
    """

    def __init__(self):
        """
        Initialize basic caching system
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache if key or item is None do nothing
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item by key
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
