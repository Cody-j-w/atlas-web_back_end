#!/usr/bin/python3
""" LRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU Caching adds:
    - ejection of least recently used item
    - functional get method to retrieve an item from the cache
    """

    def __init__(self):
        super().__init__()
        self.lru = {}
        self.count = 0

    def put(self, key, item):
        """
        Add item to cache - eject least recently used item if over limit
        """
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS:
                prev = min(self.lru.keys(), key=lambda k: self.lru[k])
                del self.cache_data[prev]
                del self.lru[prev]
                print("DISCARD: "+prev)
            self.cache_data.update({key: item})
            self.lru[key] = self.count
            self.count += 1

    def get(self, key):
        """
        Retrieve the value of the provided key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            self.lru[key] = self.count
            self.count += 1
            return self.cache_data[key]
