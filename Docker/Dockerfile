FROM python:3.7-stretch
MAINTAINER Satoru Tagawa "satoru.tagawa@gmail.com"
RUN apt-get -y update
RUN mkdir /app
WORKDIR /app
COPY $PWD/main.py /app
COPY $PWD/src /app
