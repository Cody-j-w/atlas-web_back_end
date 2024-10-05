#!/usr/bin/env python3
""" pymongo command for getting all documents in collection
"""

from pymongo import MongoClient

client = MongoClient()


def list_all(mongo_collection):
    res = []
    for doc in mongo_collection.find({}):
        res.append(doc)
    return res
