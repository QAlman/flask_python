# pull official base image
FROM python:3.9

# set working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
