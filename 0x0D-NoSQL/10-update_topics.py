#!/usr/bin/env python3
"""Change school topics """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document"""
    s_name = {"name": name}
    s_topics = {"$set": {"topics": topics}}
    return mongo_collection.update_many(s_name, s_topics)
