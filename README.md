Make sure that you have Docker installed on your system.

    docker --version

To install Docker Compose on Linux, you can follow the steps below:
- sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

Set the correct permissions on the Docker Compose binary:
    sudo chmod +x /usr/local/bin/docker-compose

Finally:
    docker --version
