#!/usr/bin/env python3
"""
Contains a LIFO based caching system
"""


class BaseCaching():
    """
    BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """
        Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """
        Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """
        Add an item in the cache
        """
        err = "put must be implemented in your cache class"
        raise NotImplementedError(err)

    def get(self, key):
        """
        Get an item by key
        """
        err = "get must be implemented in your cache class"
        raise NotImplementedError(err)


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
