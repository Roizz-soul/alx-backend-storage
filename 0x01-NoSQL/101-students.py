#!/usr/bin/env python3
""" Script to list documents in a collection """


def top_students(mongo_collection):
    """ Function to list
        documents in a collection """
    pipeline = [
        {
            "$addFields": {
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    # Execute the pipeline and return the result as a list
    return list(mongo_collection.aggregate(pipeline))
