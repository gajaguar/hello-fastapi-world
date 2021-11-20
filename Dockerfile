FROM python:alpine

WORKDIR /app

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app", "--host 0.0.0.0", "--reload"]

