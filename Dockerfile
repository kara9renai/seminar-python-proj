FROM python:latest

USER root

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y sudo \
    && pip3 install --upgrade pip

WORKDIR /pyproj

COPY ./src ./src
COPY ./csv ./csv

COPY requirements.txt ${PWD}

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt