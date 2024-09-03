#!/usr/bin/python3
BaseCaching = __import__('base_caching').BaseCaching
""" BasicCache module
"""

class BasicCache(BaseCaching):
    """
    Basic Caching adds:
    - functional put method to add item to cache
    - functional get method to retrieve an item from the cache
    """
    def put(self, key, item):
        """
        Add item to cache
        """
        if key != None and item != None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Retrieve the value of the provided key
        """
        if key == None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
