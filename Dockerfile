# syntax=docker/dockerfile:1

FROM python:3.10.5-slim-buster

WORKDIR /app_demo

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip3 install -e .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]