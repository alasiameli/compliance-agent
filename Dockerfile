
FROM debian:latest

MAINTAINER Melisa Alasia "alasiameli@gmail.com"
RUN apt update
RUN apt -y upgrade
RUN apt -y install python3-pip build-essential libssl-dev libffi-dev python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]