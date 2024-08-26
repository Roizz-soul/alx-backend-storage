#!/usr/bin/env python3
""" Script to update a document in a collection """


def update_topics(mongo_collection, name, topics):
    """ Function to update a
        document in a collection """
    mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
    )
