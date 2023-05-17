#!/usr/bin/env python3
"""
Contains a LRU based caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A LRU Based caching system inheriting from BaseCaching
    """

    def __init__(self):
        """
        Initialize LRUCache
        """
        super().__init__()
        self.limit = BaseCaching.MAX_ITEMS
        self.ages = {}
        self.age = -1

    def put(self, key, item):
        """
        Add an item in the cache if limit passed then
        discard Least recently used item added in dictionary
        """
        if key and item:
            self.age += 1
            if len(self.cache_data) == self.limit \
                    and key not in self.cache_data:
                keys = list(self.ages.keys())
                values = list(self.ages.values())
                least = values[0]
                for val in values:
                    if val <= least:
                        least = val
                k = keys[values.index(least)]
                print("DISCARD: {}".format(k))
                del self.cache_data[k]
                del self.ages[k]
            self.cache_data[key] = item
            self.ages[key] = self.age

    def get(self, key):
        """
        Gets an item by key or returns None if not existing
        """
        if key and key in self.cache_data.keys():
            self.age += 1
            self.ages[key] = self.age
            return self.cache_data[key]
        return None
