FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./backend .

EXPOSE 8000

RUN pip install --upgrade pip \
    && pip install mysqlclient \
    && pip install -r requirements.txt
