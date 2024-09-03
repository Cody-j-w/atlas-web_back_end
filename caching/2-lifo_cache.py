#!/usr/bin/python3
""" LIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching adds:
    - ejection of last item on get() if over MAX_ITEMS
    - functional get method to retrieve an item from the cache
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add item to cache - eject last item if over limit
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    print(f"DISCARD: {self.stack[len(self.stack)-1]}")
                    del self.cache_data[self.stack[len(self.stack)-1]]
                    self.stack.pop(len(self.stack)-1)
            self.cache_data.update({key: item})
            self.stack.append(key)
            print("Current stack: "+str(self.stack))

    def get(self, key):
        """
        Retrieve the value of the provided key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
