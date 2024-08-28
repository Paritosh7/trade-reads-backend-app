FROM python:3.12.4

WORKDIR /usr/src/djangotrade_reads_backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-traditional

RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/djangotrade_reads_backend/entrypoint.sh
RUN chmod +x /usr/src/djangotrade_reads_backend/entrypoint.sh 


COPY . .

ENTRYPOINT [ "/usr/src/djangotrade_reads_backend/entrypoint.sh" ]
