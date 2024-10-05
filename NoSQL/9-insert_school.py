#!/usr/bin/env python3
""" list_all module
"""

from pymongo import MongoClient

client = MongoClient()


def insert_school(mongo_collection, **kwargs):
    """ add new document
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
