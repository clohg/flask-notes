# flask-notes
Get the source code for running a local Python and Flask website using Bootstrap to store and manage your notes, also available as a Docker container.

[![Docker](https://github.com/clohg/flask-notes/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/clohg/flask-notes/actions/workflows/docker-publish.yml)

## Try It Out

### From Docker Hub
To fetch this Docker container image from Docker Hub on any internet-connected machine use:

    docker pull clohg/flask-notes:latest

To run the app use the following command:

    docker run -p 5000:5000 flask-notes:latest

### From GitHub Packages
To fetch this Docker container image from GitHub Packages on any internet-connected machine use:

    docker pull ghcr.io/clohg/flask-notes:master

To run the app use the following command:

    docker run -p 5000:5000 ghcr.io/clohg/flask-notes:master
