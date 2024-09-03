#!/usr/bin/python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching adds:
    - ejection of first item on get() if over MAX_ITEMS
    - functional get method to retrieve an item from the cache
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add item to cache - eject first item if over limit
        """
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS:
                print(f"DISCARD: {self.stack[0]}")
                self.cache_data.pop(self.stack[0])
            self.cache_data.update({key: item})
            self.stack.append(key)

    def get(self, key):
        """
        Retrieve the value of the provided key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
