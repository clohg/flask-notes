# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:focal-1.0.0

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...
RUN apt-get update
RUN apt-get install python3.8 python3-pip -y

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Setup app
WORKDIR /usr/src/app
COPY Pipfile ./
RUN pip3 install --no-cache-dir pipenv && pipenv install
COPY *.py .
COPY website/*.py website/
COPY website/templates/*.html website/templates/
COPY website/static/*.js website/static/
ENTRYPOINT pipenv run python -m flask run --host=0.0.0.0
