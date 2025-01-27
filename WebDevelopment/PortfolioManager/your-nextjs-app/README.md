# `your-nextjs-app`

This will be your main working directory. Refer to the labs in the directory above (prefixed by a lab number and a hyphen), while doing your work here.

Some information about a NextJS project structure:
* The `src` directory contains important files that make the website work. Your work will be mostly concentrated in this directory
* There are a few important directories inside `src` that we will go over:
  * The `components` directory contains all React components that are not rendered as a webpage. Components here can be imported from any of the webpages in the `pages` directory, or from other components inside the same directory. You will be creating a component file in this directory in one of the labs
  * The `pages` directory contains both *frontend* and *backend* (inside the `api` directory) website functionality. This directory usually contains the `index.jsx` (or `index.js`) file that gets rendered as the default webpage when the user accesses the website URL. You will be making changes in the `index.jsx` file
    * While the `api` directory inside `pages` contains API routes that help the frontend side of the webapp have dynamic and data-driven functionality, our focus will be mostly on the frontend. However, NextJS as a framework is able to create complex and performant fullstack web applications, and is not restricted to just the frontend

## Getting Started

The `your-nextjs-app` will be your main working directory. In order to run your webapp, follow the instructions below.

### Technical Requirements
- Docker
- Git

### Installing Git

In order to easily download the most up-to-date version of this repository, you will be interested in downloading [Git](https://git-scm.com/downloads). Once you have downloaded and installed Git, you should be able to clone this repository.

Once you have installed Git, clone this repository by opening a terminal window and running:
```
git clone https://github.com/bloomberg/bbit-learning-labs
```

The `bbit-learning-labs` repository is the parent directory of this tech lab. Your work will be contained within the `bbit-learning-labs/WebDevelopment` directory. Navigate to this directory by running the command `cd bbit-learning-labs/`, in a terminal window.

### Installing Docker

Docker Compose is a tool for defining and running multi-container applications. It is the key to unlocking a streamlined and efficient development and deployment experience.

1. [Install Docker](https://docs.docker.com/get-docker/) by following instructions for your Operating System.

2. Then, build and run your application containers from the `bbit-learning-labs/WebDevelopment` directory by running the command `docker compose up`:
    * The `docker compose up` command will execute the following commands (`npm install` && `npm run dev`, defined in the `docker-compose.yml` file) that will start your web application in addition to running a local backend server for your webapp API requests.

3. Your web application should be running. Keep this directory handy, because here is where you'll be creating/modifying your project files.

4. Open [http://localhost:3000](http://localhost:3000) with your browser to see the UI of your web application.

This is an example of how the website should look like after a successful setup:
![Successful setup](./Webapp-After-Setup.png)
