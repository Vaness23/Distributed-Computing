FROM ubuntu:latest
LABEL maintainer="Ivan Bobkov"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential curl

COPY ./app-server.py .
COPY ./requirements.txt .

WORKDIR ./

RUN curl https://bootstrap.pypa.io/get-pip.py | python3
RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3", "app-server.py"]