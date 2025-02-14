"""Module defining and intializing Redis cache datastore. Do not edit."""

import json
import os
from typing import Any, Optional

import redis

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))


class RedisClient:
    """Redis client class for saving and retrieving entries."""

    def __init__(self, host: str = REDIS_HOST, port: int = REDIS_PORT, db: int = 0):
        """
        Initialize Redis connection with connection pool.

        Args:
            host (str): Redis host address (default: redis)
            port (int): Redis port number
            db (int): Redis database number
        """
        self.pool = redis.ConnectionPool(host=host, port=port, db=db)

    def _get_connection(self) -> redis.Redis:
        """
        Get a connection from the pool.

        Returns
        -------
            redis.Redis: A Redis connection object.
        """
        return redis.Redis(connection_pool=self.pool)

    def save_entry(self, key: str, value: Any, expiration: Optional[int] = None) -> None:
        """
        Save an entry to Redis using a connection from the pool.

        Args:
            key (str): Key to store the value under
            value (Any): Value to store (will be JSON serialized)
            expiration (Optional[int]): Time in seconds until the key expires
        """
        with self._get_connection() as redis_client:
            try:
                # Convert value to JSON string for storage
                json_value = json.dumps(value)
                # Save to Redis
                redis_client.set(key, json_value, ex=expiration)
            except Exception as e:
                raise Exception(f"Error saving entry: {e}")

    def get_entry(self, key: str) -> Optional[Any]:
        """
        Retrieve an entry from Redis using a connection from the pool.

        Args:
            key (str): Key to retrieve

        Returns
        -------
            Optional[Any]: Retrieved value (JSON deserialized) or None if not found
        """
        with self._get_connection() as redis_client:
            try:
                # Retrieve the value from cache
                value = redis_client.get(key)
                if value is None:
                    return None
                # Convert JSON string back to Python object
                return json.loads(value)
            except Exception as e:
                raise KeyError(f"Error retrieving entry:\n{e}")


# Instantiates Redis Client interface for the app
REDIS_CLIENT = RedisClient(host=REDIS_HOST, port=REDIS_PORT)
