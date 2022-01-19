FROM python:3.9.9-slim-bullseye

WORKDIR ~/event_asigner

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ ./