FROM python:3.8-slim

ENV APP_HOME /app

WORKDIR $APP_HOME
COPY . ./
RUN pip install Flask gunicorn

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app