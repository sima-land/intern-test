FROM python:3.10-slim

MAINTAINER Isakov Maxim Isakovmv.ekb@gmail.com

WORKDIR /app

COPY requirements.txt .

RUN apt-get update
RUN apt-get install unzip -y
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN unzip -o ./data/data.zip -d ./data

EXPOSE 80

ENTRYPOINT [ "python", "main.py"]
