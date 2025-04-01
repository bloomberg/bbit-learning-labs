# Tech Lab: Fullstack Web Application Project

In this tech lab, students will gain hands-on experience in building a fullstack web application using React, Flask, Redis, and Docker. This project is designed to provide a comprehensive understanding of modern web development practices and technologies.

This tech lab is inspired by the real-world applications and technologies used at Bloomberg LP. By participating in this project, students will gain valuable skills that are highly relevant in the industry, preparing them for future opportunities in tech companies like Bloomberg.

## Project Overview

Students will work on creating a web application that involves both frontend and backend development. The frontend will be built using React, while the backend will be implemented using Flask. Redis will be used for data storage, and Docker will be utilized to containerize the application for easy deployment.

## Technologies Used

- **React**: A JavaScript library for building user interfaces.
- **Flask**: A lightweight WSGI web application framework in Python.
- **Redis**: An in-memory data structure store, used as a data store.
- **Docker**: A platform for developing, shipping, and running applications in standardized containers.

## Learning Objectives

By participating in this tech lab, students will:

1. **Frontend Development**: Learn how to create dynamic and responsive user interfaces using React.
2. **Backend Development**: Implement RESTful APIs using Flask to handle data retrieval and manipulation.
3. **Data Caching**: Understand the importance of caching and how to use Redis to improve application performance.
4. **Containerization**: Gain experience in containerizing applications using Docker for consistent and scalable deployment.

## Project Tasks

### Backend (Flask)

- Develop APIs to handle data requests and responses.
- Integrate Redis for storing data to improve performance.

### Frontend (NextJS/React)

- Create a user interface to display data retrieved from the backend.
- Implement forms and components to interact with the backend APIs.

## Getting Started

### Prerequisites

Make sure the following technologies are downloaded prior to starting:

- [Docker](https://docs.docker.com/desktop/)
- [Git](https://git-scm.com/downloads)
- [VS Code](https://code.visualstudio.com/)
- [VS Code Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

To get started with the project, follow these steps:

### Fork and Clone the Project Repository

1. Fork the project repository
2. Clone the forked repo into your working directory, and navigate to it:
``` sh
git clone https://github.com/YOUR-USERNAME/bbit-learning-labs.git
cd bbit-learning-labs/Tech-Lab-On-Campus/NewsFeed
```

### Open the Development Container

1. Open VSCode
2. Install the `Dev Containers` extension [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). If you already have it installed, continue to the next step.
3. Open up the Command Palette in VSCode by either `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac) and type `Dev Containers`.
VS Code may also show a pop up requesting to repoen in container, you can also click this.
4. Click on `Dev Containers: Reopen in Container`
5. VSCode will start downloading some docker images and install the necessary python and npm packages

### Run the Website

All of the `make` commands should be run from the Newfeed folder (using the `cd bbit-learning-labs/Tech-Lab-On-Campus/NewsFeed`
command from above should have placed you in the right folder). You can also simplify your workspace by simply opening
the Newsfeed folder in VS Code. To check that you are in the right folder on your computer terminal:

1. Run `pwd`
2. Verify that is says `/local/path/to/bbit-learning-labs/Tech-Lab-On-Campus/NewsFeed`, where "/local/path/to" is your
local computers path to the bbit-learning-labs folder you cloned. An example of this would be: "/user/USERNAME/Downloads",
but this will vary from person to person.

To get the web app up and running:

1. Open up a new **VS Code terminal window**, you can use <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>`</kbd>
2. In the terminal, run `make run-backend` to run the backend
3. Open up another new terminal window, you can use <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>`</kbd> again
4. In the terminal, run `make run-frontend` to run the frontend

✨ You should now be ready to develop! ✨

### Developing

- [Backend Tasks](./backend.md)
- [Frontend Tasks](./frontend.md)

## Troubleshooting

### Issues with Docker
If you are encountering issues with docker, you can use Github codespaces instead:

1. Fork the repo
2. Navigate to the forked repo
3. Click on the green `< > Code` button
4. Select the Codespaces tab and click on the `+` button
5. In codespaces, open a new terminal and run `cd Tech-Lab-On-Campus/NewsFeed/`
6. run `make install`
7. run `make redis-in-docker`
8. run `make run-backend`
9. Open up a new terminal and run `make run-frontend`
10. A pop up should appear saying that port 3000 is in use. Click on `Open in Browser`. If not, the link can be opened from the terminal window

### Starting Frontend

- Clicking on http://localhost:3000 in the terminal opens to a blank page in the browser?
    - Make sure you have done `make run` from the NewsFeed folder (where the Makefile is)
    - It will probably have opened to 0.0.0.0:3000, just rewrite the url to localhost:3000 in the browser and it should load.
- npm packages are not loading
    - If you are a bloomberg engineer, try turning off bbpvn while dev container sets up
    - Otherwise, try running make clean or deleting any package.json or node_module directories and running:
    `npm install` from within the `./frontend` folder. (Can reach via `cd frontend`)
    - If this does not work, try to open in codespaces, see [issues with docker](#issues-with-docker) section above.

## Resources

- [Resources](./resources/)

We hope you enjoy this learning experience and look forward to seeing your innovative solutions!
