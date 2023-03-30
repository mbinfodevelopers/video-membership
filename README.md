# My Awesome Project

This is a sample project that demonstrates the use of Docker Compose to set up a multi-container environment for a web application. The project consists of a Django app that displays the current time and weather conditions for a specified location, as well as an Nginx server that acts as a reverse proxy for the app.

## Installation

To run this project locally, you will need to have the following tools installed:

- Docker
- Docker Compose

## Once you have these tools installed, you can clone the project repository to your local machine:

```
git clone https://github.com/mbinfodevelopers/video-membership.git

```

Next, navigate to the project directory and build the Docker images using the following command:

```
docker-compose build
```
Once the images have been built, you can start the containers using the following command:
```
docker-compose up -d

```

This will start the containers in detached mode, allowing you to continue using the terminal. You can then access the web app by opening a web browser and navigating to http://localhost.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
