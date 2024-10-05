#!/usr/bin/env python3
""" update module
"""

from pymongo import MongoClient

client = MongoClient()


def update_topics(mongo_collection, name, topics):
    """ update document
    """
    mongo_collection.update_one({'name': name}, {'$addToSet': {'topics': topics}})
