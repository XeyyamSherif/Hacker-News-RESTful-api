FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code/core

COPY ./requirements.txt ../requirements.txt

RUN pip install -r ../requirements.txt

COPY . /code/


COPY wait-for-it.sh wait-for-it.sh

RUN chmod +x wait-for-it.sh

