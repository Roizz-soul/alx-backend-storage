#!/usr/bin/env python3
""" Get page function """

import redis
import requests
from functools import wraps
from typing import Callable


redis_client = redis.Redis()


def cache_page(func: Callable) -> Callable:
    """ Decorator to cache the page and track the access count """
    @wraps(func)
    def wrapper(url: str) -> str:
        """ Wrapper to track number of times URL is accessed """
        redis_client.incr(f"count:{url}")

        catched_page = redis_client.get(f"cache:{url}")
        if cached_page:
            return cached_page.decode('utf-8')

        html_content = func(url)

        redis_client.setex(f"cache:{url}", 10, html_content)

        return html_content

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """ Gets the page and returns its content """
    response = requests.get(url)
    html_content = response.text

    return html_content
