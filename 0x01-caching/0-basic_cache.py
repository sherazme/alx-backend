#!/usr/bin/python3
""" Basic Cache implementation """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ basic cache implementaion class """
    def put(self, key, item):
        """ Add item in cache """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get item by key """
        return self.cache_data.get(key, None)
