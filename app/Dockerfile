# pull official base image
FROM python:3.10.8-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
#  Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
#  Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app