from web import get_page
import redis

# Initialize Redis client
redis_client = redis.Redis()

def get_access_count(url: str) -> int:
    """Retrieve the count of how many times a URL was accessed."""
    count = redis_client.get(f"count:{url}")
    return int(count) if count else 0

if __name__ == "__main__":
    url = "http://www.google.com"

    # Test the get_page function multiple times
    print("First call (should take longer if not cached):")
    print(get_page(url))  # This will fetch and cache the page
    print(f"Access count after first call: {get_access_count(url)}\n")

    print("Second call (should be fast, fetched from cache):")
    print(get_page(url))  # This should return the cached page quickly
    print(f"Access count after second call: {get_access_count(url)}\n")

    print("Waiting for cache to expire (10 seconds)...")
    import time
    time.sleep(10)

    print("Third call (cache expired, should take longer):")
    print(get_page(url))  # Cache expired, so this will fetch the page again
    print(f"Access count after third call: {get_access_count(url)}")
