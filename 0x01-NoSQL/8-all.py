#!/usr/bin/env python3
""" Script to list all documents in a collection """


def list_all(mongo_collection):
    """ Function to return list
        all documents in a collection """
    documents = mongo_collection.find()
    return documents if documents else []
