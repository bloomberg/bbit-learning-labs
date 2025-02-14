## Create Backend of News Feed Website

You are tasked to get news articles from Redis Cache. You will be implementing two functions in order to display them on the News Feed Website. Do not worry about reading in the data from Redis; this is done for you in `backend/app/utils/redis.py`.

### Hints: 
* **Hint 1:** There is only one function from `backend/app/utils/redis.py` you will need to fetch articules. 
* **Hint 2:** In order to get the articles, look at how the data is written into Redis in `backend/app/__init__.py`. 

### Part 1: Write a function to Format Data
In `backend/app/newsfeed.py`, implement a private method that can format the data into an article object. Check a json file in `backend/app/resources/dataset/news` to retrieve necessary information to create an article object. 

### Part 2: Retrieve all News Articles
In `backend/app/newsfeed.py`, implement the `get_all_news` method. You should:

* Figure out how you can retrieve the data from Redis
* Format the data into Articles 
* Return the data as a list of articles. 


### Part 3: Retrieve Featured News 
In `backend/app/newsfeed.py`, implement the `get_featured_news` method. You should:

* Get all the articles
* Sort the articles by most recent published date and return the list 


