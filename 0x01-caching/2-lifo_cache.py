#!/usr/bin/env python3
"""Task 2: LIFO Caching.
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """LIFO Caching system"""
    
    def _init_(self):
        """Initialize LIFOCache"""
        super()._init_()
        self.last_key = None  # To keep track of the last item inserted

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        
        # Add the item to the cache and update the last_key
        self.cache_data[key] = item
        self.last_key = key
        
        # If the number of items exceeds MAX_ITEMS, apply LIFO removal
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key:
                # Discard the last item inserted
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")
                # Set last_key to None to avoid invalid reference
                self.last_key = None

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
