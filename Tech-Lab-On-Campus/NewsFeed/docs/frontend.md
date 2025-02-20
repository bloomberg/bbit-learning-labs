## Create Frontend of News Feed Website

You are tasked with populating the frontend of a news feed webpage which is going to display news articles. You will populate a _Featured News_ section as well as a _News Feed_ Section. You will take advantage of reusable components in [React](https://react.dev/learn). After that, you will connect the frontend to the backend in order to get data from the api your backend partner built.

### Hints

- **Hint 1:** Some classes included in `frontend/src/styles/globals.css` may help with styling.
- **Hint 2:** [Array.map()]((https://www.geeksforgeeks.org/typescript-array-map-method/)) may be useful.
- **Hint 3:** This [Medium blog](https://medium.com/@bhanu.mt.1501/api-calls-in-react-js-342a09d5315f) may be useful to figure how to fetch data.


### Part 1 : Display a Featured News Article
In `frontend/src/components/FeaturedNews.tsx` implement the component that will display the featured news article.

* It should use the props to display:
    1. The featured article's title
    1. The featured article's image
    1. A portion of the selected article's body, truncated so that it fits nicely in the section

Once completing Part 1, Once completing this part, you should be able to see the Featured News Article at the top of the page.
For more information on how to create a component, refer to the [react basics](./resources/react-basics.md) docs.


### Part 2 : Create a reusable news card to use with general stories
In `frontend/src/components/NewsCard.tsx` implement a reusable news card component to use with the news feed articles (articles that aren't the featured story)

* The `NewsCard` component should have these properties:
    1. The article's title
    1. The article's image
    1. A truncated version of the article's body

This component should be reusable so that it can be used to populate all stories on the news page.
Once completing Part 2, you should be able to see a few test articles on the right side of the screen.


### Part 3 : Populate a news feed with the given `articles`

In `frontend/src/components/NewsFeed.tsx` populate a news feed using the given articles

* Use the reusable News Card Component created in Part 2 to create the articles in the new feeds
Once completing Part 3, you should be able to see a grid of news articles at the bottom of the page under the Featured News Article Section.

### Part 4 : API Integration
In `frontend/src/pages/news.tsx` fetch article data from the API call. The Featured Article Data and the News Feed Data should both come from the API

* Fetch the featured article from `/api/news/get-featured-article`
* Fetch the news feed data from `/api/news/get-newsfeed`
* Use the `set` functions defined above to update the `articles` and `featuredArticle` variables

Once completing Part 4, you should be able to see news articles different from the dummy data originally provided.

### Stretch Goals
You now have a news feed up and running connected to a backend service! You can follow up with some of the following optimizations if interested.

1. **Responsiveness:** a website typically adjusts itself to fit the screen it is being displayed on in order to make it most presentable to the end user. Play around with the layout and responsive properties to find the best experience.
1. **Styling:** this is a pretty plain website that we have so far. Are there any styling properties or elements you can add to make it look more like a news website? Look at [Bloomberg News](https://www.bloomberg.com) for inspo!
1. **[Deploy to Heroku](https://github.com/marketplace/actions/deploy-to-heroku):** You have a full website now, which you can deploy to heroku to use as part of your portfolio!
