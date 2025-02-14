# Coding Interview Question Prompt

## Design a Backend System for a News Website Newsfeed Page

### Question

You are tasked with designing the backend system for a newsfeed page similar to those found on news websites like Bloomberg. The newsfeed should display articles from various sources, sorted by the time of publishing, with the most recent articles appearing first.

### Requirements

1. **Data Structures:**
   - Design the data structures to store articles and sources.
   - Explain your choice of data structures and how they will efficiently support the operations needed for the newsfeed.

2. **Operations:**
   - Implement the following operation:
     - `get_newsfeed() -> List[Article]`: Retrieve the newsfeed of articles, sorted by the most recent articles first.
     - `get_featured_article() -> Article`: Retrieve the article to be featured on the main page.

3. **Efficiency:**
   - Discuss the time and space complexity of each operation.
   - Consider how to handle large numbers of users and articles efficiently.

### Coding Part

```python
from datetime import datetime
from typing import List

class Article:
    def __init__(self, source_id: str, content: str, timestamp: datetime):
        self.source_id = source_id
        self.content = content
        self.timestamp = timestamp

class NewsfeedApi:
    def __init__(self):
        # Implementation here
        pass

    def get_newsfeed(self) -> List[Article]:
        # Implementation here
        return []

    def get_featured_article(self) -> Article:
        # Implementation here
        return None
```

## Follow-Up Question

Extend the backend system to keep track of the articles that users have bookmarked. The bookmarks should be kept in the order they were bookmarked. Users should also be able to remove a bookmark.

### Requirements

1. **Data Structures:**
   - Design the data structures to store bookmarks for each user.
   - Explain your choice of data structures and how they will efficiently support the operations needed for managing bookmarks.

2. **Operations:**
   - Implement the following operations:
     - `bookmark_article(user_id: str, article_id: str)`: Bookmark an article for a user.
     - `remove_bookmark(user_id: str, article_id: str)`: Remove a bookmark for a user.
     - `get_bookmarks(user_id: str) -> List[Article]`: Retrieve the list of bookmarked articles for a user in the order they were bookmarked.

## Follow-Up Question 2

Extend the backend system to keep track of the view count for each article. Implement a function to list the top `n` most viewed articles, where `n` is a user-defined number.

### Requirements

1. **Data Structures:**
   - Modify the `Article` class to include a view count.
   - Design the data structures to efficiently support the operations needed for tracking and retrieving the most viewed articles.

2. **Operations:**
   - Implement the following operation:
     - `get_top_viewed_articles(n: int) -> List[Article]`: Retrieve the top `n` most viewed articles.

## Follow-Up Question 3

Now, like in real news websites, articles will pretain to a certain news sector. Some examples of sectors include technology, finance, and politics. Implement a function to determine the most popular sector in the collection of articles. 

### Requirements

1. **Data Structures:**
   - Modify the `Article` class to include a sector.
   - Design the data structures to efficiently support the operations needed for tracking and determining the most popular sector.

2. **Operations:**
   - Implement the following operation:
     - `get_most_popular_sector() -> str`: Retrieve the most popular sector from the collection of articles.

### Hint

Is the meaning of `popular` straightforward, or is there some ambiguity? How would you approach this problem in an interview setting?
