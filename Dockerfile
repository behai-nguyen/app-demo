# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app_demo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000
ENTRYPOINT ["waitress-serve"]
CMD ["--port=8000", "--call", "src.app_demo:create_app"]