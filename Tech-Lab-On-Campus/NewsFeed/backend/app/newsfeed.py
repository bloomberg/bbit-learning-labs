"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    """Dataclass for an article."""

    author: str
    title: str
    body: str
    publish_date: datetime
    image_url: str
    url: str


def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    # 2. Format the data into articles
    # 3. Return a list of the articles formatted 
    return []


def get_featured_article() -> Article | None:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles and sort by most recent
    # 2. Return the most recent article
    return None
