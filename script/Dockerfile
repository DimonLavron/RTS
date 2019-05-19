FROM python:3.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY /home/script /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY mosquitto mosquitto

COPY withouthard.py checkpointId.txt ./

CMD ["python", "./withouthard.py"]
