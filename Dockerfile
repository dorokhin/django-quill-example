FROM python:3.6-alpine

# Copy in your requirements file
COPY requirements.txt /requirements.txt
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

WORKDIR /code

ADD requirements.txt /code/
RUN apk update && apk upgrade
RUN apk --no-cache add \
    python3 \
    python3-dev \
    postgresql-client \
    postgresql-dev \
    build-base \
    gettext
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

RUN set -x ; \
  addgroup -g 101 -S nginx ; \
  adduser -u 101 -D -S -G nginx nginx && exit 0 ; exit 1

RUN mkdir -p /data/static/ && mkdir -p /data/media/

ADD . /code/


ENV PYTHONUNBUFFERED 1