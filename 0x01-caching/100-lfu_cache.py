#!/usr/bin/env python3
"""
Contains a LFU based caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    A LFU Based caching system inheriting from BaseCaching if
    more than one item for discafing switch t LRU
    """

    def __init__(self):
        """
        Initialize LFUCache
        """
        super().__init__()
        self.limit = BaseCaching.MAX_ITEMS
        self.ages = {}
        self.age = -1
        self.hits = {}

    def put(self, key, item):
        """
        Add an item in the cache if limit passed then
        discard Least Frequently Used item added in dictionary
        if more than one item has same frequency swithc to LRU
        to determine wht to remove
        """
        if key and item:
            self.age += 1
            if len(self.cache_data) == self.limit \
                    and key not in self.cache_data:
                least_freq_keys = list(self.hits.keys())
                least_freq_values = list(self.hits.values())
                least = least_freq_values[0]
                for val in least_freq_values:
                    if val <= least:
                        least = val
                if least_freq_values.count(least) > 1:
                    # do an LRU
                    same_keys = []
                    # get all keys and values associated with 'least' value
                    for ke, va in self.hits.items():
                        if va == least:
                            same_keys.append(ke)
                    least_value = self.ages[same_keys[0]]
                    for i in range(len(same_keys)):
                        if self.ages[same_keys[i]] <= least_value:
                            least_key = same_keys[i]
                            least_value = self.ages[same_keys[i]]
                    k = least_key
                else:
                    k = least_freq_keys[least_freq_values.index(least)]
                print("DISCARD: {}".format(k))
                del self.cache_data[k]
                del self.ages[k]
                del self.hits[k]
            self.cache_data[key] = item
            self.ages[key] = self.age
            if key not in self.hits:
                self.hits[key] = 1
            else:
                self.hits[key] += 1

    def get(self, key):
        """
        Gets an item by key or returns None if not existing
        """
        if key and key in self.cache_data.keys():
            self.age += 1
            self.ages[key] = self.age
            self.hits[key] += 1
            return self.cache_data[key]
        return None
