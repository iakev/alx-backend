#!/usr/bin/python3
"""
Contains a caching system inheriting from BaseCaching
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
