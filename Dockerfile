FROM python:3.9.5-slim-buster
LABEL Author="tomer.shaiman@gmail.com"

WORKDIR /app
COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY . . 
CMD ["python" , "server.py"]