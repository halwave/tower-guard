FROM python:3.12-alpine

WORKDIR /app

COPY src/ .

CMD ["python", "-u", "main.py"]
