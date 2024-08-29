#!/usr/bin/env python3
""" Exercise.py """
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """ Initialization function """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store function to store data with a random key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
