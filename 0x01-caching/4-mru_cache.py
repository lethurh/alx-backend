#!/usr/bin/env python3
'''
task 3 learning LRU the tough way
'''

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A class representing a Least Recently Used (LRU) Cache.

    Inherits from the BaseCaching class.
    """

    def _init_(self):
        """
        Initialize the LRUCache object.

        Args:
            None

        Returns:
            None
        """
        super()._init_()
        self.track = list()

    def handle_none_full_cache(self, key, item):
        """
        Handle the case when the cache is not full.

        Adds the key and item to the cache.

        Args:
            key: The key to be added to the cache.
            item: The item to be added to the cache.

        Returns:
            None
        """
        self.track.append(key)
        self.cache_data[key] = item

    def handle_full_cache(self, key, item):
        """
        Handle the case when the cache is full.

        Removes the most recently used item from the cache and adds the new
        key and item.

        Args:
            key: The key to be added to the cache.
            item: The item to be added to the cache.

        Returns:
            None
        """
        # For MRU, remove the most recently used item, which is
        # the last item in the track list
        to_remove = self.track.pop(-1)  # Change from pop(0) to pop(-1)
        if to_remove in self.cache_data:
            self.cache_data.pop(to_remove)
            print('DISCARD:', to_remove)
        else:
            print(f"Attempted to remove non-existent key: {to_remove}")
        self.track.append(key)
        self.cache_data[key] = item

    def swap(self, key):
        """
        Move the key to the end of the track list.

        Args:
            key: The key to be moved.

        Returns:
            None
        """
        self.track.remove(key)
        self.track.append(key)

    def put(self, key, item):
        """
        Add a key-value pair to the cache.

        If the key already exists in the cache, update its value.
        If the cache is not full, add the key-value pair to the cache.
        If the cache is full, remove the least recently used item and add the
        new key-value pair.

        Args:
            key: The key to be added to the cache.
            item: The item to be added to the cache.

        Returns:
            None
        """
        if item is None or key is None:
            return
        if key in self.cache_data:
            self.swap(key)
            self.cache_data[key] = item
        elif len(self.cache_data) < self.MAX_ITEMS:
            self.handle_none_full_cache(key, item)
        else:
            self.handle_full_cache(key, item)

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.

        If the key exists in the cache, move it to the end of the track list
        and return its value.
        If the key does not exist in the cache, return None.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if the key does not
            exist in the cache.
        """
        if key in self.cache_data and key is not None:
            if key in self.track:
                self.swap(key)
            return self.cache_data[key]
        return None
