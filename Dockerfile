FROM python:3.10.5-slim-buster

RUN apt update && apt upgrade -y && pip install poetry

WORKDIR /image-generator

COPY . .

RUN poetry config virtualenvs.create false
RUN poetry install

