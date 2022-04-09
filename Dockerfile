
FROM python:3.9.5-alpine3.13

WORKDIR /app

COPY app/dbwork.py .

COPY app/form.tpl .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8080:8080