FROM python:3.12.4

WORKDIR /usr/src/djangotrade_reads_backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip 

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
