#!/usr/bin/env python3
""" Exercise.py """
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, keyG: str, fn: Optional[Callable[[bytes],
            Union[str, int, float, bytes]]] = None) -> Optional[
            Union[str, int, float, bytes]]:
        """ Get method to return original type"""
        value = self._redis.get(keyG)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, KeyG: str) -> Optional[str]:
        """ get_str calls the get method with a string """
        return self.get(KeyG, lambda x: x.decode('utf-8'))

    def get_int(self, keyG: str) -> Optional[int]:
        """ get_int calls the get method with an int """
        return self.get(keyG, lambda x: int(x))
