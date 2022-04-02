FROM python:3.9 as base

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Temporal solution due to Github 100 Mb file restriction
RUN mkdir ./data
COPY ./src/data/interactions.csv.zip ./data
RUN unzip -o ./data/interactions.csv.zip -d ./data

# Testing image
FROM base as testing

RUN pip install pytest && pip install requests

# Prod
COPY ./src /code 

# Dev
# VOLUME /code

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
