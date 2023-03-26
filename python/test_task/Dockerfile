FROM python:3.11.2

RUN mkdir -p /opt/app

WORKDIR /opt/app

COPY requirements.txt .
COPY main.py .

RUN pip install --no-cache-dir -r requirements.txt


#EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
