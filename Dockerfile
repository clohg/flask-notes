FROM python:3
WORKDIR /usr/src/app
COPY Pipfile ./
RUN pip3 install --no-cache-dir pipenv && pipenv install
COPY *.py .
COPY website/*.py website/
COPY website/templates/*.html website/templates/
COPY website/static/*.js website/static/
CMD [ "pipenv", "run", "python", "-m", "flask", "run", "--host=0.0.0.0" ]