FROM python:3.12

RUN mkdir /django_app && cd /django_app

WORKDIR /django_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
