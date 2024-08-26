#!/usr/bin/env python3
""" Script to insert a document in a collection """


def insert_school(mongo_collection, **kwargs):
    """ Function to return the id after inserting
    document in a collection """
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id
