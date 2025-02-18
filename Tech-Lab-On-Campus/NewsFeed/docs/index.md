# Tech Lab: Fullstack Web Application Project

In this tech lab, students will gain hands-on experience in building a fullstack web application using React, Flask, Redis, and Docker. This project is designed to provide a comprehensive understanding of modern web development practices and technologies.

This tech lab is inspired by the real-world applications and technologies used at Bloomberg LP. By participating in this project, students will gain valuable skills that are highly relevant in the industry, preparing them for future opportunities in tech companies like Bloomberg.

## Project Overview

Students will work on creating a web application that involves both frontend and backend development. The frontend will be built using React, while the backend will be implemented using Flask. Redis will be used for data caching, and Docker will be utilized to containerize the application for easy deployment.

## Technologies Used

- **React**: A JavaScript library for building user interfaces.
- **Flask**: A lightweight WSGI web application framework in Python.
- **Redis**: An in-memory data structure store, used as a database
- **Docker**: A platform for developing, shipping, and running applications in containers.

## Learning Objectives

By participating in this tech lab, students will:

1. **Frontend Development**: Learn how to create dynamic and responsive user interfaces using React.
2. **Backend Development**: Implement RESTful APIs using Flask to handle data retrieval and manipulation.
3. **Data Caching**: Understand the importance of caching and how to use Redis to improve application performance.
4. **Containerization**: Gain experience in containerizing applications using Docker for consistent and scalable deployment.

## Project Tasks

### Frontend (React)

- Create a user interface to display data retrieved from the backend.
- Implement forms and components to interact with the backend APIs.

### Backend (Flask)

- Develop APIs to handle data requests and responses.
- Integrate Redis for caching data to improve performance.

### Docker

- Containerize the React and Flask applications.
- Set up Docker Compose to manage multi-container applications.

## Getting Started

#### Prerequisites

- Docker
- Git
- VS Code
- VS Code Dev Containers extension

To get started with the project, follow these steps:

#### Fork and Clone the Project Repository

1. Fork the project repository
2. Clone the forked repo into your working directory, and navigate to it:
``` sh
git clone https://github.com/YOUR-USERNAME/bbit-learning-labs.git
cd Tech-Lab-On-Campus/NewsFeed
```

#### Open the Development Container

1. Open VSCode
2. Install the `Dev Containers` extension [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). If you already have it installed, continue to the next step.
3. Open up the Command Palette in VSCode by either `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac) and type `Dev Containers`.
4. Click on `Dev Containers: Reopen in Container`
5. VSCode will start downloading some docker images and install the necessary python and npm packages

#### Run the Website

1. Open up a new terminal window, you can use `` Ctrl+Shift+` ``
2. In the terminal, run `make run-backend` to run the backend
3. Open up another new terminal window, you can use `` Ctrl+Shift+` `` again
4. In the terminal, run `make run-frontend` to run the frontend

✨ You should now be ready to develop! ✨

## Resources

- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Redis Documentation](https://redis.io/documentation)
- [Docker Documentation](https://docs.docker.com/)

We hope you enjoy this learning experience and look forward to seeing your innovative solutions!
