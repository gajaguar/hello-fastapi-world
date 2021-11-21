FROM python:alpine

WORKDIR /app

RUN pip install fastapi uvicorn

