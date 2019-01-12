FROM python:3.7-stretch
MAINTAINER Satoru Tagawa "satoru.tagawa@gmail.com"
RUN apt-get -y update
ADD conf/requirements.txt /tmp/
RUN pip install -q --trusted-host pypi.python.org --upgrade pip && pip install -q --trusted-host pypi.python.org -r /tmp/requirements.txt

RUN mkdir /app
WORKDIR /app
COPY $PWD/src/*.py /app/
