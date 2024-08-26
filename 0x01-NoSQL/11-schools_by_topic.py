#!/usr/bin/env python3
""" Script to list all documents witha match in a collection """


def schools_by_topic(mongo_collection, topic):
    """ Function to return list
        all documents in a collection """
    documents = mongo_collection.find({"topics": topic})
    return documents if documents else []
