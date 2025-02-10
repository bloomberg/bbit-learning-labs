"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime

from app.utils.redis import REDIS_CLIENT


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
    all_articles: list[dict] = REDIS_CLIENT.get_entry("all_articles")

    if all_articles is None:
        return []

    return [_format_as_article(article) for article in all_articles]


def get_featured_news() -> Article | None:
    """Get the featured news article from the datastore."""
    # can be this or some criteria to decide which is featured.
    all_news = get_all_news()

    return sorted(all_news, lambda article: article.publish_date, reverse=True)[0] if all_news else None


def _format_as_article(data: dict) -> Article:
    return Article(
        author=data["author"],
        title=data["title"],
        body=data["text"],
        publish_date=datetime.fromisoformat(data["published"]),
        image_url=data["thread"]["main_image"],
        url=data["url"],
    )
